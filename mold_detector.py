import cv2

import matplotlib.pyplot as plt
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

#Go through each image and detect any circular shapes of the object
image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.cvtColor(image, cv2.CV_HOUGH_GRADIENT, 1.0, 10)
print circles 
if len(circles) != 0:
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
else:
    print("IS NOT MOLD")


cv2.imshow("output", np.hstack([image, output]))
cv2.waitKey(0)
        #if circles is none:
        #
        #else print ("IS MOLD")

#TODO - Detect the circles' color
