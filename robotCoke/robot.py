import os
import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
from detectObject import *
import weakref
import pyfirmata
from component import *

class Robot(object):
    #observer class
    port = '/dev/ttyACM0'
    #port = 'COM5'
    board = pyfirmata.Arduino(port)

    motors = []
    servo = []
    magnet = None

    def __init__(self, subject):
        print(subject.__class__.__name__, 'is now °-° from', self.__class__.__name__)
        self.subject = subject
        self.subject.addObserver(self)

    def notify(self, value, subject):
        print(' %s' % (value), 'from' , subject.__class__.__name__)
        if(value == 'on'):
            self.magnet.on()
            self.servo.move(180)
        else:
            self.magnet.off()
            self.servo.move(10) 


    def addMotor(self, pin1, pin2, position):
        self.motors.append(Motor(self.board, pin1, pin2, position))
        print ("Motor added")

    def addServo(self, pin1):
        self.servo.append(Servo(self.board, pin1))

    def setMagnet(self, pin1, pin2):
        self.magnet = Magnet(self.board, pin1, pin2)
        print("Magnet set")

    def movement(self, direction):
        for m in self.motors:
            print ("Motor : " + str(m.pin1) + " --- " + str(m.pin2) + " --- direction :" + direction)
            for i in range (0,50):
                if direction == "forward" : m.forward()
                elif direction == "backward" : m.backward()
                elif direction == "left" : m.left()
                elif direction == "rigth" : m.rigth()
                elif direction == "stop" : m.stop()
                else : print ("ERROR : Wrong movement")

    def moveServo(self, servo_number, value):
        print ("Servo move to position : " + str(value))
        for i in range (0,50):
            self.servo[servo_number].move(value)

class PiCam:
    def __init__(self):
        print('INIT CAMERA')
        # Define the camera resolution and capture
        self.camera = PiCamera(resolution=(640, 480), framerate=30)
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))

        # Init object detection
        self.detect = detectObject()

    def start(self):
        print('START CAMERA')
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            # img to gray
            self.detect.toGray(frame.array)

            cv2.imshow('Frame-Detect', self.detect.detectImg())

            key = cv2.waitKey(1) & 0xFF
            self.rawCapture.truncate(0)
            if key == ord('q'):
                self.stop()
                break

    def stop(self):
        print('STOP CAMERA')
        cv2.destroyAllWindows()
        os._exit(0)

class detectObject(object):
    def __init__(self):
        #init object xml
        #self.object = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.object = cv2.CascadeClassifier('coke.xml')
        self.observers = weakref.WeakKeyDictionary()

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
            notifyObservers('on')
        else:
            notifyObservers('off')

        return self.img

    def addObserver(self, o):
        self.observers[o] = 1

    def removeObserver(self, o):
        del self.observers[o]

    def notifyObservers(self, value):
        for o in self.observers:
            o.notify(value, self)

if __name__ == "__main__":
    piCam = PiCam()
    piCam.start()
    os.system("pause")
