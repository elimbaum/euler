#! /usr/bin/env python3.3

"""
Project Euler problem 007
10001st Prime

Eli Baum
Nov 2013


EDIT: best way is to use the fact that ALL primes are of the form 6k+/-1. See overview.
"""


print("Project Euler 007")
print("10,001st Prime")

from math import *

primeIndex = 10001 # which number prime to find

primesFound = 1 # counting 2

currentNumber = 1 # starts looking at 3 because immediately incremented by 2.


while primesFound < primeIndex:
	
	currentNumber += 2 # check the next (odd) number
	upperLimit = ceil(sqrt(currentNumber))
	currentFactor = 2
	while currentFactor <= upperLimit:
		#print("currentNumber =", currentNumber, "\tcurrentFactor =", currentFactor)
		isComposite = False
		if currentNumber % currentFactor == 0:
			# this is not a prime!
			#print("composite!")
			isComposite = True
			break
		
		currentFactor += 1 + (currentFactor & 1) # move on to the next factor.
								# ^ this is 1 iff currentFactor is odd
	
	if not isComposite:
		# we've gone through all of the odd numbers. we have a prime.
		primesFound += 1
		#print("!!!", currentNumber, "is the", primesFound, "prime.")
	
	


print(currentNumber)