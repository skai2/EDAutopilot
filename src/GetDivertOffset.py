# import the necessary packages
import numpy as np
import argparse
import cv2
import ctypes
import mss

# gets screen resolution for screenshot
user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
# gets frame from screenshot
screen = {'top': 0, 'left': 0, 'width': screenWidth, 'height': screenHeight}
with mss.mss() as sct:
        # Get raw pixels from the screen, save it to a Numpy array (cv2 mat)
        original = np.array(sct.grab(screen))

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# args = vars(ap.parse_args())
# original = cv2.imread(args["image"])

# load the image, clone it for output
output = original.copy()
output = output[round(screenHeight *2/3) : round(screenHeight) ,
              round(screenWidth *1/4)  : round(screenWidth * 2/4)]

# error handling
def error(e):
    print(e)
    exit()



# ------------------------------------------------------------------------------

image = original.copy()
# blur the image
image = cv2.GaussianBlur(image,(31,31),0)
# convert image to hsv for light filtering
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Light bounds for filtering
lowerLight = np.array([0,0,240])
upperLight = np.array([255,255,255])
# mask
image = cv2.inRange(image, lowerLight, upperLight)
# blur the image
image = cv2.GaussianBlur(image,(151,151),0)

# deliver info with CV precision (oh yeah)



# show the output after resizing
image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
# output = cv2.resize(output, (0,0), fx=0.5, fy=0.5)
cv2.imshow("processed", image)
cv2.waitKey(0)
