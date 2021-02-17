import cv2 as cv

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('dog-one.jpg'))

# Converting an image to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Small Dog',gray)

# Blurring the image
#by increasing the kernel size (3,3) you increase the blur, it must be odd
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image, opposite of eroding
dilated = cv.dilate(canny, (3,3), iterations=5)
cv.imshow('Dilated', dilated)

# Eroding the image, opposite of Dilating
eroded = cv.erode(dilated, (3,3), iterations=5)
cv.imshow('Eroded', eroded)

# Resize - without a custom function
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
#other interpolations for expanding include:
#cv.INTER_LINEAR and cv.INTER_CUBIC
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)