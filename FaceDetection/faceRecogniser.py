import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

people = []
DIR = r'C:\Users\filip\Documents\Repositories\openCV-python\FaceDetection\office'

for i in os.listdir(DIR):
    people.append(i)

img = cv.imread('validation/michael.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Who\' it gonna be?!', gray)

# detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected face', img)

cv.waitKey(0)

