# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 08:32:53 2016

@author: phyns
"""
def longest_run(L):
    """ Assumes L is a list of integers containing at least 2 elements. Finds the longest run of numbers in L, where the longest run can either be monotonically increasing or monotonically decreasing. In case of a tie for the longest run, choose the longest run that occurs first. Does not modify the list. Returns the sum of the longest run. """
    ## Find the logest monotonically INCREASING run
    BestIncRun = []
    for index in range(len(L)):
        ## Scan the Run
        firstScanIndex = index
        lastScanIndex = index + 1
        thisIndexRun = [L[firstScanIndex],]
        EndOfThisRun = False
        while EndOfThisRun == False:
            if lastScanIndex >= len(L) or L[firstScanIndex] > L[lastScanIndex]:
                EndOfThisRun = True
            else:
                thisIndexRun.append(L[lastScanIndex])
                firstScanIndex += 1
                lastScanIndex += 1
        ## Store the run if is the longest until now
        if len(BestIncRun) < len(thisIndexRun):
            BestIncRun = thisIndexRun.copy()
            BestIncStarts = index
    
    ## Find the logest monotonically DECREASING run
    BestDecRun = []
    for indexR in reversed(range(len(L))):
        ## Scan the Run
        firstScanIndex = indexR - 1
        lastScanIndex = indexR
        thisIndexRun = [L[lastScanIndex]]
        EndOfThisRun = False
        while EndOfThisRun == False:
            if firstScanIndex < 0 or L[firstScanIndex] < L[lastScanIndex]:
                EndOfThisRun = True
            else:
                thisIndexRun.append(L[firstScanIndex])
                firstScanIndex -= 1
                lastScanIndex -= 1
        ## Store the run if is the longest until now
        if len(BestDecRun) <= len(thisIndexRun):
            BestDecRun = thisIndexRun.copy()
            BestDecStarts = firstScanIndex
    
    ## Search the largest, if equal which started first
    BestRun = []
    if len(BestIncRun) > len(BestDecRun):
        BestRun = BestIncRun.copy()
    elif len(BestIncRun) < len(BestDecRun):
        BestRun = BestDecRun.copy()
    elif len(BestIncRun) == len(BestDecRun):
        if BestIncStarts < BestDecStarts:
            BestRun = BestIncRun.copy()
        else:
            BestRun = BestDecRun.copy()

    ## Return the sum of the longest
    BestRunSum = 0
    for element in BestRun:
        BestRunSum += element
    return BestRunSum