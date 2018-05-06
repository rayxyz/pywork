import cv2
import numpy as np

img = cv2.imread('/home/ray/file/cvres/ol.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (100, 100), (300, 300), (255, 0, 0), 1)
cv2.rectangle(img, (80, 90), (400, 450), (0, 255, 0), 2)
cv2.circle(img, (200, 300), 50, (0, 0, 255), 2)
points = np.array([[100, 300], [250, 300], [400, 500], [560, 600], [400, 600]], np.int32)
cv2.polylines(img, [points], True, (0, 255, 255), 1)

font = cv2.FONT_ITALIC
cv2.putText(img, 'OpenCV nerd!', (300, 200), font, 1, (255, 255, 0), 2, 1)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()