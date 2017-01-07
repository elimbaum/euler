# Project Euler 046
# Goldbach's Other Conjecture

from random import randrange
from math import floor, sqrt
import time

# how many witnesses are checked
DEFAULT_ITER = 3

# miller rabin primality test
# 	returns True if n is probably prime
# 	returns False if n is definitely composite
# iterations sets the accuracy (how many times loop is run)
#@profile
def prollyPrime(n, iterations = DEFAULT_ITER):
	# negative, 0, 1
	if n <= 1: return False
	# 2, 3
	if n <= 3: return True

	# check a few small primes
	if n % 2 == 0 or n % 3 == 0: return False

	if n in prollyPrime.primes: return prollyPrime.primes[n]

	# factor powers of 2 from n - 1
	d = n - 1
	r = 0
	while d & 1 == 0:
		d //= 2
		r += 1
	# n - 1 = 2^r * d

	for _ in range(iterations):
		a = randrange(2, n - 1)
		# compute a^d % n
		x = pow(a, d, n)
		if x == 1 or x == n - 1: continue

		composite = True
		for _ in range(r - 1):
			x = pow(x, 2, n)
			if x == 1: break
			if x == n - 1:
				composite = False
				break

		if composite:
			prollyPrime.primes[n] = False
			return False

	prollyPrime.primes[n] = True
	return True
# cache primes yay
prollyPrime.primes = {}

#@profile
def findcounterexample():
	odd = 9
	while True:
		# trying to find expression of the form
		# odd = prime + 2 * i^2
		# minimum prime is 3
		# so maximum i is
		# sqrt((odd - 3) / 2)
		max_i = floor(sqrt((odd - 3) // 2))

		# loop through all i [1, max_i]
		works = False
		for i in range(1, max_i + 1):
			if prollyPrime(odd - 2 * i * i):
				works = True
				break

		# nothing was found!
		if not works: return odd

		odd += 2
		while prollyPrime(odd): odd += 2


start_time = time.time()
result = findcounterexample()
end_time = time.time()
print("{} cannot be written".format(result))
print("Time: {} ms".format(round(1000 * (end_time - start_time), 3)))
