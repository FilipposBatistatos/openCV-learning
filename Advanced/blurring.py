import cv2 as cv

img = cv.imread('dog-two.jpg')

# Averaging
#image, kernel
average = cv.blur(img, (3,3)) #the higher the kernel size the more intense the blur
cv.imshow('Average', average)

# Gaussian
#image, kernel
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gaussian)

# Median
#more effective in removing large amounts of noise
median = cv.medianBlur(img, 3)
cv.imshow('Median', median) 

#Bilateral
#similar to median blur but it retains edges
#image, kernel in 1D form, sigma spacing, 
bilateral = cv.bilateralFilter(img, 10, 35, 25)#
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)