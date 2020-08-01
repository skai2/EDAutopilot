from dataclasses import dataclass

import d3dshot

_d3d = d3dshot.create()

display = _d3d.display
displays = _d3d.displays

number = int(displays.index(display))
width = display.resolution[0]
height = display.resolution[1]


@dataclass
class Configuration:
    number: int
    width: int
    height: int


default_configs_json = {
    "number": str(number),
    "width": str(width),
    "height": str(height)
}

if __name__ == '__main__':
    print(default_configs_json)
