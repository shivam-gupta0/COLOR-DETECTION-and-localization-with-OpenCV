import cv2
import numpy as np
from numpy import asarray

threshold_val = 500;

path_to_img = "L:\master_thesis\project//trackbar_color_detection\color_wheel.jpg"

img = cv2.imread(path_to_img)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

red = [[0, 193, 31], [0, 255, 255]]
violet_red = [[157, 81, 0], [176, 255, 255]]
violet = [[128, 57, 0], [154, 255, 140]]
blue = [[99, 167, 135],[156, 255, 239]]
green = [[48, 129, 109], [60, 255, 255]]
yellow = [[24, 35, 182], [36, 255, 255]]

lower = np.array(blue[0])
upper = np.array(blue[1])

mask = cv2.inRange(imgHSV, lower, upper)
imageResult = cv2.bitwise_and(img, img, mask=mask)
numpy_data = asarray(imageResult)
count_in1 = np.count_nonzero(numpy_data)
cv2.imshow("Original Image", cv2.resize(img, (0, 0), fx=0.8, fy=0.8))
cv2.imshow("Detected_Color", cv2.resize(imageResult, (0, 0), fx=0.8, fy=0.8))
if count_in1 > threshold_val:
    print("color detected")
cv2.waitKey(0)
