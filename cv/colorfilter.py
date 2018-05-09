import cv2 as cv
import numpy as np

cap = cv.VideoCapture('/home/ray/file/cvres/girl.mp4')

while True:
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red = np.array([100, 100, 200])
    upper_red = np.array([255, 255, 255])

    mask = cv.inRange(hsv, lower_red, upper_red)
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    # cv.imshow('mask', mask)
    cv.imshow('res', res)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.waitKey(0)
cv.destroyAllWindows()
cap.release()
