import cv2
import numpy as np
import pytesseract
import tesserocr
from src.tesser_api import get_words_info
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

WEGHTS = [0.95]
N = len(WEGHTS)


def alg():
    pass


def make_forcing(syms_list):
    count = len(syms_list)
    res = [0] * count
    input_ = [0.0] * N
    input_.extend(syms_list)
    zero = [0.0] * N
    input_.extend(zero)

    for i in range(count):
        for j in range(N):
            add = (input_[i + N + j + 1] + input_[i + N - j - 1]) * WEGHTS[j]
            res[i] = input_[i + N]*1.1 + add

    return res


def get_words_info_extra(sym_list, img):
    result = []
    i = 0
    for el in sym_list:
        (x_, y_, w_, h_) = el['position']

        black = 0
        for y__ in range(y_, h_):
            for x__ in range(x_, w_):
                if img.item(y__, x__) == 0:
                    black += 1
                # print(img[y__, x__], end='\t')
            # print()

        res_ = black / ((y_ - h_) * (x_ - w_))
        print(f'res = {res_}, x, y = {(x_, y_, w_, h_, (y_ - h_) * (x_ - w_))}, sym = {el["word"]} n = {i}')
        result.append(res_)
        img = cv2.rectangle(img, (x_, y_), (w_, h_), (0, 255, 0), 4)
        i += 1
    return result


def smooth(y, box_pts):
    box = np.ones(box_pts) / box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


img = cv2.imread('page_2.png', cv2.IMREAD_GRAYSCALE)
(thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

h, w = img.shape
boxes = pytesseract.image_to_boxes(img)
res = []
i = 0
# for b in boxes.splitlines():
#     b = b.split(' ')
#     (x_, y_, w_, h_) = (int(b[1]), h - int(b[2]), int(b[3]), h - int(b[4]))
#
#     black = 0
#     for y__ in range(h_, y_):
#         for x__ in range(x_, w_):
#             if img.item(y__, x__) == 0:
#                 black += 1
#             # print(img[y__, x__], end='\t')
#         # print()
#
#     res_ = black / ((h_ - y_) * (x_ - w_))
#     black = 0
#     print(f'res = {res_}, x, y = {(x_, y_, w_, h_, (h_ - y_) * (x_ - w_))}, n = {i}')
#     res.append(res_)
#     img = cv2.rectangle(img, (x_, y_), (w_, h_), (0, 255, 0), 2)
#     i += 1

# mid = int(len(boxes.splitlines()) / 2)
# #
# for i in range(10):
#     print(res[i + 39] / res[i])

sym_list = get_words_info('page_2.png', 'tessdata')
res = get_words_info_extra(sym_list, img)
x_ = range(len(res))

# xnew = np.linspace(x_[0], x_[len(x_) - 1], len(x_))
# spl = make_interp_spline(x_, res, k=3)
# power_smooth = spl(xnew)

res = make_forcing(res)
res = make_forcing(res)
res = make_forcing(res)
res = make_forcing(res)
res = make_forcing(res)
res = make_forcing(res)
res = make_forcing(res)
res = make_forcing(res)
res = make_forcing(res)
res = make_forcing(res)


plt.plot(x_, res)
plt.ylabel('some numbers')
plt.show()

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
