# Project Euler 043
# Substring Divisibility
from collections import namedtuple
import time

def compute():
	primes = [2, 3, 5, 7, 11, 13, 17]

	left = []
	right = []

	p = primes.pop()

	# preload with multiples of 17
	for i in range(p, 1000, p):
		# but reverse order hehe
		a = i % 10
		b = (i // 10) % 10
		c = i // 100
		if a == b or a == c or b == c: continue
		left.append([a, b, c])

	stack = left
	other = right
	while primes:
		p = primes.pop()

		while stack:
			n = stack.pop()
			#print("checking {}".format(n))
			for x in range(10):
				# make it pandigital by construction
				if x not in n and (100 * x + 10 * n[-1] + n[-2]) % p == 0:
					new = list(n)
					new.append(x)
					other.append(new)
		
		# swap stacks
		temp = stack
		stack = other
		other = temp
		#print("FLIP")

	totalSum = 0

	for s in stack:
		digits = set(range(10))

		# convert to int
		#print(s, end=" => ")

		n = 0
		while s:
			n *= 10
			d = s.pop()
			n += d
			digits.remove(d)

		# prepend final (first?) digit
		n = digits.pop() * (10 ** 9) + n
		#print(n)
		totalSum += n
	return totalSum


start_time = time.time()
answer = compute()
end_time = time.time()

print(answer)
print("Time: {} us".format(1e6 * (end_time - start_time)))
