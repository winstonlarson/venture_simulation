__author__ = 'wlarson'

import csv
import sys
from Portfolio import Portfolio

class Accelerator(object):
    def __init__(self, sLimit, sAssumptions, eAssumptions, iAssumptions, aAssumptions, dAssumptions):

        # Assumptions
        self.screenLimit = sLimit
        self.screenAssumptions = sAssumptions
        self.evaluateAssumptions = eAssumptions
        self.incubateAssumptions = iAssumptions
        self.accelerateAssumptions = aAssumptions
        self.developAssumptions = dAssumptions

        # set up portfolio
        self.portfolio = Portfolio(self.screenAssumptions, self.evaluateAssumptions, self.incubateAssumptions, self.accelerateAssumptions, self.developAssumptions)
        self.year = 1

        # Totals to report to looper
        self.totalScreen = 0
        self.totalEvaluate = 0
        self.totalIncubate = 0
        self.totalAccelerate = 0
        self.totalDevelop = 0
        self.totalSuccess = 0

        self.totalBudget = 0
        self.peakBudget = 0
        self.peakHeadcount = 0
        self.finalBudget = 0

        # New projects
        self.newScreen = 0
        self.newEvaluate = 0
        self.newIncubate = 0
        self.newAccelerate = 0
        self.newDevelop = 0
        self.newSuccess = 0

        # Add screen projects up to the limit
        k = 1
        while k <= self.screenLimit:
            self.portfolio.addScreen()
            self.totalScreen = self.totalScreen + 1
            self.newScreen = self.newScreen + 1
            k = k + 1

        # Add T1D as an incubate project
        self.portfolio.addIncubate()
        self.totalIncubate = self.totalIncubate + 1
        self.newIncubate = self.newIncubate + 1

        # Record the year's progress for the first year
        self.portfolio.addYear(self.year, self.newScreen, self.newEvaluate, self.newIncubate, self.newAccelerate, self.newDevelop, self.newSuccess)
        self.totalBudget = self.totalBudget + self.portfolio.getAnnualBudget()
        self.peakBudget = self.portfolio.getAnnualBudget()
        self.peakHeadcount = self.portfolio.getAnnualHeadcount()

    def runAccelerator(self):

        # Increase the year
        self.year = self.year + 1

        # Reset the new project counters
        self.newScreen = 0
        self.newEvaluate = 0
        self.newIncubate = 0
        self.newAccelerate = 0
        self.newDevelop = 0

        # Grow existing projects. Let them succeed or fail
        self.portfolio.nextYear()

        # Add new screens
        if self.year <= 2:
            screenAdd = self.screenLimit
        else:
            screenAdd = self.screenAssumptions[4]

        self.newScreen = screenAdd
        while screenAdd > 0:
            self.portfolio.addScreen()
            self.totalScreen = self.totalScreen + 1
            screenAdd = screenAdd - 1

        # Move successful screens to evaluate
        evaluateAdd = self.portfolio.getAnnualScreenSuccesses()
        self.newEvaluate = evaluateAdd
        while evaluateAdd > 0:
            self.portfolio.addEvaluate()
            self.totalEvaluate = self.totalEvaluate + 1
            evaluateAdd = evaluateAdd - 1

        # Move successful evaluate to incubate
        incubateAdd = self.portfolio.getAnnualEvaluateSuccesses()
        self.newIncubate = incubateAdd
        while incubateAdd > 0:
            self.portfolio.addIncubate()
            self.totalIncubate = self.totalIncubate + 1
            incubateAdd = incubateAdd - 1

        # Move successful incubate to accelerate
        accelerateAdd = self.portfolio.getAnnualIncubateSuccesses()
        self.newAccelerate = accelerateAdd
        while accelerateAdd > 0:
            self.portfolio.addAccelerate()
            self.totalAccelerate = self.totalAccelerate + 1
            accelerateAdd = accelerateAdd - 1

        # Move successful accelerate to develop
        developAdd = self.portfolio.getAnnualAccelerateSuccesses()
        self.newDevelop = developAdd
        while developAdd > 0:
            self.portfolio.addDevelop()
            self.totalDevelop = self.totalDevelop + 1
            developAdd = developAdd - 1

        # Find number of successes that year
        self.newSuccess = self.portfolio.getAnnualDevelopSuccesses()
        self.totalSuccess = self.totalSuccess + self.portfolio.getAnnualDevelopSuccesses()

        # Record this year's progress
        self.portfolio.addYear(self.year, self.newScreen, self.newEvaluate, self.newIncubate, self.newAccelerate, self.newDevelop, self.newSuccess)

        # Add totals
        self.totalBudget = self.totalBudget + self.portfolio.getAnnualBudget()
        if self.portfolio.getAnnualBudget() > self.peakBudget:
            self.peakBudget = self.portfolio.getAnnualBudget()
        if self.portfolio.getAnnualHeadcount() > self.peakHeadcount:
            self.peakHeadcount = self.portfolio.getAnnualHeadcount()
        if self.year == 16:
            self.finalBudget = self.portfolio.getAnnualBudget()

    def getFinalBudget(self):
        return self.finalBudget

    def getTotalBudget(self):
        return self.totalBudget

    def getPeakBudget(self):
        return self.peakBudget

    def getPeakHeadcount(self):
        return self.peakHeadcount

    def getTotalSuccess(self):
        return self.totalSuccess

    def getTotalDevelop(self):
        return self.totalDevelop

    def getTotalAccelerate(self):
        return self.totalAccelerate

    def getTotalIncubate(self):
        return self.totalIncubate

    def getTotalEvaluate(self):
        return self.totalEvaluate

    def getTotalScreen(self):
        return self.totalScreen

    def writeModel(self):
        if sys.version_info >= (3,0,0):
            self.outfile = open('output.csv', 'w', newline='')
            self.csvout = csv.writer(self.outfile)
        else:
            self.outfile = open("output.csv", "wb")
            self.csvout = csv.writer(self.outfile)

        data = ["Year","Screen","Evaluate","Incubate","Accelerate","Develop","Success","Total Budget","Total Headcount"]
        self.csvout.writerow(data)
        self.portfolio.printModel(self.csvout, self.outfile)