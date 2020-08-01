from random import random

import cv2
from numpy import where

from autopilot.helpers import resource_path
from autopilot.vision import filters, get_compass_image


def get_navpoint_offset(testing=False, last=None):
    global same_last_count, last_last
    navpoint_template = cv2.imread(resource_path("templates/navpoint.png"), cv2.IMREAD_GRAYSCALE)
    navpoint_width, navpoint_height = navpoint_template.shape[::-1]
    pt = (0, 0)
    while True:
        compass_image, compass_width, compass_height = get_compass_image()
        mask_blue = filters.nav_blue(compass_image)
        # filtered = filter_bright(compass_image)
        match = cv2.matchTemplate(mask_blue, navpoint_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.5
        loc = where(match >= threshold)
        for point in zip(*loc[::-1]):
            pt = point
        final_x = (pt[0] + ((1 / 2) * navpoint_width)) - ((1 / 2) * compass_width)
        final_y = ((1 / 2) * compass_height) - (pt[1] + ((1 / 2) * navpoint_height))
        if testing:
            cv2.rectangle(compass_image, pt, (pt[0] + navpoint_width, pt[1] + navpoint_height), (0, 0, 255), 2)
            cv2.imshow('Navpoint Found', compass_image)
            cv2.imshow('Navpoint Mask', mask_blue)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    if pt[0] == 0 and pt[1] == 0:
        if last:
            if last == last_last:
                same_last_count = same_last_count + 1
            else:
                last_last = last
                same_last_count = 0
            if same_last_count > 5:
                same_last_count = 0
                if random() < .9:
                    result = {'x': 1, 'y': 100}
                else:
                    result = {'x': 100, 'y': 1}
            else:
                result = last
        else:
            result = None
    else:
        result = {'x': final_x, 'y': final_y}
    # logging.debug('get_navpoint_offset='+str(result))
    return result


if __name__ == '__main__':
    get_navpoint_offset(testing=True)
