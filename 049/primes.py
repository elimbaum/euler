
from itertools import count

def primes():
	sieve = {}
	for q in count(2):
		if q not in sieve:
			# prime
			yield q
			sieve[q * q] = [q]
		else:
			# composite
			for p in sieve[q]:
				sieve.setdefault(p + q, []).append(p)
			del sieve[q]

gen = primes()

p = next(gen)
while p < 1000:
	print("\t" + str(p))
	p = next(gen)

print(p)

for p in gen:
	if p > 10000: break
	print(p)
print("\t" + str(p))