import cv2 as cv
import time
import numpy as np

cap = cv.VideoCapture('/home/ray/file/cvres/girl.mp4')
# fourcc = cv.cv.CV_FOURCC(*'XVID')
# fourcc = cv.cv.CV_FOURCC(*'H264')
# output = cv.VideoWriter('output.avi', fourcc, 20, (640, 480), True)

while True:
    time.sleep(0.008)
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # output.write(frame)
    cv.imshow('frame', frame)
    # cv.imshow('gray', gray)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# output.release()
cv.destroyAllWindows()