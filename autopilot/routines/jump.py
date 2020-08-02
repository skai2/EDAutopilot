from time import sleep

from autopilot.control import keys, send
from autopilot.edlog import ship
from autopilot.routines import align


def jump():
    # logging.debug('jump')
    tries = 3
    for i in range(tries):
        # logging.debug('jump= try:'+str(i))
        if not (ship()['status'] == 'in_supercruise' or ship()['status'] == 'in_space'):
            # logging.error('jump=err1')
            raise Exception('not ready to jump')
        sleep(0.5)
        # logging.debug('jump= start fsd')
        send(keys['HyperSuperCombination'], hold=1)
        sleep(16)
        if ship()['status'] != 'starting_hyperspace':
            # logging.debug('jump= misalign stop fsd')
            send(keys['HyperSuperCombination'], hold=1)
            sleep(2)
            align()
        else:
            # logging.debug('jump= in jump')
            while ship()['status'] != 'in_supercruise':
                sleep(1)
            # logging.debug('jump= speed 0')
            send(keys['SetSpeedZero'])
            # logging.debug('jump=complete')
            return True
    # logging.error('jump=err2')
    raise Exception("jump failure")


if __name__ == '__main__':
    sleep(5)
    jump()
