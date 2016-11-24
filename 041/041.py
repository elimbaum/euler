#coding: utf-8
# Project Euler 041
# Largest pandigital prime
#
# answer: 7652413

import math

# checks if n is m-digit pandigital, where m is the length of n
# NOTE this doesn't actually work properly. Only gives if no repeated digits.
def isPandigital(n):
	digits = set()
	digits.add(0)
	while n > 0:
		d = n % 10
		if d in digits: return False
		digits.add(d)
		n //= 10
	
	return True

max = 7654321
min = 1234567

# first generate all necessary primes up to √max
primes = [2, 3]

k = 5
max_check = math.floor(math.sqrt(max))
lower = True # for the 6k±1

while k <= max_check:
	isPrime = True
	for p in primes:
		if k % p == 0:
			isPrime = False
			break
	
	if isPrime: primes.append(k)
	
	if lower: k += 2
	else: k += 4
	
	lower = not lower

n = max
while n >= min:
	# check if n is prime
	isPrime = True
	for p in primes:
		if n % p == 0:
			isPrime = False
			break
			
	if isPandigital(n) and isPrime:
		print(n)
		break
	
	# This saves 9x the work
	n -= 9
