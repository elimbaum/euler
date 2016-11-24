# 111factor.py
# Prime factorizes numbers consisting of all 1s
# can easily be adapted to a generalized prime factorizer
# For use with Euler 026.

from math import sqrt, ceil
import signal

def isPrime(n):
	if n <= 1:
		return False
	if n <= 3:
		return True
		
	if n % 2 == 0 or n % 3 == 0:
		return False;
	
	k = 1
	while (6 * k - 1) <= sqrt(n):
		if n % (6 * k + 1) == 0 or n % (6 * k - 1) == 0:
			return False
		k += 1
	
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
	

def status(s, f):
	print('\t-->',n, p)
	
# Get status with control-T (mac only)
signal.signal(signal.SIGINFO, status)

for i in range(0, 18 + 1):
	n = 0
	for j in range(i):
		n += 10 ** j
	
	print(n)
	
	# n now has i 1s... factorize by looping through primes.
	p = 2
	while p < sqrt(n):
		while n % p == 0:
			n //= p
			print('\t', p)
		p = nextPrime(p)
	# remaining n is prime
	print('\t', n)

	
	
	
	

