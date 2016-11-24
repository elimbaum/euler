# Euler 026
# Reciprocal Cycles
#
# Don't acually have to store the result.

from math import ceil, log10
from time import time

t_start = time()

longest = (0, 0)

# only check odds; count backwards
for d in range(999, 501, -1):
	
	# Take out 2s and 5s here. (ten partially-divisible... non repeating)
	# Could take out more primes but not worth it.
	if d % 2 == 0 or d % 5 == 0:
		continue
		
	base = 10**int(ceil(log10(d)))
	
	l = 0

	started = False
	b = base

	while True:
		if b < d:
			b *= 10
		
		if started and (b == base or b == 0):
			break;
		
		b %= d
		l += 1
	
		started = True
	
	# Check if new record
	if l > longest[1]:
		longest = (d, l)
		
	# cycle length is always less than d.
	# so if current longest is longer than d, it's done.
	if longest[1] > d:
		break
	
t_end = time()

print(longest)
print("found in", str(1000*(t_end - t_start)), "ms")
