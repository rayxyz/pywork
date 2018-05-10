import cv2 as cv
import numpy as np

tmpt_bgr = cv.imread('/home/ray/file/cvres/tmpt_bgr2.jpg')
tmpt_bgr_gray = cv.cvtColor(tmpt_bgr, cv.COLOR_BGR2GRAY)

tmpt = cv.imread('/home/ray/file/cvres/tmpt02.png', 0)
w, h = tmpt.shape[::-1]

res = cv.matchTemplate(tmpt_bgr_gray, tmpt, cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)


for pt in zip(*loc[::-1]):
    cv.rectangle(tmpt_bgr, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 1)

cv.imshow('detected', tmpt_bgr)

cv.waitKey(0)
cv.destroyAllWindows()


