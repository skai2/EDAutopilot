# Get status of ship being used
from dataclasses import dataclass
from datetime import datetime
from json import loads
from os.path import getmtime
from pathlib import Path

from dacite import from_dict, Config

from autopilot.edlog.journal import get_latest_journal_path

@dataclass
class Status:
    in_station: bool
    starting_undocking: bool
    in_undocking: bool
    in_space: bool
    in_supercruise: bool
    starting_hyperspace: bool
    starting_docking: bool
    in_docking: bool

@dataclass
class Ship:
    time: int
    status: Status
    type: str
    location: str
    star_class: str
    has_target: bool
    target: str
    fuel_capacity: float
    fuel_level: float
    fuel_percent: int
    is_scooping: bool
    log_path: Path


_converters = {
    bool: bool,
    int: int,
    float: float,
    str: str,
    Path: Path
}


def ship():
    ship_json = get_ship_json()
    ship_class = from_dict(data_class=Ship, data=ship_json, config=Config(type_hooks=_converters))
    return ship_class


def get_statuses(current_status):
    statuses = {
        'in_station': False,
        'starting_undocking': False,
        'in_undocking': False,
        'in_space': False,
        'in_supercruise': False,
        'starting_hyperspace': False,
        'starting_docking': False,
        'in_docking': False
    }
    for status in statuses.keys():
        if status == current_status:
            statuses[status] = True
    return statuses



def get_ship_json():
    """Returns a ship dict containing relevant game status information (state, fuel, ...)"""
    latest_journal = get_latest_journal_path()
    ship_json = {
        'time': (datetime.now() - datetime.fromtimestamp(getmtime(latest_journal))).seconds,
        'parsed_status': None,
        'status': None,
        'type': None,
        'location': None,
        'star_class': None,
        'has_target': False,
        'target': None,
        'fuel_capacity': None,
        'fuel_level': None,
        'fuel_percent': None,
        'is_scooping': False,
        'log_path': Path(latest_journal)
    }
    # Read log line by line and parse data
    with open(latest_journal, encoding="utf-8") as f:
        for line in f:
            log = loads(line)

            # parse data
            try:
                # parse ship status
                log_event = log['event']

                if log_event == 'StartJump':
                    ship_json['parsed_status'] = str('starting_' + log['JumpType']).lower()

                elif log_event == 'SupercruiseEntry' or log_event == 'FSDJump':
                    ship_json['parsed_status'] = 'in_supercruise'

                elif log_event == 'SupercruiseExit' or log_event == 'DockingCancelled' or (
                        log_event == 'Music' and ship_json['parsed_status'] == 'in_undocking') or (
                        log_event == 'Location' and log['Docked'] == False):
                    ship_json['parsed_status'] = 'in_space'

                elif log_event == 'Undocked':
                    #                     ship['status'] = 'starting_undocking'
                    ship_json['parsed_status'] = 'in_space'

                elif log_event == 'DockingRequested':
                    ship_json['parsed_status'] = 'starting_docking'

                elif log_event == "Music" and log['MusicTrack'] == "DockingComputer":
                    if ship_json['parsed_status'] == 'starting_undocking':
                        ship_json['parsed_status'] = 'in_undocking'
                    elif ship_json['parsed_status'] == 'starting_docking':
                        ship_json['parsed_status'] = 'in_docking'

                elif log_event == 'Docked':
                    ship_json['parsed_status'] = 'in_station'

                # parse ship type
                if log_event == 'LoadGame' or log_event == 'Loadout':
                    ship_json['type'] = log['Ship']

                # parse fuel
                if 'FuelLevel' in log and ship_json['type'] != 'TestBuggy':
                    ship_json['fuel_level'] = log['FuelLevel']
                if 'FuelCapacity' in log and ship_json['type'] != 'TestBuggy':
                    try:
                        ship_json['fuel_capacity'] = log['FuelCapacity']['Main']
                    except:
                        ship_json['fuel_capacity'] = log['FuelCapacity']
                if log_event == 'FuelScoop' and 'Total' in log:
                    ship_json['fuel_level'] = log['Total']
                if ship_json['fuel_level'] and ship_json['fuel_capacity']:
                    ship_json['fuel_percent'] = round((ship_json['fuel_level'] / ship_json['fuel_capacity']) * 100)
                else:
                    ship_json['fuel_percent'] = 10

                # parse scoop
                if log_event == 'FuelScoop' and ship_json['time'] < 10 and ship_json['fuel_percent'] < 100:
                    ship_json['is_scooping'] = True
                else:
                    ship_json['is_scooping'] = False

                # parse location
                if (log_event == 'Location' or log_event == 'FSDJump') and 'StarSystem' in log:
                    ship_json['location'] = log['StarSystem']
                if 'StarClass' in log:
                    ship_json['star_class'] = log['StarClass']

                # parse target
                if log_event == 'FSDTarget':
                    if log['Name'] == ship_json['location']:
                        ship_json['target'] = ''
                    else:
                        ship_json['target'] = log['Name']
                        ship_json['has_target'] = True
                elif log_event == 'FSDJump':
                    if ship_json['location'] == ship_json['target']:
                        ship_json['target'] = ''

                ship_json['status'] = get_statuses(ship_json['parsed_status'])


            # exceptions
            except Exception as e:
                # logging.exception("Exception occurred")
                print(e)
    #     logging.debug('ship='+str(ship))
    return ship_json


if __name__ == '__main__':
    print(get_ship_json())
    print(ship())
    print(ship().status.in_space)
