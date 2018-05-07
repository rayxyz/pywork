import cv2 as cv
import numpy as np
import time

face_cascade = cv.CascadeClassifier('/home/ray/softs/opencv-3.4.1/data/haarcascades/haarcascade_frontalface_default.xml')
# img = cv.imread('/home/ray/file/cv/class-activity.jpg')

# cap = cv.VideoCapture('/home/ray/file/cv/news.mp4')
cap = cv.VideoCapture('/home/ray/file/cv/mv.mp4')

while True:
    time.sleep(0.005)
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv.imshow('face', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.waitKey(0)
cv.destroyAllWindows()