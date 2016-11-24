# Euler 39
# Integer right triangles
import math
from time import time

start = time()

# Arbitrary.
EPSILON = 1E-9

# The lower-bound divisor
k = 1/math.sqrt(2) + 1

max_perimeter = 0 # which perimeter gives the highest solutions
max_solutions = 0 # how many solutions it gives



# Per problem
p = 1000
while p > 0:
	s = 0
	for a in range(1, p):
		b = (p * (p - 2 * a)) / (2 * (p - a))
		
		if b <= 0: continue
		
		# check if b is an int
		if abs(b - int(b)) < EPSILON:
			s += 1
			#print(p, a, b)
		
	if s > max_solutions:
		max_perimeter = p
		max_solutions = s
	p -= 1

end = time()

print(max_perimeter, "gives", max_solutions, "solutions.")
print(1000 * (end - start), "ms")