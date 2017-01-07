# Project Euler 048
# Self Powers
# Gives last DIGITS digits of 
#
# sum_k=1^MAX k^k

import time

start = time.time()

DIGITS = 10
d = 10 ** DIGITS

MAX = 1000

s = sum(pow(i, i, d) for i in range(1, MAX + 1)) % d

end = time.time()

print(s)
print(round(1000 * (end - start), 3))