# Project Euler 044
# Pentagon Numbers

from math import sqrt
import time

#@profile
def minimize():
	pents = {}

	i = 1
	pi = 1
	while True:
		diff = sumf = pi = pi + 1 + 3 * i
		i += 1
		pents[pi] = True

		for j in range(1, i):
			delta = 3 * j - 2
			diff -= delta
			sumf += delta

			if pents.get(diff, False) and (sqrt(24 * sumf + 1) % 6 == 5):
				print(i, j)
				return diff


start_time = time.time()
answer = minimize()
end_time = time.time()
print(answer)
print("Time: {} ms".format(1000 * (end_time - start_time)))