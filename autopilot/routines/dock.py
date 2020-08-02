from time import sleep

from autopilot.control import keys, send
from autopilot.edlog import ship


def dock():
    # logging.debug('dock')
    if not ship().status.in_space:
        # logging.error('dock=err1')
        raise Exception('dock error 1')
    tries = 3
    for i in range(tries):
        send(keys['UI_Back'], repeat=10)
        send(keys['HeadLookReset'])
        send(keys['UIFocus'], state=1)
        send(keys['UI_Left'])
        send(keys['UIFocus'], state=0)
        send(keys['CycleNextPanel'], repeat=2)
        send(keys['UI_Up'], hold=3)
        send(keys['UI_Right'])
        send(keys['UI_Select'])
        sleep(1)
        if ship().status.starting_docking or ship().status.in_docking:
            break
        if i > tries - 1:
            # logging.error('dock=err2')
            raise Exception("dock error 2")
    send(keys['UI_Back'])
    send(keys['HeadLookReset'])
    send(keys['SetSpeedZero'], repeat=2)
    wait = 120
    for i in range(wait):
        sleep(1)
        if i > wait - 1:
            # logging.error('dock=err3')
            raise Exception('dock error 3')
        if ship().status.in_station:
            break
    send(keys['UI_Up'], hold=3)
    send(keys['UI_Down'])
    send(keys['UI_Select'])
    # logging.debug('dock=complete')
    return True


if __name__ == '__main__':
    sleep(5)
    dock()
