from __future__ import generators
from os import system
import random


class RoboCorp(object):
    #factory class
    def factory(part):
        #check type
        if part.__name__ == 'Engine' : return part()
        if part.__name__ == 'Sight' : return part()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)

# Generate shape name issue:
def RoboCorpGen(n):
    parts = RoboCorp.__subclasses__()
    for i in range(n):
        yield random.choice(parts)

def RoboCorpGenErr(n):
    errs = RoboCorp.__subclasses__().errs
    for i in range(n):
        yield random.choice(errs)

# Return fake signature
def signature():
    return 'R0B0Tx' + ''.join(random.choice('0123456789ABCDEF') for i in range(16))

if __name__ == "__main__":
    parts = (RoboCorp.factory(i) for i in RoboCorpGen(1))
    for part in parts:
        part.create(signature());
    system("pause");
