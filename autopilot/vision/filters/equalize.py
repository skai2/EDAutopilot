import cv2

from autopilot.configs import config
from autopilot.vision.display import screenshot


# TODO: Add more descriptive name
def equalize(image=None, testing=False):
    """Equalizes received image"""
    while True:
        if testing:
            img = screenshot(left=(5 / 16) * config.display.width, top=(5 / 8) * config.display.height,
                             right=(2 / 4) * config.display.width, bottom=(15 / 16) * config.display.height)
        else:
            img = image.copy()
        # Load the image in greyscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # create a CLAHE object (Arguments are optional).
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        img_out = clahe.apply(img_gray)
        if testing:
            cv2.imshow('Equalized', img_out)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            break
    return img_out


if __name__ == '__main__':
    equalize(testing=True)
