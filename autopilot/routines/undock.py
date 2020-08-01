from time import sleep

from autopilot.control import keybinds
from autopilot.control.directinput import directinput_keys
from autopilot.control.directinput.send import send
from autopilot.edlog import ship

keys = keybinds.get_latest()
keys = directinput_keys.get(keys)


def undock():
    # logging.debug('undock')
    if ship()['status'] != "in_station":
        # logging.error('undock=err1')
        raise Exception('undock error 1')
    send(keys['UI_Back'], repeat=10)
    send(keys['HeadLookReset'])
    send(keys['UI_Down'], hold=3)
    send(keys['UI_Select'])
    sleep(1)
    if not (ship()['status'] == "starting_undock" or ship()['status'] == "in_undock"):
        # logging.error('undock=err2')
        raise Exception("undock error 2")
    send(keys['HeadLookReset'])
    send(keys['SetSpeedZero'], repeat=2)
    wait = 120
    for i in range(wait):
        sleep(1)
        if i > wait - 1:
            # logging.error('undock=err3')
            raise Exception('undock error 3')
        if ship()['status'] == "in_space":
            break
    # logging.debug('undock=complete')
    return True


if __name__ == '__main__':
    sleep(5)
    undock()
