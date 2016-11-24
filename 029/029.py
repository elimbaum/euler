# Euler 029
# Distinct Powers
# This non-brute force solution is actually slower than the brute force.
# I'll come back to this problem again, probably.

from math import sqrt, ceil
from time import time

def isPrime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
		
	if n % 2 == 0 or n % 3 == 0:
		return False;
	
	k = 6
	while (k - 1) <= sqrt(n):
		if n % (k + 1) == 0 or n % (k - 1) == 0:
			return False
		k += 6
	
	return True

# returns the next prime > p (which is not necessarily a prime)
# p must be a positive integer
def nextPrime(p):
	if p <= 2:
		return p + 1
	if p == 3:
		return 5
	
	# Err on the side of caution
	# Set k to a minimum value.
	k = (p - 1) // 6
	
	next = 6 * k - 1
	if isPrime(next) and next > p: return next
	
	next += 2 # 6 * k + 1
	if isPrime(next) and next > p: return next
	
	# Move on to the next k-value.
	k += 1
	
	while 1:
		next = 6 * k - 1
		if isPrime(next) and next > p: return next
		
		next += 2 # 6 * k + 1
		if isPrime(next) and next > p: return next
		
		# no luck this time! next k
		k += 1 

def countUnique(max):
	count = (max - 1) ** 2


	# generate primes
	primes = [2]
	while True:
		p = nextPrime(primes[-1])
		if p <= max:
			primes.append(p)
		else: break
	

	# generate factors on the interval [2, max]
	factors = []
	for n in range(2, max + 1):
		factors.append([])
		for p in primes:
			exp = 0
			d = n
			while d % p == 0:
				d //= p
				exp += 1
		
			# make sure to subtract 2 from the index
			if exp > 0: factors[n - 2].append((p, exp))

	unique = set()

	for a in range(2, max + 1):
		for b in range(2, max + 1):
			p = list(factors[a - 2])
			for i in range(len(p)):
				p[i] = (p[i][0], p[i][1] * b)
		
			p = frozenset(p)
			unique.add(p)
		
	return len(unique)

s = time()
u = countUnique(100)
e = time()
print(u)
print(1000 * (e - s))

#for i in range(4, 101):
	#u = countUnique(i)
	#print(i, "\t", u, "\t", i ** 2 - u, sep="")






