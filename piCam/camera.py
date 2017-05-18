from os import system
import numpy as np
import cv2
from picamera.array import PiRGBArray
import time
from picamera import PiCamera

class PiCam:
    def __init__(self):
        # Define the camera resolution and capture
        camera = PiCamera(resolution=(640, 480), framerate=30)
        rawCapture = PiRGBArray(camera, size=(640, 480))
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    def start(self):
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            img = frame.array
            cv2.flip(img, 0)
            out.write(img)

            cv2.imshow('Frame', img)
            key = cv2.waitKey(1) & 0xFF
            rawCapture.truncate(0)
            if key == ord('q'):
                stop()
    def stop(self):
        print('DONE')
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    PiCam = Picam()
    Picam.start
    system("pause")
