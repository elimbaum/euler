# Project Euler 043
# Sub-string divisibility

# Returns the index of the first nonunique element of x 
def uniqList(x):
	seen = set()
	for i in range(len(x)):
		if x[i] in seen: return False
		seen.add(x[i])
	return True

# The set of primes to check
primes = [2, 3, 5, 7, 11, 13, 17]

# The list of allowed digits
digits = {}

a = set()
i = 0
digits[primes[0]] = []

while i < 1000:
	d = [i // 100, i // 10 % 10, i % 10]
	
	if uniqList(d):
		digits[primes[0]].append(d)
		a.add(i % 100)
	
	i += primes[0]
	
# Don't check the first one
for p in primes[1:]:
	b = set()
	i = 0
	digits[p] = []
	while i < 1000:
		if i // 10 in a:
			d = [i // 100, i // 10 % 10, i % 10]
			if uniqList(d):
				b.add(i % 100)
				digits[p].append(d)
		i += p
	a = b

i = -1
j = 0

# for p in primes:
# 	print(p, digits[p])


# All allowed three-digit susbtrings have been generated.
# Now create permutations and check for pandigital-ness.

size = len(digits)

# holds the current arrangement
counter = [0 for _ in range(size)]
done = False
maxLen = 0


#
# doing it backwards.
#

while not done:
	n = list(digits[primes[-1]][counter[-1]])
	
	num_ok = True

	for i in reversed(range(size)[:-1]):
		#print(primes[i])
		if n[:2] == digits[primes[i]][counter[i]][-2:]:
			n = digits[primes[i]][counter[i]][0] + n
			print(n)
		else:
			# doesn't match
			#num_ok = False
			break

		if not uniqList(n):
			# repeated digit
			num_ok = False
			break

	if num_ok and len(n) > maxLen:
		print(n)
		maxLen = len(n)

	for i in range(size):
		if counter[i] == len(digits[primes[i]]) - 1:
			counter[i] = 0
			if i == size - 1: done = True
		else:
			counter[i] += 1
			break
