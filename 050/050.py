#!/usr/bin/env python3
# Project Euler 050
# Consecutive prime sums

from itertools import permutations, count, takewhile
from collections import deque
import time

UPPER_BOUND = 1000000

# eppstein sieve to generate primes
#@profile
def prime_gen():
	sieve = {}
	for q in count(2):
		if q not in sieve:
			# prime
			yield q
			# all factors [2..q-1] have already been seen, so the first multiple
			# of q not already seen is q^2.
			sieve[q * q] = [q]
		else:
			# composite
			for p in sieve[q]:
				# for each prime factor p, q = k_p * p. Add another p, giving
				# (k_p + 1) * p which is still divisible by p.
				sieve.setdefault(q + p, []).append(p)

			del sieve[q]

#@profile
def eppstein(n):
	primes = deque()
	sieve = {}
	for q in count(2):
		if q not in sieve:
			# prime
			if q > n: return primes
			primes.append(q)
			# all factors [2..q-1] have already been seen, so the first multiple
			# of q not already seen is q^2.
			sieve[q * q] = [q]
		else:
			# composite
			for p in sieve[q]:
				# for each prime factor p, q = k_p * p. Add another p, giving
				# (k_p + 1) * p which is still divisible by p.
				sieve.setdefault(q + p, []).append(p)

			del sieve[q]

def rwh_primes1(n):
	""" Returns  a list of primes < n """
	primes = deque([2])
	sieve = [True] * (n // 2)
	for i in range(3, int(n ** 0.5) + 1, 2):
		if sieve[i // 2]:
			sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
	primes.extend([2 * i + 1 for i in range(1, n // 2) if sieve[i]])
	return primes

def rwh_prime_gen(n):
	""" Returns a list of primes < n """
	yield 2
	sieve = [True] * (n // 2)
	for i in range(3, int(n ** 0.5) + 1, 2):
		if sieve[i // 2]:
			sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

	for i in range(1, n // 2):
	 	if sieve[i]: yield 2 * i + 1 

#@profile
def maxSum(N):
	prime_deque = deque(rwh_prime_gen(N))
	prime_set = set(prime_deque)

	maxlength = 0
	maxprime = None
	maxsum = 0

	while prime_deque:
		p = prime_deque.popleft()
		prime_set.discard(p)
		total = p
		length = 1
		#print(total)
		for q in prime_deque:
			#print("\t{}".format(q))
			total += q
			length += 1
			if total > N: break
			if length > maxlength and total in prime_set:
				#print("{} len {} = {}".format(p, length, total))
				maxlength = length
				maxsum = total
				maxprime = p

		# consecutive length < N is non-increasing. if maxlength seen exceeds
		# length of this iteration, there's no way we'll ever find a new
		# record. stop checking.
		if length < maxlength: break

	return (maxprime, maxlength, maxsum)


start = time.time()
p, length, total = maxSum(UPPER_BOUND)
end = time.time()
print("start {} has sum len {} = {}".format(p, length, total))
print("Time: {} ms".format(round(1000 * (end - start), 3)))
