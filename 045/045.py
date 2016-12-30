# Project Euler 045
# Triangular & Pentagonal numbers
#
# don't recompute if you can just increment!

import time
from math import sqrt

def findNext():
	# current values
	hi = 143
	pi = 165
	p = h = hi * (2 * hi - 1)

	while True:
		if p < h:
			p += 3 * pi + 1
			pi += 1
		else:
			h += 4 * hi + 1
			hi += 1

		if p == h:
			return p



start_time = time.time()
result = findNext()
end_time = time.time()
print(result)
print("Time: {} ms".format(1000 * (end_time - start_time)))