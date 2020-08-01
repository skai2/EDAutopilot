import numpy as np

from autopilot.configs import config
from autopilot.vision import filters
from autopilot.vision.display.screenshot import screenshot


def get():
    screen = screenshot((1 / 3) * config.display.width, (1 / 3) * config.display.height, (2 / 3) * config.display.width,
                        (2 / 3) * config.display.height)
    filtered = filters.star_bright(screen)
    white = np.sum(filtered == 255)
    black = np.sum(filtered != 255)
    result = white / black
    return result * 100


if __name__ == '__main__':
    print(get())
