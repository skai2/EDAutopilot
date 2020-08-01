from autopilot.vision.helpers import screenshot
from autopilot.configs import config
from numpy import array
import cv2


def navpoint(image=None, testing=False):
    while True:
        if testing:
            hsv = screenshot(left=0.0, top=(2/3)*config.display.height,
                             right=(1/3)*config.display.width, bottom=config.display.height)
        else:
            hsv = image.copy()
        # converting from BGR to HSV color space
        hsv = cv2.cvtColor(hsv, cv2.COLOR_RGB2HSV)
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

