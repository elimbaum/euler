#! /usr/bin/env python3.3

"""
Project Euler problem 001
Multiples of 3 and 5

Optimal Result, from the answer.

"""

n = int(input("n = ")) - 1  # Because we don't want to count 1000

def sumMultiples(m):
	p = n // m
	return int(m * (p * (p+1)) / 2)
	
print(sumMultiples(3)+sumMultiples(5)-sumMultiples(15))
