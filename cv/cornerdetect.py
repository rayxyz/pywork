import cv2 as cv
import numpy as np

img = cv.imread('/home/ray/file/cvres/tmpt_bgr2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)

corners = cv.goodFeaturesToTrack(gray, 500, 0.001, 1)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv.circle(img, (x, y), 3, 255, -1)

cv.imshow('corners', img)
cv.waitKey(0)
cv.destroyAllWindows()