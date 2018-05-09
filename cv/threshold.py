import cv2 as cv

img = cv.imread('/home/ray/file/cvres/ol.jpg')

retval, threshold = cv.threshold(img, 3, 255, cv.THRESH_BINARY)

grayed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
retval2, threshold2 = cv.threshold(grayed, 3, 255, cv.THRESH_BINARY)

gaus = cv.adaptiveThreshold(grayed, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)

cv.imshow('original', img)
cv.imshow('threshold', threshold)
cv.imshow('threshold2', threshold2)
cv.imshow('gaus', gaus)

cv.waitKey(0)
cv.destroyAllWindows()