import cv2
import numpy as np

path_to_img = "L:\master_thesis\project//trackbar_color_detection\color_wheel.jpg"
img = cv2.imread(path_to_img)


def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 166, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 56, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imageResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Original", cv2.resize(img, (0, 0), fx=0.5, fy=0.5))
    cv2.imshow("Mask", cv2.resize(mask, (0, 0), fx=0.5, fy=0.5))
    cv2.imshow("final", cv2.resize(imageResult, (0, 0), fx=0.5, fy=0.5))
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        print(h_min, h_max, s_min, s_max, v_min, v_max)
        cv2.destroyAllWindows()
        break
