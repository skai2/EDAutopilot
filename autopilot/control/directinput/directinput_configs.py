from dataclasses import dataclass


@dataclass
class Configuration:
    key_mod_delay: float
    key_default_delay: float
    key_repeat_delay: float


default_configs_json = {
    "key_mod_delay": "0.010",
    "key_default_delay": "0.200",
    "key_repeat_delay": "0.100"
}

if __name__ == '__main__':
    print(default_configs_json)
