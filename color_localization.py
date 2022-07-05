import cv2
import numpy as np


font = cv2.FONT_HERSHEY_PLAIN

im = cv2.imread("E:\project\\vehicle_dataset\\toy_car_imgs//5.jpg")
imgHSV = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
red = [[0, 86, 56], [255, 196, 178]]

lower = np.array(red[0])
upper = np.array(red[1])

mask = cv2.inRange(imgHSV, lower, upper)
bluecnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

if len(bluecnts) > 0:
    blue_area = max(bluecnts, key=cv2.contourArea)
    (xg, yg, wg, hg) = cv2.boundingRect(blue_area)
    cv2.rectangle(im, (xg, yg), (xg + wg, yg + hg), (0, 255, 0), 2)
    cv2.putText(im, "car", (xg, yg), font, 20, (255, 255, 0), 3)

#cv2.imshow("original",im)
#cv2.imshow("mask",mask)
cv2.imshow('frame', cv2.resize(im, (0, 0), fx=0.3, fy=0.3))
cv2.imshow('mask', cv2.resize(mask, (0, 0), fx=0.3, fy=0.3))

k = cv2.waitKey(0)

cv2.destroyAllWindows()
