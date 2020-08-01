from time import sleep

from autopilot.control.directinput.directinput import PressKey, ReleaseKey


def send(key, hold=None, repeat=1, repeat_delay=None, state=None):
    """Sends specified key"""
    global KEY_MOD_DELAY, KEY_DEFAULT_DELAY, KEY_REPEAT_DELAY

    if key is None:
        # logging.warning('SEND=NONE !!!!!!!!')
        return

    # logging.debug('send=key:' + str(key) + ',hold:' + str(hold) + ',repeat:' + str(repeat) + ',repeat_delay:' + str(repeat_delay) + ',state:' + str(state))
    for i in range(repeat):

        if state is None or state == 1:
            if 'mod' in key:
                PressKey(key['mod'])
                sleep(KEY_MOD_DELAY)

            PressKey(key['key'])

        if state is None:
            if hold:
                sleep(hold)
            else:
                sleep(KEY_DEFAULT_DELAY)

        if state is None or state == 0:
            ReleaseKey(key['key'])

            if 'mod' in key:
                sleep(KEY_MOD_DELAY)
                ReleaseKey(key['mod'])

        if repeat_delay:
            sleep(repeat_delay)
        else:
            sleep(KEY_REPEAT_DELAY)
