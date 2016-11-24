# Euler 39 (better version)
# From the forum.
# Some improvements on my part... 2000x faster than the original.

from time import time

start = time()

def gcd(a, b):
	while b > 0:
		t = a % b
		a = b
		b = t
	return a

upper = 1000
perimeters = [0] * (upper + 1)

maxCheck = int((upper / 4) ** 0.5)

for m in range(2, maxCheck):
	for n in range(1, m, 2): 
		if gcd(m, n) != 1: continue
		
		# Per the Pythagorean Triple generating formula
		t = p = 2 * m * (n + m)
		while t <= upper:
			perimeters[t] += 1
			t += p

ans = perimeters.index(max(perimeters))
end = time()

print(ans)
print(1000 * (end - start))