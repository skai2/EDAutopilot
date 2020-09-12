from time import sleep

from autopilot.control import keyboard, keys
from autopilot.elite import ship


def undock():
    # logging.debug('undock')
    if ship().status.in_station:
        # logging.error('undock=err1')
        raise Exception('undock error 1')
    keyboard.tap(keys['UI_Back'], repeat=10)
    keyboard.tap(keys['HeadLookReset'])
    keyboard.hold(keys['UI_Down'], hold=3)
    keyboard.tap(keys['UI_Select'])
    sleep(1)
    if not (ship().status.starting_undocking or ship().status.in_undocking):
        # logging.error('undock=err2')
        raise Exception("undock error 2")
    keyboard.tap(keys['HeadLookReset'])
    keyboard.tap(keys['SetSpeedZero'], repeat=2)
    wait = 120
    for i in range(wait):
        sleep(1)
        if i > wait - 1:
            # logging.error('undock=err3')
            raise Exception('undock error 3')
        if ship().status.in_space:
            break
    # logging.debug('undock=complete')
    return True


if __name__ == '__main__':
    sleep(5)
    undock()
