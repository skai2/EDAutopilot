import numpy as np

from autopilot.vision import display, filters


def get_sun_percent():
    screen = display.screenshot((1 / 3) * display.width, (1 / 3) * display.height, (2 / 3) * display.width,
                                (2 / 3) * display.height)
    filtered = filters.star_bright(screen)
    white = np.sum(filtered == 255)
    black = np.sum(filtered != 255)
    result = white / black
    return result * 100


if __name__ == '__main__':
    print(get_sun_percent())
