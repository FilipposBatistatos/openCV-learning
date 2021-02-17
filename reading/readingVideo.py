import cv2 as cv

capture = cv.VideoCapture(0) #this refers to camera
#if you want to use a file, provide the path

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()