import cv2
from numpy import array

from autopilot.configs import config
from autopilot.vision.display import screenshot


def ui_orange2(image=None, testing=False):
    while True:
        if testing:
            hsv = screenshot(left=(1 / 3) * config.display.width, top=(1 / 3) * config.display.height,
                             right=(2 / 3) * config.display.width, bottom=(2 / 3) * config.display.height)
        else:
            hsv = image.copy()
        # converting from BGR to HSV color space
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
        # filter Elite UI orange
        filtered = cv2.inRange(hsv, array([15, 220, 220]), array([30, 255, 255]))
        if testing:
            cv2.imshow('Filtered', filtered)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return filtered


if __name__ == '__main__':
    ui_orange2(testing=True)
