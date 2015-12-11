__author__ = 'wlarson'

class Year(object):
    def __init__(self, y, s, e, i, a, d):
        self.year = y
        self.budget = 0
        self.headcount = 0
        self.screen = s
        self.evaluate = e
        self.incubate = i
        self.accelerate = a
        self.develop = d

        self.numScreen = len(self.screen)
        self.numEvaluate = len(self.evaluate)
        self.numIncubate = len(self.incubate)
        self.numAccelerate = len(self.accelerate)
        self.numDevelop = len(self.develop)

        self.activeScreen = 0
        self.activeEvaluate = 0
        self.activeIncubate = 0
        self.activeAccelerate = 0
        self.activeDevelop = 0

        self.newScreen = 0
        self.newEvaluate = 0
        self.newIncubate = 0
        self.newAccelerate = 0
        self.newDevelop = 0
        self.newSuccess = 0

        # Find screen
        i = 0
        while i < self.numScreen:
            self.budget = self.budget + self.screen[i].getBudget()
            self.headcount = self.headcount + self.screen[i].getHeadcount()
            i = i + 1

        # Find evaluate
        i = 0
        while i < self.numEvaluate:
            self.budget = self.budget + self.evaluate[i].getBudget()
            self.headcount = self.headcount + self.evaluate[i].getHeadcount()
            i = i + 1

        # Find incubate
        i = 0
        while i < self.numIncubate:
            self.budget = self.budget + self.incubate[i].getBudget()
            self.headcount = self.headcount + self.incubate[i].getHeadcount()
            i = i + 1

        # Find accelerate
        i = 0
        while i < self.numAccelerate:
            self.budget = self.budget + self.accelerate[i].getBudget()
            self.headcount = self.headcount + self.accelerate[i].getHeadcount()
            i = i + 1

    def getYear(self):
        return self.year

    def getBudget(self):
        return self.budget

    def getHeadcount(self):
        return self.headcount

    def getActiveScreen(self):
        return self.activeScreen

    def getActiveEvaluate(self):
        return self.activeEvaluate

    def getActiveIncubate(self):
        return self.activeIncubate

    def getActiveAccelerate(self):
        return self.activeAccelerate

    def getActiveDevelop(self):
        return self.activeDevelop

    def getNewSuccess(self):
        return self.newSuccess

    def setActiveScreen(self, n):
        self.activeScreen = n

    def setActiveEvaluate(self, n):
        self.activeEvaluate = n

    def setActiveIncubate(self, n):
        self.activeIncubate = n

    def setActiveAccelerate(self, n):
        self.activeAccelerate = n

    def setActiveDevelop(self, n):
        self.activeDevelop = n

    def setNewSuccess(self, n):
        self.newSuccess = n

    def getNewScreen(self):
        return self.newScreen

    def getNewEvaluate(self):
        return self.newEvaluate

    def getNewIncubate(self):
        return self.newIncubate

    def getNewAccelerate(self):
        return self.newAccelerate

    def getNewDevelop(self):
        return self.newDevelop

    def setNewScreen(self, n):
        self.newScreen = n

    def setNewEvaluate(self, n):
        self.newEvaluate = n

    def setNewIncubate(self, n):
        self.newIncubate = n

    def setNewAccelerate(self, n):
        self.newAccelerate = n

    def setNewDevelop(self, n):
        self.newDevelop = n