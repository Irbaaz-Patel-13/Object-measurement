'''import cv2
import numpy as np
import utilities
from AppKit import NSApplicationDelegate

class AppDelegate(NSApplicationDelegate):
    def applicationSupportsSecureRestorableState_(self, app):
        return True

webcam = False
path = 'IMG_7944.JPG'
cap = cv2.VideoCapture(0)
cap.set(10,160) ##brightness parameter 10 and value 160
cap.set(3,1920) #widght parameter 3 and value 1920
cap.set(4,1080) #height parameter 4 and value 1080
scale = 3
wP = 160*scale
hP = 244*scale


while True:
    if webcam:success,img = cap.read()
    else: img = cv2.imread(path)
    img,finalCountours = utilities.getContours(img,minArea=50000,filter=4)
    if len(finalCountours) != 0:
        biggest = finalCountours[0][2]
        #print(biggest)
        imgWarp = utilities.warpImg(img, biggest, wP, hP)
        cv2.imshow('paper', imgWarp)

    img = cv2.resize(img,(0,0),None,0.5,0.5)
    cv2.imshow('Original',img)
    cv2.waitKey(1)'''