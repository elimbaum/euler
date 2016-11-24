# Euler 35
# Circular Primes
import math
from time import time

start = time()

badDigits = [0, 2, 4, 5, 6, 8]

def digitsOK(n):
	while n > 0:
		if n % 10 in badDigits: return False
		n //= 10
	return True

MAX = 1000000

# First, use sieve to generate primes < 1000000
isPrime = [True] * MAX

# Hard-code 0 and 1 as not prime.
isPrime[0] = isPrime[1] = False

maxCheck = int(math.sqrt(MAX))
# Skip the evens, because the digitsOK() function will remove all of them.
for n in range(3, maxCheck, 2):
	if isPrime[n]:
		for i in range(n * n, MAX, n):
			isPrime[i] = False

middle = time()

alreadyChecked = [False] * MAX
# Start off with 2, 3, 5, 7 (single digits)
count = 4

# Start at the double digits; skip evens
for n in range(11, MAX, 2):
	# check last digit mod 3
	if n % 3 == 0: continue
	if not isPrime[n]: continue
	if not digitsOK(n): continue
	if alreadyChecked[n]: continue
	
	# hold the count while the rotations are checked
	tempCount = 0
	temp = n
	multiplier = int(math.pow(10, int(math.log10(n))))
	while True:
		temp = (temp // 10) + (temp % 10) * multiplier
		alreadyChecked[temp] = True
		
		if not isPrime[temp]: break
		
		tempCount += 1
		if temp == n:
			count += tempCount
			break # all done!

end = time()

print(count)
print("Sieve:\t", 1000 * (middle - start), "ms")
print("Check:\t", 1000 * (end - middle), "ms")
print("Total:\t", 1000 * (end - start), "ms")
