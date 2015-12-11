__author__ = 'wlarson'

import random

class Screen(object):
    def __init__(self, assumptions):
        self.rate = assumptions[0]
        self.time = assumptions[1]
        self.budget = assumptions[2]
        self.headcount = assumptions[3]

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
            self.budget = 0
            self.headcount = 0
            self.done = True

    def getBudget(self):
        return self.budget

    def getHeadcount(self):
        return self.headcount

    def getSuccess(self):
        return self.success

    def getDone(self):
        return self.done

    def getCounted(self):
        return self.notCounted

    def setCounted(self, c):
        self.notCounted = c