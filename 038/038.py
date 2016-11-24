# Euler 038
# Pandigital Multiples
import math
from time import time

# No zeros or repeat digits allowed
def digitsOK(n):
	digits = set()
	while n > 0:
		d = n % 10
		if d in digits or d == 0: return False
		digits.add(d)
		n //= 10
		
	return True

def run():
	for z in range(9876, 5000, -1):
		if not digitsOK(z): continue
		z *= 2
		if not digitsOK(z): continue
		
		# 10000 can be hardcoded because 2 * z is known to be 5 digits
		# Just factored a z out of the expression.
		# 100000 * z + 2 * z -> 100002 * z
		# Already multiplied by 2 above, so multiply by the other half
		z *= 50001
	
		# Found the answer!
		if digitsOK(z): break
	
	return z

N = 1000

start = time()
for _ in range(N):
	run()
end = time()

print(run())
print(1000.0 * (end - start) / N, "ms per iter")
			