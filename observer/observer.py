from os import system
import weakref

class Robot(object):
    #observer class
    def __init__(self, subject):
        print(subject.__class__.__name__, 'is now °-° from', self.__class__.__name__)
        self.subject = subject
        self.subject.addObserver(self)

    def notify(self, old, new, subject):
        print('foo changed from %s to %s' % (old, new), 'from' , subject.__class__.__name__)

class Observer(object):
    #test observable !!must be move to engine and sight!!
    def __init__(self, value):
        self.value = value
        self.observers = weakref.WeakKeyDictionary()

    def set(self, value):
        old = self.value
        self.value = value
        self.notifyObservers(old, self.value)

    def get(self):
        return self.value

    def addObserver(self, o):
        self.observers[o] = 1

    def removeObserver(self, o):
        del self.observers[o]

    def notifyObservers(self, old, new):
        for o in self.observers:
            o.notify(old, new, self)

if __name__ == "__main__":
    subj = Observable(23)
    obs = Observer(subj)

    subj.set(50);
    print (subj.get())
    subj.removeObserver(obs)
    subj.set(55);

    system("pause");
