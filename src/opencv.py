import cv2
import numpy as np
import pytesseract
import tesserocr


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)

    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


img = cv2.imread('page_1.png', cv2.IMREAD_GRAYSCALE)

# h, w, c = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

words = []
image_path = 'page_1.png'
tessdata_path = 'tessdata'
with tesserocr.PyTessBaseAPI(path=tessdata_path, oem=tesserocr.OEM.TESSERACT_LSTM_COMBINED, psm=11) as api:
    api.SetImageFile(image_path)
    level = tesserocr.RIL.WORD
    words = api.GetRegions()
    api.Recognize()
    ri = api.GetIterator()
    while (ri.Next(level)):
        word = ri.GetUTF8Text(level)
        boxes = ri.BoundingBox(level)
        # boxes = ri.
        print(word, "word")
        print(boxes, "coords")

custom_config = r'--oem 3 --psm 6'
details = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, config=custom_config,
                                    lang='eng')

print(details)
print(words)
d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
n_boxes = len(d['level'])
(w, h) = img.shape
print(w, h)
res = []
for i in words:
    rec = i[1]
    (x, y, w, h) = rec['x'], rec['y'], rec['w'], rec['h']
    print(rec)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # black = 0
    # no_black = 0
    # for y_ in range(y, y + h):
    #     for x_ in range(x, x + w):
    #         if img[y_, x_] != black:
    #             no_black += 1
    #         else:
    #             black += 1
    #         # print(img[x_, y_], end='\t')
    #         # print((x_, y_), end=' ')
    #     # print()
    # res_ = black/(w*h)
    # print(f'res = {res_}')
    # res.append(res_)

# print(res[0]/res[1])
# (w,h) = img.shape
# print(w,h)
# for y_ in range(h):
#     for x_ in range(w):
#         print(img[x_, y_], end=' ')
#         # print((x_, y_), end=' ')
#     print()
#
cv2.imshow('img', img)
cv2.waitKey(0)

# (thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# thresh = 127
# im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
# cv2.imwrite('bw_image.png', im_bw)
cv2.destroyAllWindows()
