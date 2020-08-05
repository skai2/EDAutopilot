import glob
import logging
import pathlib
from dataclasses import dataclass, field
from os import environ
from os.path import join, getmtime
from time import sleep
from typing import List
from xml.etree.ElementTree import parse

from win32gui import GetWindowText, GetForegroundWindow

from autopilot.configs import config
from autopilot.control import directinput
from autopilot.control.EDKeyCodes import EDKeyCodes


@dataclass
class ModKey:
    EDKeyCode: str
    ScanCode: int


@dataclass
class InputKey:
    EDKeyCode: str = field(default="")
    ScanCode: int = field(default=0)
    mod: List[ModKey] = field(default_factory=list)


class Keyboard:
    default_path = join(environ['LOCALAPPDATA'], 'Frontier Developments\Elite Dangerous\Options\Bindings')

    required_keys = [
        'YawLeftButton',
        'YawRightButton',
        'RollLeftButton',
        'RollRightButton',
        'PitchUpButton',
        'PitchDownButton',
        'SetSpeedZero',
        'SetSpeed100',
        'HyperSuperCombination',
        'UIFocus',
        'UI_Up',
        'UI_Down',
        'UI_Left',
        'UI_Right',
        'UI_Select',
        'UI_Back',
        'CycleNextPanel',
        'HeadLookReset',
        'PrimaryFire',
        'SecondaryFire',
        'MouseReset'
    ]

    keybinds = {}

    KEY_MOD_DELAY = config.directinput.key_mod_delay
    KEY_DEFAULT_DELAY = config.directinput.key_default_delay
    KEY_REPEAT_DELAY = config.directinput.key_repeat_delay

    def __init__(self, cv_testing=False):
        self.cv_testing = cv_testing
        self._get_bindings()

        # TODO: Check if this was the intention behind the logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('Keyboard.log')
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)

        for key in self.required_keys:
            try:
                self.logger.info('get_bindings: ' + str(key) + ' = ' + str(self.keybinds[key]))
            except Exception as e:
                self.logger.warning(str("get_bindings: " + key + " = does not have a valid keybind.").upper())

    # Get latest keybinds file
    def _get_latest_keybinds(self, path_bindings=None):
        if not path_bindings:
            path_bindings = self.default_path

        """Returns the full path of the latest elite keybinds file from specified path"""
        path_to_search = pathlib.Path(path_bindings)
        list_of_files = glob.glob(str(path_to_search) + '\*.binds')
        latest_file = max(list_of_files, key=getmtime)
        return latest_file

    def _get_bindings(self, keysToObtain=None):
        """Returns a dict struct with the direct input equivalent of the necessary elite keybindings"""
        if keysToObtain is None:
            keysToObtain = self.required_keys

        latest_bindings = self._get_latest_keybinds()
        bindings_tree = parse(latest_bindings)
        bindings_root = bindings_tree.getroot()

        keybinds = {}

        for item in bindings_root:
            if item.tag in keysToObtain:
                EDName = item.tag
                binding = InputKey()
                '''{
                    'EDKeyCode': None,
                    'VKCode': None,
                    'mod': []
                }'''

                # Check primary
                if item[0].attrib['Device'].strip() == "Keyboard":
                    binding.EDKeyCode = item[0].attrib['Key']
                    binding.ScanCode = EDKeyCodes[item[0].attrib['Key']]
                    for ii in range(len(item[0])):
                        binding.mod.append(ModKey(item[0][ii].attrib['Key'], EDKeyCodes[item[0][ii].attrib['Key']]))

                # Check secondary
                elif item[1].attrib['Device'].strip() == "Keyboard":
                    binding.EDKeyCode = item[1].attrib['Key']
                    binding.ScanCode = EDKeyCodes[item[1].attrib['Key']]
                    for ii in range(len(item[1])):
                        binding.mod.append(ModKey(item[1][ii].attrib['Key'], EDKeyCodes[item[1][ii].attrib['Key']]))

                keybinds[EDName] = binding

        if keybinds == {}:
            self.keybinds = None
        else:
            self.keybinds = keybinds

    # Direct input function
    # Send input
    def press(self, key: InputKey):
        # Halt if ED window is inactive
        if GetWindowText(GetForegroundWindow()) != 'Elite - Dangerous (CLIENT)':
            # if GetWindowText(GetForegroundWindow()) != 'Elite - Dangerous (CLIENT)':
            # logging, handling, etc
            raise Exception("ED:Autopilot halted due to inactive window")
            # raise Exception("ED:Autopilot halted due to inactive window")

        if not self.cv_testing:
            if key is None:
                self.logger.warning('SEND=NONE !!!!!!!!')
                return

            self.logger.debug('press=key:' + str(key))
            for mod in key.mod:
                directinput.press_key(mod.ScanCode)
                sleep(self.KEY_MOD_DELAY)
            directinput.press_key(key.ScanCode)

    def release(self, key: InputKey):
        # Halt if ED window is inactive
        if GetWindowText(GetForegroundWindow()) != 'Elite - Dangerous (CLIENT)':
            # if GetWindowText(GetForegroundWindow()) != 'Elite - Dangerous (CLIENT)':
            # logging, handling, etc
            raise Exception("ED:Autopilot halted due to inactive window")
            # raise Exception("ED:Autopilot halted due to inactive window")

        if not self.cv_testing:
            if key is None:
                self.logger.warning('SEND=NONE !!!!!!!!')
                return

            self.logger.debug('release=key:' + str(key))
            directinput.release_key(key.ScanCode)
            for mod in key.mod:
                directinput.release_key(mod.ScanCode)

    def tap(self, key: InputKey, repeat: int = 1):
        if not self.cv_testing:
            if repeat < 1:
                self.logger.warning('Repeat must be greater than 0')
                return
            for _ in range(repeat):
                if key is None:
                    self.logger.warning('SEND=NONE !!!!!!!!')
                    return

                self.logger.debug('tap=key:' + str(key))
                self.press(key)
                sleep(self.KEY_DEFAULT_DELAY)
                self.release(key)

    def hold(self, key: InputKey, hold: float):
        if not self.cv_testing:
            if key is None:
                self.logger.warning('SEND=NONE !!!!!!!!')
                return

            self.logger.debug('tap=key:' + str(key) + ',hold:' + str(hold))
            self.press(key)
            sleep(hold if hold > self.KEY_DEFAULT_DELAY else self.KEY_DEFAULT_DELAY)
            self.release(key)

    def clear_input(self, to_clear=None):
        if not self.cv_testing:
            logging.info('---- CLEAR INPUT ' + 183 * '-')
            self.tap(to_clear['SetSpeedZero'])
            self.tap(to_clear['MouseReset'])

            if to_clear is None:
                to_clear = self.keybinds

            for key_to_clear in to_clear.keys():
                if key_to_clear in self.keybinds:
                    self.release(to_clear[key_to_clear])
            logging.debug('clear_input')


if __name__ == "__main__":
    for i in list(range(3))[::-1]:
        print(i + 1)
        sleep(1)
    print('press')

    keyboardTest = Keyboard()
    keyboardTest.tap(keyboardTest.keybinds['UI_Up'])
