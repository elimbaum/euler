# 029 brute force test.
from time import time

s = time()

MAX = 100
all = set()

for a in range(2, MAX + 1):
	for b in range(2, MAX + 1):
		all.add(a ** b)

print(len(all))

print(1000 * (time() - s))