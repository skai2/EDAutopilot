import glob
import pathlib
from os import environ
from os.path import join, getmtime
from xml.etree.ElementTree import parse

default_path = join(environ['LOCALAPPDATA'], 'Frontier Developments\Elite Dangerous\Options\Bindings')

keys_needed = [
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
    'SecondaryFire'
]


def get_latest_path(path_to_search=default_path):
    """Returns the full path of the latest elite keybinds file from specified path"""
    path_to_search = pathlib.Path(path_to_search)
    list_of_files = glob.glob(str(path_to_search)+'\*.binds')
    latest_file = max(list_of_files, key=getmtime)
    return latest_file


def get_latest(keys_to_obtain=keys_needed):
    """Returns a dict with the ED names of bindings for keys_to_obtain"""
    key_bindings = {}
    latest_bindings = get_latest_path()
    bindings_tree = parse(latest_bindings)
    bindings_root = bindings_tree.getroot()

    for item in bindings_root:
        if item.tag in keys_to_obtain:
            key = None
            mod = None
            # Check primary
            if item[0].attrib['Device'].strip() == "Keyboard":
                key = item[0].attrib['Key']
                if len(item[0]) > 0:
                    mod = item[0][0].attrib['Key']
            # Check secondary (and prefer secondary)
            if item[1].attrib['Device'].strip() == "Keyboard":
                key = item[1].attrib['Key']
                if len(item[1]) > 0:
                    mod = item[1][0].attrib['Key']
            # Store binding
            key_bindings[item.tag] = {'mod': mod, 'key': key}

    if len(list(key_bindings.keys())) < 1:
        return None
    else:
        return key_bindings


if __name__ == '__main__':
    print(get_latest_path())
    print(get_latest())
