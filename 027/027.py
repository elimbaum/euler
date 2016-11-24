# Euler 027
# Quadratic Primes
#
# This is the main program.
#
# General quadratic:
# (x - k/2)^2 + v
# should generate primes from x = 0..n, where n is maximized.
#
# I have determined that v must be 41 - 0.25 = 40.75,
# and k must be positive and odd.
#
# Also: given n^2 + an + b, b < 1000 and b = k^2/4 + v - 0.25
# So k^2/4 + v - 0.25 < 1000
# This program just solves the inequality above.
#
# EXTREMELY fast... the problem isn't ACTUALLY as hard as I thought.

from math import sqrt
from time import time

start = time()
v = 41

k = int(sqrt(4 * (1000.25 - v)))

# a equals k. b equals k^2/4 - 1/4 + v. Find the product.
# Negative for semantics.
print(-k * ((k*k - 1)//4 + v))

end = time()
print(1000000*(end-start), "us")