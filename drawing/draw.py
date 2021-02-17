import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

#1. Paint a certain color
blank[:] = 0,255,0
cv.imshow('Green', blank)
#drawin specific portions of the image
blank[200:300, 300:400] = 0,0,255
cv.imshow('Specific region', blank)

#2. Draw a rectangle
#image, one conrer, other corner, color, thickness
cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=2)
cv.imshow('Rectangle', blank)

#3. Draw a circle
#image, centre, radius, color, thickness
cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
#setting the thickness to -1 will fill the shape
cv.imshow('Circle', blank)

#4. Draw a line
#image, point one, point two, color, thickness
cv.line(blank, (0,0), (300,300), (255,255,255), thickness=4)
cv.imshow('Line', blank)

#5. Write text on image
#image, text, position, font family, fontscale, color, thickness
cv.putText(blank, 'Hello', (255,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)