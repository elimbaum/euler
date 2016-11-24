#! /usr/bin/env python3.3

"""
Project Euler 010
Sum of primes < 2M

Uses sieve of eratosthenes.


Form overview: not perfect, but this is the general idea.
Takes 1.28s, but keep in mind this is interpreted, *not* compiled.
Would be no doubt faster in c.
(overview claims algorithm runs in < 1s)

However the overhead (before functions and loops), just init, takes
0.06s.

"""

from math import *

nMax = 2000000 # check up to here.

# 0 is prime, 1 is composite (marked)
# array will only have odd numbers, so can be twice as small
# and will also start with 3 (we don't care about 1)
primeArray = [0] * (nMax // 2)	# fill with 0s


sum = 2 # start off with 2 b/c we're not looking at evens.

currentNumber = 3 # we'll go up by 2*n so we can skip evens.

currentMultiple = 3 # the prime number. Start at 3

maxCheck = floor(sqrt(nMax))


def isMarked(x):
	# x should always be odd.
	return primeArray[(x - 3) // 2]

while currentMultiple < maxCheck:
	if not isMarked(currentMultiple): # we have a prime!
		#print(currentMultiple, "is a prime!  Sum:", sum)
		sum += currentMultiple # add the prime
	
		currentNumber = currentMultiple * currentMultiple # start at prime' square (faster)
		# mark all multiples
		while currentNumber < nMax:
			primeArray[(currentNumber - 3) // 2] = 1 # mark it
			currentNumber += 2 * currentMultiple
	
	currentMultiple += 2 # check the next odd number to be a prime
	
# now we have all primes less than sqrt(nMax). Now just add the remaining primes.

currentNumber = maxCheck

if currentNumber & 1:
	currentNumber += 1 # make it odd if its not


while currentNumber < nMax:
	if not isMarked(currentNumber):
		sum += currentNumber
		#print(currentNumber, "is a prime!  Sum:", sum)
		
	currentNumber += 2
	
print("Final sum is", sum)
	
	
		
		

	