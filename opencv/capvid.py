import cv2 as cv
import time
import numpy as np

cap = cv.VideoCapture('/home/ray/file/cv/news.mp4')

while True:
    time.sleep(0.03)
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame)
    cv.imshow('gray', gray)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()