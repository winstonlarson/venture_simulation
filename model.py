#__author__ = 'wlarson'

import time
from Looper import Looper

# Success assmption
goal2030 = 3

# Screen assumptions
screenRate = 0.5
screenTime = 1
screenCost = 0.1
screenHeadcount = 0
screenYearly = 5
screenAssumptions = [screenRate, screenTime, screenCost, screenHeadcount, screenYearly]

# Evaluate assumptions
evaluateRate = 0.75
evaluateTime = 1
evaluateCost = 1
evaluateHeadcount = 0.33
evaluateAssumptions = [evaluateRate, evaluateTime, evaluateCost, evaluateHeadcount]

# Incubate assumptions
incubateRate = 0.75
incubateTime = 3
incubateCost = 5
incubateHeadcount = 3
incubateAssumptions = [incubateRate, incubateTime, incubateCost, incubateHeadcount]

# Accelerate assumptions
accelerateRate = 0.25
accelerateTime = 4
accelerateCost = 10
accelerateHeadcount = 5
accelerateGrowth = 0.25
accelerateAssumptions = [accelerateRate, accelerateTime, accelerateCost, accelerateHeadcount, accelerateGrowth]

# Develop assumptions
developRate = 0.65
developTime = 5
developAssumptions = [developRate, developTime]

t0= time.time()

screenLimit = 40
loopLimit = 1000

loop = Looper(screenLimit, loopLimit, goal2030, screenAssumptions, evaluateAssumptions, incubateAssumptions, accelerateAssumptions, developAssumptions)

loop.runLoop()

print("Successes: " + str(loop.getAverageSuccesses()))
print("Screen: " + str(loop.getAverageScreen()))
print("Evaluate: " + str(loop.getAverageEvaluate()))
print("Incubate: " + str(loop.getAverageIncubate()))
print("Accelerate: " + str(loop.getAverageAccelerate()))
print("Develop: " + str(loop.getAverageDevelop()))
print("Total budget: " + str(loop.getAverageBudget()))
print("Peak budget: " + str(loop.getPeakBudget()))
print("Peak headcount: " + str(loop.getPeakHeadcount()))
print("Probability of succeeding: " + str(loop.getProbability()))

t1 = time.time() - t0