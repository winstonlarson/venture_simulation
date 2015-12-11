__author__ = 'wlarson'

from Accelerator import Accelerator

class Looper(object):
    def __init__(self, sLimit, lLimit, g2030, sAssumptions, eAssumptions, iAssumptions, aAssumptions, dAssumptions):

        # Controlling loops and accelerators
        self.screenLimit = sLimit
        self.loopLimit = lLimit
        self.goal2030 = g2030

        # Assumptions to pass
        self.screenAssumptions = sAssumptions
        self.evaluateAssumptions = eAssumptions
        self.incubateAssumptions = iAssumptions
        self.accelerateAssumptions = aAssumptions
        self.developAssumptions = dAssumptions

        # Totals and averages
        self.totalSuccesses = 0
        self.averageSuccesses = 0
        self.totalScreen = 0
        self.averageScreen = 0
        self.totalEvaluate = 0
        self.averageEvaluate = 0
        self.totalIncubate = 0
        self.averageIncubate = 0
        self.totalAccelerate = 0
        self.averageAccelerate = 0
        self.totalDevelop = 0
        self.averageDevelop = 0

        self.totalBudget = 0
        self.averageBudget = 0
        self.totalPeakBudget = 0
        self.averagePeakbudget = 0
        self.totalPeakHeadcount = 0
        self.averagePeakHeadcount = 0

        # Printing one
        self.goal = 0
        self.written = False

    def runLoop(self):
        n = self.loopLimit

        # Run a single Accelerator model, through N loops
        while n > 0:
            acc = Accelerator(self.screenLimit, self.screenAssumptions, self.evaluateAssumptions, self.incubateAssumptions, self.accelerateAssumptions, self.developAssumptions)

            # Run Accelerator for 16 years
            c = 15
            while c > 0:
                acc.runAccelerator()
                c = c - 1

            # Update loop running totals (to calculate averages later)
            self.totalSuccesses = self.totalSuccesses + acc.getTotalSuccess()
            self.totalScreen = self.totalScreen + acc.getTotalScreen()
            self.totalEvaluate = self.totalEvaluate + acc.getTotalEvaluate()
            self.totalIncubate = self.totalIncubate + acc.getTotalIncubate()
            self.totalAccelerate = self.totalAccelerate + acc.getTotalAccelerate()
            self.totalDevelop = self.totalDevelop + acc.getTotalDevelop()

            self.totalBudget = self.totalBudget + acc.getTotalBudget()
            self.totalPeakBudget = self.totalPeakBudget + acc.getPeakBudget()
            self.totalPeakHeadcount = self.totalPeakHeadcount + acc.getPeakHeadcount()

            if acc.getTotalSuccess() > self.goal2030:
                self.goal = self.goal + 1

            # Print a model accelerator out to CSV
            if acc.getTotalSuccess() == 2 and not self.written and acc.getFinalBudget() > 0:
                acc.writeModel()
                self.written = True

            n = n - 1

    def getAverageSuccesses(self):
        self.averageSuccesses = self.totalSuccesses / self.loopLimit
        return self.averageSuccesses

    def getAverageScreen(self):
        self.averageScreen = self.totalScreen / self.loopLimit
        return self.averageScreen

    def getAverageEvaluate(self):
        self.averageEvaluate = self.totalEvaluate / self.loopLimit
        return self.averageEvaluate

    def getAverageIncubate(self):
        self.averageIncubate = self.totalIncubate / self.loopLimit
        return self.averageIncubate

    def getAverageAccelerate(self):
        self.averageAccelerate = self.totalAccelerate / self.loopLimit
        return self.averageAccelerate

    def getAverageDevelop(self):
        self.averageDevelop = self.totalDevelop / self.loopLimit
        return self.averageDevelop

    def getAverageBudget(self):
        self.averageBudget = self.totalBudget / self.loopLimit
        return self.averageBudget

    def getPeakBudget(self):
        self.averagePeakbudget = self.totalPeakBudget / self.loopLimit
        return self.averagePeakbudget

    def getPeakHeadcount(self):
        self.averagePeakHeadcount = self.totalPeakHeadcount / self.loopLimit
        return self.averagePeakHeadcount

    def getProbability(self):
        return self.goal / self.loopLimit