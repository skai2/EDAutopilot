from time import sleep

from autopilot.configs import config
from autopilot.control import keybinds
from autopilot.control.directinput import directinput_keys
from autopilot.control.directinput.send import send
from autopilot.vision import sun_percent

keys = keybinds.get_latest()
keys = directinput_keys.get(keys)


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
        send(keys['PrimaryFire'], state=1)
    elif scan == 2:
        # logging.debug('position=scanning')
        send(keys['SecondaryFire'], state=1)
    send(keys['PitchUpButton'], state=1)
    sleep(5)
    send(keys['PitchUpButton'], state=0)
    send(keys['SetSpeed100'])
    send(keys['PitchUpButton'], state=1)
    while sun_percent.get() > 3:
        sleep(1)
    sleep(5)
    send(keys['PitchUpButton'], state=0)
    sleep(5 * refueled_multiplier)
    if scan == 1:
        # logging.debug('position=scanning complete')
        send(keys['PrimaryFire'], state=0)
    elif scan == 2:
        # logging.debug('position=scanning complete')
        send(keys['SecondaryFire'], state=0)
    # logging.debug('position=complete')
    return True


if __name__ == '__main__':
    sleep(5)
    reposition()
