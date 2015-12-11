# venture_simulation
Monte Carlo simulation of a venture portfolio

Portfolios of venture-based companies are inherently fraught with risk. As part of a project to build a strategy for managing a portfolio of high-risk biotech ventures, I created a Monte Carlo simulation of the portfolio. My simulation accepted basic assumptions about the expected life-span of ventures, their chances of success, and their expected costs. Based on a desired number of successful ventures over 10 years, we used the simulation to estimate:

* The number of deals the portfolio managers would need to do
* The approximate number of ventures they would be managing at a given time
* The expected amount of investment needed
* The approximate headcount in the portfolio at a given time
* My simulation helped to inform the portfolio managers in creating their strategy and setting expectations around the output of the portfolio.

A [full write-up](http://winstonlarson.github.io/venture-simulation) is available in [my portfolio](http://winstonlarson.github.io).

The whole simulation is run from `model.py`. You can change assumptions in that file. It generates a Looper object, which simulates thousands of Accelerator objects. Accelerators contain Portfolios, which keep track of projects in different stages (i.e. screen, evaluate, develop, accelerate) of a venture portfolio. Accelerators loop over Years, and each year projects grow, succeeding or failing. Each year and project has an expected budget and headcount.
