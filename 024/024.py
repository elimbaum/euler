# Euler 024
# Lexicographic Permutations
#
# What is the 1 000 000 th lexicographic permutation of the digits 0-9?

import math

# The permutation number (1-indexed)
n = 1000000
n -= 1 # make it 0-indexed

digits = list(range(10))

s = ""

for i in reversed(range(10)):
	f = n // math.factorial(i)
	s += str(digits[f])
	del digits[f] # no repeats allowed, so remove it
	n %= math.factorial(i)

print(s)