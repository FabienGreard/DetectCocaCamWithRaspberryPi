from os import system
import numpy as np
import cv2

class detectObject(object):
    def __init__(self):
        #init object xml
        #self.object = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.object = cv2.CascadeClassifier('coke.xml')

    def toGray(self, img):
        #init gray filter
        self.img = img
        self.gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    def detectImg(self):
        #find objects
        # face test : objects = self.object.detectMultiScale(self.gray, 1.3, 5)
        old = self.img
        objects = self.object.detectMultiScale(self.gray, 1.3, 5)
        for (x,y,w,h) in objects:
            #cv2.putText(self.img,'Coca',(x-w,y-h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (11,255,255), 2, cv2.LINE_AA)
            cv2.rectangle(self.img, (x,y), (x+w,y+h),(255,0,0),2)

        if(len(objects) != 0):
            print("object found !")


        return self.img

if __name__ == "__main__":
    system("pause")
