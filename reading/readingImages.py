#this will allow you to open up an image
#then resize the image to fit in your screen
import cv2 as cv

img = cv.imread('dog-one.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)