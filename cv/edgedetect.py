import cv2 as cv

cap = cv.VideoCapture('/home/ray/file/cvres/girl.mp4')

while True:
    ret, frame = cap.read()

    laplacian = cv.Laplacian(frame, cv.CV_64F)
    edges = cv.Canny(frame, 100, 200)

    cv.imshow('frame', frame)
    # cv.imshow('laplacian', laplacian)
    cv.imshow('edges', edges)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()