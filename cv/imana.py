import cv2 as cv

img = cv.imread('/home/ray/file/cvres/ol.jpg', cv.IMREAD_COLOR)
px = img[50, 60]

print(px)

img[50, 60] = [0, 0, 255]

img[300:400, 300:400] = [255, 255, 0]

roi = img[45:100, 200:400]

img[0:55, 0:200] = roi

cv.imshow('image', img)

print(px)


cv.waitKey(0)
cv.destroyAllWindows()