import random, pylab
random.seed(0)

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values,bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title is not None:
        pylab.title(title)
    pylab.show()

# Implement this -- Coding Part 2 of 2
def findLongestRun(rolls):
    '''
    Returns an int of the longest run of the same numbers in an sequence
    '''
    longestRun = 1

    for begin in range(len(rolls)-1):

        start, end, run = begin, begin + 1, 1

        while rolls[start] == rolls[end]:
            run = end - begin + 1
            start, end = end, end + 1
            if end > len(rolls)-1:
                break

        if run > longestRun:
            longestRun = run

    return longestRun

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longestRuns = list()
    for trial in range(numTrials):

        # Do a barrel roll
        rollsResult = list()
        for roll in range(numRolls):
            rollsResult.append(die.roll())

        # Find the longest run
        longestRuns.append(findLongestRun(rollsResult))

    # Plot histogram
    makeHistogram(longestRuns,10,"Means of the Longest Run","Number of Trials", "Distribution of the longest Runs")

    return sum(longestRuns)/float(len(longestRuns))

## One test case
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))

# Test 1
print("Test 1",getAverage(Die([1]), 10, 1000))

# Test 2
print("Test 2",getAverage(Die([1,1]), 10, 1000))

# Test 3
print("Test 3",getAverage(Die([1,2,3,4,5,6]), 50, 1000))

# Test 4
print("Test 4",getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 1000))

# Test 5
print("Test 5",getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))
