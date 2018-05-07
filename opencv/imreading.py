import cv2
import numpy as np

img = cv2.imread('/home/ray/file/cv/class-activity.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()