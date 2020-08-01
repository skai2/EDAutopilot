from numpy import array

import cv2

from autopilot.configs import config
from autopilot.vision.display import screenshot


# TODO: Add more descriptive name
def orange(image=None, testing=False):
    while True:
        if testing:
            hsv = screenshot(left=(1 / 3) * config.display.width, top=(1 / 3) * config.display.height,
                             right=(2 / 3) * config.display.width, bottom=(2 / 3) * config.display.height)
        else:
            hsv = image.copy()
        # converting from BGR to HSV color space
        hsv = cv2.cvtColor(hsv, cv2.COLOR_RGB2HSV)
        # filter Elite UI orange
        filtered = cv2.inRange(hsv, array([0, 130, 123]), array([25, 235, 220]))
        if testing:
            cv2.imshow('Filtered', filtered)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return filtered


if __name__ == '__main__':
    orange(testing=True)
