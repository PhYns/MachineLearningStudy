import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 1000
CURRENTFOXPOP = 50


def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    
    prob = 1 - (CURRENTRABBITPOP/MAXRABBITPOP)
    
    if random.random() < prob:
        CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    
    prob = float(CURRENTRABBITPOP/MAXRABBITPOP)
    
    if random.random() <= prob and CURRENTRABBITPOP > 10:
        CURRENTRABBITPOP -= 1
        if random.random() >= float(1/3):
            CURRENTFOXPOP += 1
    elif random.random() < float(1/10) and CURRENTFOXPOP > 10:
        CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations, fox_populations = list(), list()
    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    
    return (rabbit_populations, fox_populations)


# Ploting
rabbits, foxes = runSimulation(200)

coeff = pylab.polyfit(range(len(rabbits)), rabbits, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbits))))

coeff = pylab.polyfit(range(len(foxes)), foxes, 2)
pylab.plot(pylab.polyval(coeff, range(len(foxes))))

pylab.plot(rabbits)
pylab.plot(foxes)
pylab.ylabel("Population")
pylab.xlabel("Time Steps")
pylab.title("Foxes and Rabbits")
pylab.show()
