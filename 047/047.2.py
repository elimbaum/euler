#!/usr/bin/env python3

# Project Euler 047
# Distinct Prime Factors
#
# call as ./047.py n
# where n is the number of consecutive/distinct prime factors
#
# better version, using a progressive sieve.
# 								...yes! they exist!

import sys
import time
from itertools import count

#@profile
def compute(N):
	sieve = {}
	for i in count(2):
		if i not in sieve:
			# prime!
			consec = 0
			p = i
		else:
			# composite
			p, factors = sieve.pop(i)
			if factors < N:
				consec = 0
			else:
				consec += 1
				if consec == N: return i - N + 1

		while True:
			i += p
			if i not in sieve: break
			sieve[i][1] += 1
			#print("\t {} {}".format(i, sieve[i]))
		sieve[i] = [p, 1]
		#print("\t {} {}".format(i, sieve[i]))

starttime = time.time()
N = int(sys.argv[1])
result = compute(N)
endtime = time.time()
print("Lowest of consecutive: {}".format(result))
print("Time: {} ms".format(round(1000 * (endtime - starttime), 3)))

