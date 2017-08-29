# -*- coding: utf-8 -*-
"""
lets generate "methinks it is like a weasel".
Guess a quote by Shakespeare
"""
import string
from random import randrange

AVAILABLE = string.ascii_lowercase + " "
SIZE = len(AVAILABLE)
LENGTH = 28
TARGET = "methinks it is like a weasel"

'''
    returns random string of length 28
'''
def randomSlow():
    res = ''
    for _ in range(LENGTH):
        res += AVAILABLE[randrange(0, SIZE)]
    return res

'''
    change different characters of input to hill climb TARGET
'''
def randomUpdateBest(guess):
    res = ''
    for i in range(LENGTH):
        if guess[i] == TARGET[i]:
            res += guess[i]
        else:
            res += AVAILABLE[randrange(0, SIZE)]
    return res

'''
    return score
'''
def rateGuess(guess):
    return len([i for i in range(LENGTH) if guess[i] == TARGET[i]])


def driver():
    currentGuess = randomSlow()
    guessed = False
    iterations = 0
    while not guessed:
        currentScore = rateGuess(currentGuess)
        currentGuess = randomUpdateBest(currentGuess)
        iterations += 1
        if currentScore == LENGTH:
            guessed = True
    print("Found in ", iterations, "iterations, ", currentGuess)
    
if __name__ == '__main__':
    driver()