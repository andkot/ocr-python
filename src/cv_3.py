import cv2
import numpy as np

img = cv2.imread('trsh/from_im/page_13.png', cv2.IMREAD_GRAYSCALE)

# blur = cv2.medianBlur(img, 15)
# ret, blur = cv2.threshold(img, 250, 255, cv2.THRESH_TOZERO)

kernel = np.ones((4, 4), np.uint8)
kernel__2 = np.ones((6, 6), np.uint8)
kernel_2 = np.ones((2, 2), np.uint8)

img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel__2)
# img = cv2.dilate(img, kernel_2, iterations=1)

img = (255 - img)
# img = cv2.dilate(img, kernel, iterations=1)
img = cv2.distanceTransform(img, cv2.DIST_L2, 0)
# img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel_2)
# img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel_2)

img = (255 - img)
# img = cv2.erode(img, kernel, iterations=1)
# img = cv2.dilate(img, kernel_2, iterations=10)

# img = cv2.erode(img, kernel, iterations=10)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

r, img = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY)

img = cv2.erode(img, kernel_2, iterations=50)
img = np.uint8(img)
# img.convertTo(img, cv2.CV_16U)
# nb_components, img, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
# img = (255 - img)
# img = cv2.erode(img, kernel_2, iterations=11)
# # nb_components, img, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
# img = (255 - img)

# Filter using contour area and remove small noise
thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
img = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = img[0] if len(img) == 2 else img[1]
for c in img:
    area = cv2.contourArea(c)
    if area < 6000:
        cv2.drawContours(thresh, [c], -1, (0, 0, 0), -1)

# img = cv2.erode(img, kernel_2, iterations=30)
thresh = (255 - thresh)

# img, contours = cv2.findContours(img, 1, 2)

# res = np.nonzero(img)
# print(img[res[0][len(res[0])-1]][res[1][len(res[1])-1]])

cv2.imwrite('cv_im.png', thresh)
