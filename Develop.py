__author__ = 'wlarson'

import random

class Develop(object):
    def __init__(self, assumptions):
        self.rate = assumptions[0]
        self.time = assumptions[1]

        self.age = 1
        self.success = False
        self.life = self.time
        self.notCounted = True
        self.done = False

        r = random.random()

        if r < self.rate:
            self.success = True

    def grow(self):
        self.age = self.age + 1
        if self.age > self.life:
            self.done = True

    def getSuccess(self):
        return self.success

    def getDone(self):
        return self.done

    def getCounted(self):
        return self.notCounted

    def setCounted(self, c):
        self.notCounted = c