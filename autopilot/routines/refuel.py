from time import sleep

from autopilot.control import keyboard, keys
from autopilot.elite import ship


def refuel(refuel_threshold=33):
    # logging.debug('refuel')

    scoopable_stars = ['F', 'O', 'G', 'K', 'B', 'A', 'M']
    if ship().status.in_supercruise:
        # logging.error('refuel=err1')
        return False
        # raise Exception('not ready to refuel')

    if ship().fuel_percent < refuel_threshold and ship().star_class in scoopable_stars:
        # logging.debug('refuel= start refuel')
        keyboard.tap(keys['SetSpeed100'])
        #     while not ship()['is_scooping']:
        #         sleep(1)
        sleep(4)
        # logging.debug('refuel= wait for refuel')
        keyboard.tap(keys['SetSpeedZero'], repeat=3)
        while not ship().fuel_percent == 100:
            sleep(1)
        # logging.debug('refuel=complete')
        return True
    elif ship().fuel_percent >= refuel_threshold:
        # logging.debug('refuel= not needed')
        return False
    elif ship().fuel_percent not in scoopable_stars:
        # logging.debug('refuel= needed, unsuitable star')
        return False
    else:
        return False


if __name__ == '__main__':
    sleep(5)
    refuel()
