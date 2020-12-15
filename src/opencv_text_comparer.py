import cv2
import numpy as np

# ref
"""
for (63, 16, 135, 63)
Mobile (182, 16, 364, 63)
SEPs (415, 17, 543, 63)
for (593, 16, 663, 63)
Mobile (711, 16, 894, 63)
Devices (943, 16, 1146, 63)
set (1195, 24, 1262, 63)
out (1310, 23, 1389, 62)
in (1438, 16, 1483, 62)
this (1533, 16, 1621, 63)
Clause (1669, 17, 1841, 63)
1 (1898, 17, 1908, 62)
("Licensing (1969, 17, 2274, 76)
Framework") (62, 105, 431, 161)
as (462, 119, 510, 151)
the (540, 104, 615, 150)
exclusive (646, 104, 886, 151)
means (917, 119, 1078, 150)
for (1110, 105, 1181, 151)
determining (1210, 104, 1518, 164)
FRAND (1550, 107, 1761, 151)
terms (1793, 113, 1933, 151)
of (1966, 105, 2024, 151)
a (2046, 120, 2072, 151)
license (2104, 105, 2273, 152)
"""

img = np.ones((500, 500, 1), np.uint8) * 255

###
img_ = cv2.imread('page_1.png', cv2.IMREAD_GRAYSCALE)
h, w = img_.shape
rec = (105, 161, 62, 431)
word = img_[105:161, 62:431]

# font
font = cv2.FONT_HERSHEY_SIMPLEX
font_2 = cv2.FONT_HERSHEY_TRIPLEX

# org
org = (50, 50)
org_2 = (50, 100)

# fontScale
fontScale = 1

# Blue color in BGR
color = (0, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.putText() method
img = cv2.putText(img, 'Framework")', org, font, fontScale, color, thickness, cv2.LINE_AA)
img = cv2.putText(img, 'Framework")', org_2, font_2, fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow('image', word)
cv2.waitKey(0)
cv2.destroyAllWindows()
