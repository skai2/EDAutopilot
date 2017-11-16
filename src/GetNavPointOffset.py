# import the necessary packages
import numpy as np
import argparse
import cv2
import ctypes
import mss
import sys

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
    sys.exit(0)



# NAVBALL ----------------------------------------------------------------------

image = original.copy()
image = image[round(screenHeight *2/3) : round(screenHeight) ,
              round(screenWidth *1/4)  : round(screenWidth * 2/4)]
# convert image to hsv for color filtering
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# orange (HSV 30|21.25 85|216.75 100|255) bounds for filtering
lowerOrange = np.array([0,67,195])
upperOrange = np.array([52,267,255])
# mask
image = cv2.inRange(image, lowerOrange, upperOrange)

# blur the image to prepare for hough transform
image = cv2.GaussianBlur(image,(15,15),0)

# convert image to grayscale for hough circle processing
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect circles in the image
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 100,
                        param1=100,param2=30,minRadius=15,maxRadius=50)

navBall = [0,0,0]
if circles is not None and len(circles) is 1:
    navBall = circles[0][0]
else:
    # NavBall not detected
    error(-1)

# ensure at least some circles were found
# if circles is not None:
# 	# convert the (x, y) coordinates and radius of the circles to integers
# 	circles = np.round(circles[0, :]).astype("int")#
#
# 	# loop over the (x, y) coordinates and radius of the circles
# 	for (x, y, r) in circles:
# 		# draw the circle in the output image, then draw a rectangle
# 		# corresponding to the center of the circle
# 		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
# 		# cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)



# NAVPOINT ----------------------------------------------------------------------

image = original.copy()
image = image[round(screenHeight *2/3) : round(screenHeight) ,
              round(screenWidth *1/4)  : round(screenWidth * 2/4)]
# convert image to hsv for color filtering
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# blue (HSV 180|127.5 28|71.4 100|255) bounds for filtering
lowerBlue = np.array([60,20,180])
upperBlue = np.array([190,130,255])
# mask
image = cv2.inRange(image, lowerBlue, upperBlue)
blueimg = image.copy()

# blur the image to prepare for hough transform
image = cv2.GaussianBlur(image,(9,9),0)

# convert image to grayscale for hough circle processing
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect circles in the image
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 100,
                        param1=100,param2=10,minRadius=1,maxRadius=15)

navPoint = [0,0,0]
if circles is not None and len(circles) is 1:
    navPoint = circles[0][0]
else:
    # NavPoint not detected
    error(-2)

# ensure at least some circles were found
# if circles is not None:
# 	# convert the (x, y) coordinates and radius of the circles to integers
# 	circles = np.round(circles[0, :]).astype("int")#
#
# 	# loop over the (x, y) coordinates and radius of the circles
# 	for (x, y, r) in circles:
# 		# draw the circle in the output image, then draw a rectangle
# 		# corresponding to the center of the circle
# 		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
# 		# cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)



# deliver info with CV precision (oh yeah)
npx , npy = int(round(navPoint[0])) , int(round(navPoint[1]))
# calculate
diameter = navBall[2] * 2
OffX =   navPoint[0] - navBall[0]
OffY = -(navPoint[1] - navBall[1])
if abs(OffX) > diameter or abs(OffY) > diameter:
    error(-3)
# check whether point is in front or behind
if all( blueimg[npy][npx] == [0,0,0] ):
    print(0)
else:
    print(1)
print(OffX)
print(OffY)

# show the output after resizing
# image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
# output = cv2.resize(output, (0,0), fx=0.5, fy=0.5)
# cv2.imshow("processed", image)
# cv2.imshow("output", output)
# cv2.waitKey(0)
