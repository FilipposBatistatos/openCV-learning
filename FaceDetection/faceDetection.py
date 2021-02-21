#haar cascades are REALLY SENSITIVE to noise, see group two
#to adjust for this we can adjust the minimum naighbours parameter
import cv2 as cv

img = cv.imread('grouptwo.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#importing the classifier to detect faces
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#detecting the faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)