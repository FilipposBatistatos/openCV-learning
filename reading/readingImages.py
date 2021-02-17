#this will allow you to open up an image
#then resize the image to fit in your screen
import cv2 as cv

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('dog-one.jpg')

cv.imshow('Big Dog', img)
cv.imshow('Small Dog', rescaleFrame(img))

cv.waitKey(0)