import cv2 as cv

im1 = cv.imread('/home/ray/file/cvres/cry.png', cv.IMREAD_COLOR)
im2 = cv.imread('/home/ray/file/cvres/ol.jpg', cv.IMREAD_COLOR)

# imadd = im1 + im1
# imadd = cv.add(im2, im2)

weighted = cv.addWeighted(im2, 0.2, im2, 0.1, 0)

cv.imshow('weighted', weighted)

cv.waitKey(0)
cv.destroyAllWindows()