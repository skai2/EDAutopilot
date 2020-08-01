from autopilot.configs import config
from numpy import array

import cv2

from autopilot.vision.display import screenshot
from autopilot.vision.filters.equalize import equalize


# TODO: Add more descriptive name
def hsv_slider(bandw=False):
    """Tool to test different HSV filters on screen"""
    cv2.namedWindow('image')

    # Min and max values for H (hue), S (saturation) and V (value/brightness)
    min_h = 0
    max_h = 179
    min_s = 0
    max_s = 255
    min_v = 0
    max_v = 255

    # TODO: Check if callback should be doing something
    def callback(x):
        pass

    # create trackbars for color change
    cv2.createTrackbar('lowH', 'image', min_h, 179, callback)
    cv2.createTrackbar('highH', 'image', max_h, 179, callback)

    cv2.createTrackbar('lowS', 'image', min_s, 255, callback)
    cv2.createTrackbar('highS', 'image', max_s, 255, callback)

    cv2.createTrackbar('lowV', 'image', min_v, 255, callback)
    cv2.createTrackbar('highV', 'image', max_v, 255, callback)

    while True:
        # grab the frame
        frame = screenshot(left=(5 / 16) * config.display.width, top=(5 / 8) * config.display.height,
                           right=(2 / 4) * config.display.width, bottom=(15 / 16) * config.display.height)
        if bandw:
            frame = equalize(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

        # get trackbar positions
        min_h = cv2.getTrackbarPos('lowH', 'image')
        max_h = cv2.getTrackbarPos('highH', 'image')
        min_s = cv2.getTrackbarPos('lowS', 'image')
        max_s = cv2.getTrackbarPos('highS', 'image')
        min_v = cv2.getTrackbarPos('lowV', 'image')
        max_v = cv2.getTrackbarPos('highV', 'image')

        hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        lower_hsv = array([min_h, min_s, min_v])
        higher_hsv = array([max_h, max_s, max_v])
        mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

        frame = cv2.bitwise_and(frame, frame, mask=mask)

        # show thresholded image
        cv2.imshow('image', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    hsv_slider(bandw=False)
