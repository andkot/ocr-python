import cv2
import numpy as np

img = cv2.imread('trsh/from_im/page_14.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((5, 5), np.uint8)
kernel2 = np.ones((3, 3), np.uint8)
marker = cv2.dilate(thresh, kernel, iterations=1)
mask = cv2.erode(thresh, kernel, iterations=1)

while True:
    tmp = marker.copy()
    marker = cv2.erode(marker, kernel2)
    marker = cv2.max(mask, marker)
    difference = cv2.subtract(tmp, marker)
    if cv2.countNonZero(difference) == 0:
        break

marker_color = cv2.cvtColor(marker, cv2.COLOR_GRAY2BGR)
out = cv2.bitwise_or(img, marker_color)
cv2.imwrite('out.png', out)
cv2.imshow('result', out)
