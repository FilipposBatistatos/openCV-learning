import cv2 as cv
#import matplotlib.pyplot as plt

img = cv.imread('dog-two.jpg')
cv.imshow('Dog', img)

#since open cv works in BGR using libraries
#that work in RGB will result in inverted colors
# plt.imshow(img)
# plt.show()

#BGR ro Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#HSV to BGR
#these work the other way around too!
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

cv.waitKey(0)