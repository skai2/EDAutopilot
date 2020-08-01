from dataclasses import dataclass


@dataclass
class Configuration:
    scanner: str


default_configs_json = {
    "scanner": "primary_fire"
}

if __name__ == '__main__':
    print(default_configs_json)
