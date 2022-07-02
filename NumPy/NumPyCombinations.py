# -*- coding: utf-8 -*-
"""
Created on Mon May  8 20:29:42 2017

@author: phyns
"""
import numpy as np
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    combinations = list()
    choicesArray = np.array(choices)
    
    # Generate all possible combinations
    for combinationNumber in range(2**len(choices)):
        combination = list(bin(combinationNumber)[2:])
        while len(combination) < len(choices):
            combination.insert(0,0)
        combinations.append(np.array(combination,np.int))
    
    # Find combinations that gives the total
    possibleCombinations = list()
    for combination in combinations:
        if sum(combination * choicesArray) == total:
            possibleCombinations.append(combination)
    
    # Find the best combination
    if possibleCombinations != list():
        minElementsToTotal = int()
        for combination in possibleCombinations:
            elementsInCombination = sum(combination)
            if elementsInCombination < minElementsToTotal or minElementsToTotal is int():
                bestCombination, minElementsToTotal = combination, elementsInCombination
        return bestCombination
            
    else:
        # If not any combination with exact total, find the closest possible
        margin = 1
        while margin < len(choices):
            for combination in combinations:
                if sum(combination * choicesArray) == (total - margin):
                    return combination
            margin += 1
    
    return np.array(choices)
    

print(find_combination([1,2,2,3],4))
print(find_combination([1,1,3,5,3],5))
print(find_combination([1,1,1,9],4))
print(find_combination([4, 6, 3, 5, 2], 10))
print(find_combination([1], 10))
