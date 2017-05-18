from os import system
import numpy as np
import cv2
from picamera.array import PiRGBArray
import time
from picamera import PiCamera

class PiCam:
    def __init__(self):
        print('INIT CAMERA')
        # Define the camera resolution and capture
        self.camera = PiCamera(resolution=(640, 480), framerate=30)
        self.rawCapture = PiRGBArray(self.camera, size=(640, 480))

    def start(self):
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            img = frame.array
            cv2.imshow('Frame', img)
            key = cv2.waitKey(1) & 0xFF
            self.rawCapture.truncate(0)
            if key == ord('q'):
                self.stop()
                break
    def stop(self):
        print('STOP CAMERA')
        cv2.destroyAllWindows()

if __name__ == "__main__":
    piCam = PiCam()
    piCam.start()
    system("pause")
