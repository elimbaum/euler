#!/usr/bin/env python3

# Project Euler 049
# Prime permutations

from itertools import permutations, count, takewhile
import time

# eppstein sieve to generate primes
def primes():
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

def findPerms():
	primegen = primes()

	fourprimes = set()

	# prime the prime generator (hehe)
	for p in primegen:
		if p > 1000:
			fourprimes.add(p)
			break

	# find all the primes
	fourprimes.update(takewhile((lambda x: x < 10000), primegen))

	for p in fourprimes:
		perms = set(filter((lambda x: x in fourprimes and x > p),
							[int("".join(q)) for q in permutations(str(p))]))
		if len(perms) < 2:
			continue

		for q in perms:
			if (2 * q - p) in perms:
				yield (p, q)

start = time.time()
results = list(findPerms())
end = time.time()
for r in results:
	print("{0} {1} {2} -> {0}{1}{2}".format(r[0], r[1], 2 * r[1] - r[0]))

print("Time: {} ms".format(round(1000 * (end - start), 3)))