from os import system

from robotCoke import *
from factory import robocorp

import time

class Make:
    def __init__(self):
        print("i do robot")
        camera = Camera();
        robot = Robot(camera)
        setRobot(robot)

        robot.movement("left")
        time.sleep(3)
        robot.movement("rigth")
        time.sleep(3)
        robot.movement("stop")

        robot.magnet.on()
        time.sleep(5)
        robot.magnet.off()

        robot.moveServo(0, 175)
        time.sleep(3)
        robot.moveServo(0, 0)
        time.sleep(3)

    def setRobot(robot):
        #motor top left (motor 1)
        motor_pin1 = 'd:4:o'
        motor_pin2 = 'd:5:o'
        motor_position = 'left'
        robot.addMotor(motor_pin1, motor_pin2, motor_position)

        #motor top rigth (motor 2)
        motor_pin1 = 'd:6:o'
        motor_pin2 = 'd:7:o'
        motor_position = 'left'
        robot.addMotor(motor_pin1, motor_pin2, motor_position)

        #motor bottom left (motor 3)
        motor_pin1 = 'd:8:o'
        motor_pin2 = 'd:9:o'
        motoro_position = 'left'
        robot.addMotor(motor_pin1, motor_pin2, motor_position)

        #motor bottom rigth (motor 4)
        motor_pin1 = 'd:10:o'
        motor_pin2 = 'd:11:o'
        motor_position = 'left'
        robot.addMotor(motor_pin1, motor_pin2, motor_position)

        #magnet
        magnet_pin1 = 'd:12:o'
        magnet_pin2 = 'd:13:o'
        robot.setMagnet(magnet_pin1, magnet_pin2)

        #servo-motor 1
        servo_pin = 'd:2:s'
        robot.addServo(servo_pin)

        #servor-motor 2
        servo_pin = 'd:3:s'
        robot.addServo(servo_pin)

if __name__ == "__main__":
    Make()
    system("pause")
