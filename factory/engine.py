from os import system
from robocorp import *

#DC settings
class Engine(RoboCorp):
    def create(self, _id):
        print(_id, ' : ', self.__class__.__name__)

if __name__ == "__main__":
    parts = (RoboCorp.factory(i) for i in RoboCorpGen(1))
    for part in parts:
        part.create(signature());
    system("pause");
