from time import sleep

from autopilot.control import keyboard, keys
from autopilot.edlog import ship


def dock():
    # logging.debug('dock')
    if not ship().status.in_space:
        # logging.error('dock=err1')
        raise Exception('dock error 1')

    tries = 3
    for i in range(tries):
        keyboard.tap(keys['UI_Back'], repeat=10)
        keyboard.tap(keys['HeadLookReset'])
        keyboard.press(keyboard.keybind['UIFocus'])
        keyboard.tap(keys['UI_Left'])
        keyboard.release(keys['UIFocus'])
        keyboard.tap(keys['CycleNextPanel'], repeat=2)
        keyboard.hold(keys['UI_Up'], hold=3)
        keyboard.tap(keys['UI_Right'])
        keyboard.tap(keys['UI_Select'])
        sleep(1)
        if ship().status.starting_docking or ship().status.in_docking:
            break
        if i > tries - 1:
            # logging.error('dock=err2')
            raise Exception("dock error 2")
    keyboard.tap(keys['UI_Back'])
    keyboard.tap(keys['HeadLookReset'])
    keyboard.tap(keys['SetSpeedZero'], repeat=2)
    wait = 120
    for i in range(wait):
        sleep(1)
        if i > wait - 1:
            # logging.error('dock=err3')
            raise Exception('dock error 3')
        if ship().status.in_station:
            break
    keyboard.hold(keys['UI_Up'], hold=3)
    keyboard.tap(keys['UI_Down'])
    keyboard.tap(keys['UI_Select'])
    # logging.debug('dock=complete')
    return True


if __name__ == '__main__':
    sleep(5)
    dock()
