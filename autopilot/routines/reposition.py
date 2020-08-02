from time import sleep

from autopilot.configs import config
from autopilot.control.Keyboard import Keyboard
from autopilot.vision import get_sun_percent


def get_scanner():
    if config.routines.scanner == 'primary_fire':
        return 1
    elif config.routines.scanner == 'secondary_fire':
        return 2
    else:
        raise Exception("Invalid configuration for routines.scanner. Must be primary_fire or secondary_fire")


def reposition(refueled_multiplier=1):
    # logging.debug('position')
    keyboard = Keyboard()

    scan = get_scanner()
    if scan == 1:
        # logging.debug('position=scanning')
        keyboard.press(keyboard.keybinds['PrimaryFire'])
    elif scan == 2:
        # logging.debug('position=scanning')
        keyboard.press(keyboard.keybinds['SecondaryFire'])
    keyboard.press(keyboard.keybinds['PitchUpButton'])
    sleep(5)
    keyboard.release(keyboard.keybinds['PitchUpButton'])
    keyboard.tap(keyboard.keybinds['SetSpeed100'])
    keyboard.press(keyboard.keybinds['PitchUpButton'])
    while get_sun_percent() > 3:
        sleep(1)
    sleep(5)
    keyboard.release(keyboard.keybinds['PitchUpButton'])
    sleep(5 * refueled_multiplier)
    if scan == 1:
        # logging.debug('position=scanning complete')
        keyboard.release(keyboard.keybinds['PrimaryFire'])
    elif scan == 2:
        # logging.debug('position=scanning complete')
        keyboard.release(keyboard.keybinds['SecondaryFire'])
    # logging.debug('position=complete')
    return True


if __name__ == '__main__':
    sleep(5)
    reposition()
