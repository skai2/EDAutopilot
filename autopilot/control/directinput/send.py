from time import sleep

from win32gui import GetWindowText, GetForegroundWindow

from autopilot.configs import config
from autopilot.control.directinput.main import PressKey, ReleaseKey


def send(key, hold=None, repeat=1, repeat_delay=None, state=None):
    """Sends specified key if ED is active window"""
    key_mod_delay = config.directinput.key_mod_delay
    key_default_delay = config.directinput.key_default_delay
    key_repeat_delay = config.directinput.key_repeat_delay

    # Halt if ED window is inactive
    if GetWindowText(GetForegroundWindow()) != 'Elite - Dangerous (CLIENT)':
        # logging, handling, etc
        raise Exception("ED:Autopilot halted due to inactive window")

    if key is None:
        # logging.warning('SEND=NONE !!!!!!!!')
        return

    # logging.debug('send=key:' + str(key) + ',hold:' + str(hold) + ',repeat:' + str(repeat) + ',repeat_delay:' + str(repeat_delay) + ',state:' + str(state))
    for i in range(repeat):

        if state is None or state == 1:
            if 'mod' in key:
                PressKey(key['mod'])
                sleep(key_mod_delay)

            PressKey(key['key'])

        if state is None:
            if hold:
                sleep(hold)
            else:
                sleep(key_default_delay)

        if state is None or state == 0:
            ReleaseKey(key['key'])

            if 'mod' in key:
                sleep(key_mod_delay)
                ReleaseKey(key['mod'])

        if repeat_delay:
            sleep(repeat_delay)
        else:
            sleep(key_repeat_delay)


if __name__ == '__main__':
    directinput_testkey = {'HyperSuperCombination': {'pre_key': 'DIK_F', 'key': 33}}
    sleep(5)
    send(directinput_testkey['HyperSuperCombination'])
