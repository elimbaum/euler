#! /usr/bin/env python3.3

"""
Project Euler problem 002
Even Fibonacci Numbers

by Eli Baum
14 April 2013

"""

print("Project Euler problem 002")
print("Even Fibonacci Numbers")

n = int(input("Upper Limit: "))

# Brute-Force calculate all of the fibonacci numbers

a, b = 0, 1
sum = 0

while True:
	a, b = a + b, a
	if a > n:
		break # We have reached the upper limit; stop
	
	if a % 2:
		sum += a
	
print(sum)