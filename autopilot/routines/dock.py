from time import sleep

from autopilot.control.Keyboard import Keyboard
from autopilot.edlog import ship


def dock():
    # logging.debug('dock')
    if not ship().status.in_space:
        # logging.error('dock=err1')
        raise Exception('dock error 1')
    
    keyboard = Keyboard()

    tries = 3
    for i in range(tries):
        keyboard.tap(keyboard.keybinds['UI_Back'], repeat=10)
        keyboard.tap(keyboard.keybinds['HeadLookReset'])
        keyboard.press(keyboard.keybind['UIFocus'])
        keyboard.tap(keyboard.keybinds['UI_Left'])
        keyboard.release(keyboard.keybinds['UIFocus'])
        keyboard.tap(keyboard.keybinds['CycleNextPanel'], repeat=2)
        keyboard.hold(keyboard.keybinds['UI_Up'], hold=3)
        keyboard.tap(keyboard.keybinds['UI_Right'])
        keyboard.tap(keyboard.keybinds['UI_Select'])
        sleep(1)
        if ship().status.starting_docking or ship().status.in_docking:
            break
        if i > tries - 1:
            # logging.error('dock=err2')
            raise Exception("dock error 2")
    keyboard.tap(keyboard.keybinds['UI_Back'])
    keyboard.tap(keyboard.keybinds['HeadLookReset'])
    keyboard.tap(keyboard.keybinds['SetSpeedZero'], repeat=2)
    wait = 120
    for i in range(wait):
        sleep(1)
        if i > wait - 1:
            # logging.error('dock=err3')
            raise Exception('dock error 3')
        if ship().status.in_station:
            break
    keyboard.hold(keyboard.keybinds['UI_Up'], hold=3)
    keyboard.tap(keyboard.keybinds['UI_Down'])
    keyboard.tap(keyboard.keybinds['UI_Select'])
    # logging.debug('dock=complete')
    return True


if __name__ == '__main__':
    sleep(5)
    dock()
