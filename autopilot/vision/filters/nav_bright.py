import cv2
from numpy import array

from autopilot.configs import config
from autopilot.vision.display.screenshot import screenshot
from autopilot.vision.filters import equalize


def nav_bright(image=None, testing=False):
    while True:
        if testing:
            img = screenshot(left=(5 / 16) * config.display.width, top=(5 / 8) * config.display.height,
                             right=(2 / 4) * config.display.width, bottom=(15 / 16) * config.display.height)
        else:
            img = image.copy()
        equalized = equalize(img)
        equalized = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
        equalized = cv2.cvtColor(equalized, cv2.COLOR_BGR2HSV)
        filtered = cv2.inRange(equalized, array([0, 0, 215]), array([0, 0, 255]))
        if testing:
            cv2.imshow('Filtered', filtered)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return filtered


if __name__ == '__main__':
    nav_bright(testing=True)
