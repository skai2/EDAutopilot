################################################################################
#                       Elite Dangerous Autopilot v2
#    A computer vision based, completely external autopilot module for ED
################################################################################
from time import sleep

from autopilot.control import keys, send
from autopilot.edlog import ship
from autopilot.routines import align, jump, refuel, reposition


def activate():
    # logging.info('\n'+200*'-'+'\n'+'---- AUTOPILOT START '+179*'-'+'\n'+200*'-')
    # logging.info('get_latest_log='+str(get_latest_log(PATH_LOG_FILES)))
    # logging.debug('ship='+str(ship()))
    #     if ship()['target']:
    #         undock()
    while ship()['target']:
        if ship()['status'] == 'in_space' or ship()['status'] == 'in_supercruise':
            # logging.info('\n'+200*'-'+'\n'+'---- AUTOPILOT ALIGN '+179*'-'+'\n'+200*'-')
            align()
            # logging.info('\n'+200*'-'+'\n'+'---- AUTOPILOT JUMP '+180*'-'+'\n'+200*'-')
            jump()
            # logging.info('\n'+200*'-'+'\n'+'---- AUTOPILOT REFUEL '+178*'-'+'\n'+200*'-')
            refueled = refuel()
            # logging.info('\n'+200*'-'+'\n'+'---- AUTOPILOT POSIT '+179*'-'+'\n'+200*'-')
            if refueled:
                reposition(refueled_multiplier=4)
            else:
                reposition(refueled_multiplier=1)
    send(keys['SetSpeedZero'])
    # logging.info('\n'+200*'-'+'\n'+'---- AUTOPILOT END '+181*'-'+'\n'+200*'-')


if __name__ == '__main__':
    sleep(5)
    activate()
