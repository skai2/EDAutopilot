from math import degrees, atan
from time import sleep

from autopilot.control import keybinds
from autopilot.control.directinput import directinput_keys
from autopilot.control.directinput.send import send
from autopilot.edlog import ship
from autopilot.vision import sun_percent, navpoint_offset, destination_offset

keys = keybinds.get_latest()
keys = directinput_keys.get(keys)


def x_angle(point=None):
    if not point or point['x'] == 0:
        return None
    result = degrees(atan(point['y'] / point['x']))
    if point['x'] > 0:
        return +90 - result
    else:
        return -90 - result


def align():
    # logging.debug('align')
    if not (ship()['status'] == 'in_supercruise' or ship()['status'] == 'in_space'):
        # logging.error('align=err1')
        raise Exception('align error 1')

    # logging.debug('align= speed 100')
    send(keys['SetSpeed100'])

    # logging.debug('align= avoid sun')
    while sun_percent.get() > 5:
        send(keys['PitchUpButton'], state=1)
    send(keys['PitchUpButton'], state=0)

    # logging.debug('align= find navpoint')
    off = navpoint_offset.get()
    while not off:
        send(keys['PitchUpButton'], state=1)
        off = navpoint_offset.get()
    send(keys['PitchUpButton'], state=0)

    # logging.debug('align= crude align')
    close = 3
    close_a = 18
    hold_pitch = 0.350
    hold_roll = 0.170
    ang = x_angle(off)
    while (off['x'] > close and ang > close_a) or (off['x'] < -close and ang < -close_a) or (off['y'] > close) or (
            off['y'] < -close):

        while (off['x'] > close and ang > close_a) or (off['x'] < -close and ang < -close_a):

            if off['x'] > close and ang > close:
                send(keys['RollRightButton'], hold=hold_roll)
            if off['x'] < -close and ang < -close:
                send(keys['RollLeftButton'], hold=hold_roll)

            if ship()['status'] == 'starting_hyperspace':
                return
            off = navpoint_offset.get(last=off)
            ang = x_angle(off)

        ang = x_angle(off)
        while (off['y'] > close) or (off['y'] < -close):

            if off['y'] > close:
                send(keys['PitchUpButton'], hold=hold_pitch)
            if off['y'] < -close:
                send(keys['PitchDownButton'], hold=hold_pitch)

            if ship()['status'] == 'starting_hyperspace':
                return
            off = navpoint_offset.get(last=off)
            ang = x_angle(off)

        off = navpoint_offset.get(last=off)
        ang = x_angle(off)

    # logging.debug('align= fine align')
    sleep(0.5)
    close = 50
    hold_pitch = 0.200
    hold_yaw = 0.400
    for i in range(5):
        new = destination_offset.get()
        if new:
            off = new
            break
        sleep(0.25)
    if not off:
        return
    while (off['x'] > close) or (off['x'] < -close) or (off['y'] > close) or (off['y'] < -close):

        if off['x'] > close:
            send(keys['YawRightButton'], hold=hold_yaw)
        if off['x'] < -close:
            send(keys['YawLeftButton'], hold=hold_yaw)
        if off['y'] > close:
            send(keys['PitchUpButton'], hold=hold_pitch)
        if off['y'] < -close:
            send(keys['PitchDownButton'], hold=hold_pitch)

        if ship()['status'] == 'starting_hyperspace':
            return

        for i in range(5):
            new = destination_offset.get()
            if new:
                off = new
                break
            sleep(0.25)
        if not off:
            return


if __name__ == '__main__':
    sleep(5)
    align()
