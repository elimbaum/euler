#! /usr/bin/env python3.3

"""
Project Euler problem 003
Largest Prime Factor

Optimal solution, from the website answer.

by Eli Baum
14 April 2013

"""

from math import *

print("Project Euler problem 003")
print("Largest Prime Factor")

n = float(input("n = "))


"""
Find the first prime factor.
Then, divide out ALL instances of it.

In addition, with the exception of 2, only odd numbers need to be tested.

"""

factor = 1

if n % 2 == 0:  # Check 2 first.
	n = n / 2
	factor = 2	
	while n % 2 == 0:
		n = n / 2

if n == 1:
		print(int(factor))  # n was just a power of two!
else:
	factor = 3
	while True:
		if n % factor == 0:
			n = n / factor
			while n % factor == 0:
				n = n / factor
		if n == 1:
			print(int(factor))
			break
		
		factor += 2