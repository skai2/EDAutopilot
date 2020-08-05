from time import sleep

from autopilot.configs import config
from autopilot.control import keyboard, keys
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

    scan = get_scanner()
    if scan == 1:
        # logging.debug('position=scanning')
        keyboard.press(keys['PrimaryFire'])
    elif scan == 2:
        # logging.debug('position=scanning')
        keyboard.press(keys['SecondaryFire'])
    keyboard.press(keys['PitchUpButton'])
    sleep(5)
    keyboard.release(keys['PitchUpButton'])
    keyboard.tap(keys['SetSpeed100'])
    keyboard.press(keys['PitchUpButton'])
    while get_sun_percent() > 3:
        sleep(1)
    sleep(5)
    keyboard.release(keys['PitchUpButton'])
    sleep(5 * refueled_multiplier)
    if scan == 1:
        # logging.debug('position=scanning complete')
        keyboard.release(keys['PrimaryFire'])
    elif scan == 2:
        # logging.debug('position=scanning complete')
        keyboard.release(keys['SecondaryFire'])
    # logging.debug('position=complete')
    return True


if __name__ == '__main__':
    sleep(5)
    reposition()
