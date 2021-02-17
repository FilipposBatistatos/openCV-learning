import cv2 as cv

capture = cv.VideoCapture(0) #this refers to camera
#if you want to use a file, provide the path

#this can also be achieved using cv.set
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    frame_resized = rescaleFrame(frame)
    cv.imshow('Small Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()