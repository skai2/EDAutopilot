from time import sleep

from autopilot.control.Keyboard import Keyboard
from autopilot.edlog import ship


def undock():
    # logging.debug('undock')
    keyboard = Keyboard()
    if ship().status.in_station:
        # logging.error('undock=err1')
        raise Exception('undock error 1')
    keyboard.tap(keyboard.keybinds['UI_Back'], repeat=10)
    keyboard.tap(keyboard.keybinds['HeadLookReset'])
    keyboard.hold(keyboard.keybinds['UI_Down'], hold=3)
    keyboard.tap(keyboard.keybinds['UI_Select'])
    sleep(1)
    if not (ship().status.starting_undocking or ship().status.in_undocking):
        # logging.error('undock=err2')
        raise Exception("undock error 2")
    keyboard.tap(keyboard.keybinds['HeadLookReset'])
    keyboard.tap(keyboard.keybinds['SetSpeedZero'], repeat=2)
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
