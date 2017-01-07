#!/usr/bin/env python3

# Project Euler 047
# Distinct Prime Factors
#
# call as ./047.py n
# where n is the number of consecutive/distinct prime factors

import sys
import time

@profile
def getPrimeFactors(n):
	cache = getPrimeFactors.cache
	factors = set()
	
	m = n

	# check 2 and 3 manually
	if m % 2 == 0:
		factors.add(2)
		while m % 2 == 0: m //= 2

	if m % 3 == 0:
		factors.add(3)
		while m % 3 == 0: m //= 3


	# check the rest
	k = 6
	while m > 1:
		# can memoize here
		if m in cache:
			#print("[{}] memoized; {} {} already in".format(n, m, cache[m]), end="\t")
			factors |= cache[m]
			break

		if m % (k - 1) == 0:
			factors.add(k - 1)
			while m % (k - 1) == 0: m //= (k - 1)
		if m % (k + 1) == 0:
			factors.add(k + 1)
			while m % (k + 1) == 0: m //= (k + 1)

		k += 6

	cache[n] = factors
	return factors
getPrimeFactors.cache = {}

@profile
def compute(N):
	# first couple of primes, for computing lower bound
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	LOWER_BOUND = 1
	for i in range(N): LOWER_BOUND *= primes[i]

	i = LOWER_BOUND
	while True:
		pf = getPrimeFactors(i)
		if len(pf) == N:
			# check neighborhood back and forth
			checkDown = True
			down = i
			checkUp = True
			up = i

			while up - down + 1 < N and (checkUp or checkDown):
				if checkDown:
					down -= 1
					pfd = getPrimeFactors(down)
					if len(pfd) != N:
						checkDown = False
						down += 1
				if checkUp:
					up += 1
					pfu = getPrimeFactors(up)
					if len(pfu) != N:
						checkUp = False
						up -= 1

			if up - down + 1 >= N:
				return down
		i += N

starttime = time.time()
N = int(sys.argv[1])
result = compute(N)
endtime = time.time()
print("Lowest of consecutive: {}".format(result))
for i in range(N):
	print(result + i, getPrimeFactors(result + i))
print("Time: {} ms".format(round(1000 * (endtime - starttime), 3)))

