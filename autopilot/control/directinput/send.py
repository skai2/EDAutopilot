from dataclasses import dataclass
from time import sleep

from win32gui import GetWindowText, GetForegroundWindow

from autopilot.control.directinput.directinput import PressKey, ReleaseKey
from autopilot.configs import config

@dataclass
class Configuration:
    key_mod_delay: float
    key_default_delay: float
    key_repeat_delay: float

def send(key, hold=None, repeat=1, repeat_delay=None, state=None):
    """Sends specified key if ED is active window"""
    KEY_MOD_DELAY = config.key_mod_delay
    KEY_DEFAULT_DELAY = config.key_default_delay
    KEY_REPEAT_DELAY = config.key_repeat_delay

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


if __name__ == '__main__':
    directinput_testkey = {'HyperSuperCombination': {'pre_key': 'DIK_F', 'key': 33}}
    sleep(3)
    send(directinput_testkey['HyperSuperCombination'])
