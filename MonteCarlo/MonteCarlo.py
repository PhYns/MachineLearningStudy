# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:23:19 2017

@author: phyns
"""
import random

def generateBucket(howmanyreds,howmanygreens):
    '''
    Returns a list of bucket with 'howmanyred' red balls and 'howmanygreens' green balls
    
    howmanyreds and how manygreens are ints
    '''
    Bucket = list()
    
    for redballs in range(howmanyreds):
        Bucket.append("Red Ball")
    
    for greenballs in range(howmanygreens):
        Bucket.append("Green Ball")
    
    random.shuffle(Bucket)
    
    return Bucket

def pickBall(howmanyballsPicked,listOfBalls):
    '''
    This functions returns a list of 'howmanyballsPicked' balls
    randomly choosen
    
    howmanyballsPicked is an int
    listOfBalls is a list
    '''
    ballsPicked = list()
    bucket = listOfBalls.copy()
    for pick in range(howmanyballsPicked):
        ballsPicked.append(bucket.pop(bucket.index(random.choice(bucket))))
    
    return ballsPicked

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    SameColor = 0
    for trial in range(numTrials):      
        ballspicked = pickBall(3,generateBucket(4,4))
        if ballspicked[1:] == ballspicked[:-1]:
            SameColor += 1
    
    return float(SameColor/numTrials)
