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

cv2.imshow('HAH', gray)

'''
    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.0, 100)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:

		     cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		     cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        if circles is none:
            print("IS NOT MOLD")
        else print ("IS MOLD")
'''

#TODO - Detect the circles' color
