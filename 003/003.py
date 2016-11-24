#! /usr/bin/env python3.3

"""
Project Euler problem 003
Largest Prime Factor

by Eli Baum
14 April 2013

"""

from math import *

print("Project Euler problem 003")
print("Largest Prime Factor")

n = float(input("n = "))


"""
We only need to find ONE prime factor.
Then we can divide, and factor that smaller number.

"""

largestPrime = 0
factored = False

while not factored:
	upperLimit = floor(sqrt(n))  # We only need to check up to sqrt(n)

	for i in range(2, upperLimit):
		factored = True  # If no more factors are found, while loop stops.
		if not (n % i):
			n /= i
			factored = False	
			if i > largestPrime:  # Add the highscore!
				largestPrime = i
			break

print(int(n))