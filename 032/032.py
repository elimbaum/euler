# Euler 32
# Pandigital Products
#
# Sum of all products p where a * b = p, given that abp contains all 9 digits.
#
# When benchmarked, runs in less than 30 ms.

from time import time

MAX = 9999
# Stores the digits of each number OFFSET..MAX
digits = [[] for _ in range(MAX)]

# To test against
allOnes = [1] * 9

# Holds past pandigitals
# sets don't allow for repeats, and are faster.
pandigitals = set()

# Returns the digits of n
def getDigits(n):
	# stores 1..9 (9 elements)
	result = [0 for _ in range(9)]
	while n > 0:
		d = n % 10
		# Zero & repeated digits aren't allowed.
		if d == 0 or result[d - 1] != 0: return -1
		result[d - 1] = 1
		n //= 10
	
	return result

def checkPandigital(a, b):
	# For speed
	# a, b, product are decremented because they are usually required
	# in that form (for array indexes)
	# Where their original form is required, a + 1 is used.
	product = a * b - 1
	a -= 1
	b -= 1
	
	# Memoization
	if not digits[a]: digits[a] = getDigits(a + 1)
	if not digits[b]: digits[b] = getDigits(b + 1)
	if not digits[product]: digits[product] = getDigits(product + 1)
	
	if -1 in (digits[a], digits[b], digits[product]): return

	if [sum(x) for x in zip(digits[a], digits[b], digits[product])] \
		== allOnes:
		pandigitals.add(product)
		#print(a + 1, "*", b + 1, "=", product + 1)

def compute():
	# First check 1 digit * 4 digit
	# Don't check 5.
	for a in (2, 3, 4, 6, 7, 8, 9):
		for b in range(1234, 9876 + 1):
			if b % 5 == 0 or b % 10 == 1: continue 
			# too big.. move on to next a
			if a * b > MAX: break
			checkPandigital(a, b)
	
	# Now check 2 digit * 3 digit
	for a in range(12, 98 + 1):
		if a % 5 == 0: continue
		for b in range(123, 987 + 1):
			if b % 5 == 0 or b % 10 == 1: continue 
			if a * b > MAX: break
			checkPandigital(a, b)
			
EXECS = 1000
start = time()
for _ in range(EXECS): compute()
end = time()
print(sum(pandigitals))
print(1000.0 * (end - start) / EXECS, "ms per iter")
			
			