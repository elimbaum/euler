# Euler 33
# Digit canceling fractions
from time import time

# Euclidean GCD algorithm method.
def simplify(a, b):
	n = a
	d = b
	while d > 0:
		t = n % d
		n = d
		d = t
		
	return (a // n, b // n)

start = time()

numerator = 1
denominator = 1

for a in range(1, 9 + 1):
	for b in range(1, 9 + 1):
		if a == b: continue
		for c in range(1, 9 + 1):
			if c < a: continue # This prevents checking duplicates and > 1
			if (10 * a * (c - b)) == (c * (a - b)):
				numerator *= a
				denominator *= c

simp = simplify(numerator, denominator)

end = time()

print("Product: ")
print(numerator, "/", denominator, " --> ", simp[0], "/", simp[1], sep="")
print(1000 * (end - start), "ms")