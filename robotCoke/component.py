# Class to for the global value of a component
class RobotComponent(object):
    pin1 = None
    pin2 = None
    position = None

    def __init__(self, board, pin1, pin2=None, position=None):
        self.pin1 = board.get_pin(pin1)
        if pin2 != None:
            self.pin2 = board.get_pin(pin2)
        if position != None:
            self.position = position

# class for the motors actions
class Motor(RobotComponent):

    def forward(self):
        self.pin1.write(1)
        self.pin2.write(0)

    def backward(self):
        self.pin1.write(0)
        self.pin2.write(1)

    def left(self):
        if self.position == "left":
            self.backward()
        elif self.position == "rigth":
            self.forward()

    def rigth(self):
        if self.position == "left":
            self.forward()
        elif self.position == "rigth":
            self.backward()

    def stop(self):
        self.pin1.write(0)
        self.pin2.write(0)

# class for the magnet actions
class Magnet(RobotComponent):

    def on(self):
        print ("Magnet on")
        for i in range(0,50):
            self.pin1.write(1)
            self.pin2.write(1)

    def off(self):
        print ("Magnet off")
        for i in range(0,50):
            self.pin1.write(0)
            self.pin2.write(0)

class Servo(RobotComponent):

    def move(self, value):
        print (value)
        self.pin1.write(value)
