import cv2
from numpy import array

from autopilot.configs import config
from autopilot.vision.display import screenshot


def nav_blue(image=None, testing=False):
    while True:
        if testing:
            hsv = screenshot(left=(1 / 6) * config.display.width, top=(2 / 3) * config.display.height,
                             right=(3 / 6) * config.display.width, bottom=config.display.height)
        else:
            hsv = image.copy()
        # converting from BGR to HSV color space
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
        # filter Elite UI orange
        filtered = cv2.inRange(hsv, array([0, 0, 200]), array([180, 100, 255]))
        if testing:
            cv2.imshow('Filtered', filtered)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return filtered


if __name__ == '__main__':
    nav_blue(testing=True)
