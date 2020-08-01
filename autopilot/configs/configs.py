import json
import pathlib
from dataclasses import dataclass
from distutils.version import StrictVersion
from os.path import isfile, join

import dacite as dacite

from autopilot.control.directinput import directinput_configs
from autopilot.vision.display import display_configs

_DEFAULT_CONFIGS_PATH = join(pathlib.Path(__file__).parent, '../configs.json')

_DEFAULT_CONFIG_JSON = {
    "version": "1.0.0",
    "display": display_configs.default_configs_json,
    'directinput': directinput_configs.default_configs_json,
    "routines": {
        "function_default_delay": "0.500"
    }
}


@dataclass
class Configuration:
    version: StrictVersion
    display: display_configs.Configuration
    directinput: directinput_configs.Configuration


def _create_default_configs(configs_path):
    with open(configs_path, 'w', encoding='utf8') as json_file:
        json.dump(_DEFAULT_CONFIG_JSON, json_file)


def _read_configs_json(configs_path):
    if not isfile(configs_path):
        _create_default_configs(configs_path)
    with open(configs_path, 'r', encoding='utf8') as json_file:
        configs_json = json.load(json_file)
    return configs_json


# define converters for values used in configuration file
_converters = {
    StrictVersion: StrictVersion,
    pathlib.Path: pathlib.Path,
    int: int,
    float: float
}
# create and validate the Configuration object
config = dacite.from_dict(
    data_class=Configuration, data=_read_configs_json(_DEFAULT_CONFIGS_PATH),
    config=dacite.Config(type_hooks=_converters),
)

if __name__ == '__main__':
    print(config)
