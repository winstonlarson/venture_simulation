__author__ = 'wlarson'

from Screen import Screen
from Evaluate import Evaluate
from Incubate import Incubate
from Accelerate import Accelerate
from Develop import Develop
from Year import Year

class Portfolio(object):
    def __init__(self, sAssumptions, eAssumptions, iAssumptions, aAssumptions, dAssumptions):

        self.screenAssumptions = sAssumptions
        self.evaluateAssumptions = eAssumptions
        self.incubateAssumptions = iAssumptions
        self.accelerateAssumptions = aAssumptions
        self.developAssumptions = dAssumptions

        self.screen = []
        self.evaluate = []
        self.incubate = []
        self.accelerate = []
        self.develop = []

        self.years = []
        self.activeScreen = 0
        self.activeEvaluate = 0
        self.activeIncubate = 0
        self.activeAccelerate = 0
        self.activeDevelop = 0

        self.screenYearSuccess = 0
        self.evaluateYearSuccess = 0
        self.incubateYearSuccess = 0
        self.accelerateYearSuccess = 0
        self.developYearSuccess = 0

    def addScreen(self):
        s = Screen(self.screenAssumptions)
        self.screen.append(s)
        self.activeScreen = self.activeScreen + 1

    def addEvaluate(self):
        e = Evaluate(self.evaluateAssumptions)
        self.evaluate.append(e)
        self.activeEvaluate = self.activeEvaluate + 1

    def addIncubate(self):
        i = Incubate(self.incubateAssumptions)
        self.incubate.append(i)
        self.activeIncubate = self.activeIncubate + 1

    def addAccelerate(self):
        a = Accelerate(self.accelerateAssumptions)
        self.accelerate.append(a)
        self.activeAccelerate = self.activeAccelerate + 1

    def addDevelop(self):
        d = Develop(self.developAssumptions)
        self.develop.append(d)
        self.activeDevelop = self.activeDevelop + 1

    def nextYear(self):
        # Grow and count screen
        i = 0
        self.activeScreen = 0
        self.screenYearSuccess = 0
        while i < len(self.screen):
            self.screen[i].grow()
            if self.screen[i].getDone():
                if self.screen[i].getCounted():
                    self.screen[i].setCounted(False)
                    if self.screen[i].getSuccess():
                        self.screenYearSuccess = self.screenYearSuccess + 1
            else:
                self.activeScreen = self.activeScreen + 1
            i = i + 1

        # Grow and count evaluate
        i = 0
        self.activeEvaluate = 0
        self.evaluateYearSuccess = 0
        while i < len(self.evaluate):
            self.evaluate[i].grow()
            if self.evaluate[i].getDone():
                if self.evaluate[i].getCounted():
                    self.evaluate[i].setCounted(False)
                    if self.evaluate[i].getSuccess():
                        self.evaluateYearSuccess = self.evaluateYearSuccess + 1
            else:
                self.activeEvaluate = self.activeEvaluate + 1
            i = i + 1

        # Grow and count incubate
        i = 0
        self.activeIncubate = 0
        self.incubateYearSuccess = 0
        while i < len(self.incubate):
            self.incubate[i].grow()
            if self.incubate[i].getDone():
                if self.incubate[i].getCounted():
                    self.incubate[i].setCounted(False)
                    if self.incubate[i].getSuccess():
                        self.incubateYearSuccess = self.incubateYearSuccess + 1
            else:
                self.activeIncubate = self.activeIncubate + 1
            i = i + 1

        # Grow and count accelerate
        i = 0
        self.activeAccelerate = 0
        self.accelerateYearSuccess = 0
        while i < len(self.accelerate):
            self.accelerate[i].grow()
            if self.accelerate[i].getDone():
                if self.accelerate[i].getCounted():
                    self.accelerate[i].setCounted(False)
                    if self.accelerate[i].getSuccess():
                        self.accelerateYearSuccess = self.accelerateYearSuccess + 1
            else:
                self.activeAccelerate = self.activeAccelerate + 1
            i = i + 1

        # Grow and count develop
        i = 0
        self.activeDevelop= 0
        self.developYearSuccess = 0
        while i < len(self.develop):
            self.develop[i].grow()
            if self.develop[i].getDone():
                if self.develop[i].getCounted():
                    self.develop[i].setCounted(False)
                    if self.develop[i].getSuccess():
                        self.developYearSuccess = self.developYearSuccess + 1
            else:
                self.activeDevelop = self.activeDevelop + 1
            i = i + 1

    def addYear(self, y, ns, ne, ni, na, nd, nsuc):
        newyear = Year(y, self.screen, self.evaluate, self.incubate, self.accelerate, self.develop)
        newyear.setActiveScreen(self.activeScreen)
        newyear.setActiveEvaluate(self.activeEvaluate)
        newyear.setActiveIncubate(self.activeIncubate)
        newyear.setActiveAccelerate(self.activeAccelerate)
        newyear.setActiveDevelop(self.activeDevelop)
        newyear.setNewScreen(ns)
        newyear.setNewEvaluate(ne)
        newyear.setNewIncubate(ni)
        newyear.setNewAccelerate(na)
        newyear.setNewDevelop(nd)
        newyear.setNewSuccess(nsuc)
        self.years.append(newyear)

    def printModel(self, csvout, fileout):
        b = 0
        while b <= 15:
            s = self.years[b].getYear() + 2014
            data = [s,self.years[b].getActiveScreen(),self.years[b].getActiveEvaluate(),self.years[b].getActiveIncubate(),self.years[b].getActiveAccelerate(),self.years[b].getActiveDevelop(),self.years[b].getNewSuccess(), self.years[b].getBudget(), self.years[b].getHeadcount()]
            csvout.writerow(data)
            b = b + 1

        fileout.close()

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

    def getAnnualScreenSuccesses(self):
        return self.screenYearSuccess

    def getAnnualEvaluateSuccesses(self):
        return self.evaluateYearSuccess

    def getAnnualIncubateSuccesses(self):
        return self.incubateYearSuccess

    def getAnnualAccelerateSuccesses(self):
        return self.accelerateYearSuccess

    def getAnnualDevelopSuccesses(self):
        return self.developYearSuccess

    def getAnnualBudget(self):
        last = len(self.years)
        last = last - 1
        return self.years[last].getBudget()

    def getAnnualHeadcount(self):
        last = len(self.years)
        last = last - 1
        return self.years[last].getHeadcount()

