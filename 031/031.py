# Euler 031
# Coins Sums
from time import time

# Amount to make, in pence
AMOUNT = 200

# Not including the 1p coin.
coins = [200, 100, 50, 20, 10, 5, 2]

purse = []

count = 0

def getAmount(): return sum([a*b for a, b in zip(coins, purse)])

def compute():
	global count, purse
	purse = [0 for _ in range(len(coins))]
	remainder = AMOUNT
	for i in range(len(coins)):
		c = remainder // coins[i]
		purse[i] = c
		remainder -= c * coins[i]

		if remainder == 0: break

	# Iterate through
	level = 0
	count = 1 # include the above above
	empty = [0] * len(coins)
	while purse != empty:
		# Take one down, pass it around...
		purse[level] -= 1
	
		if level < len(coins) - 1:
			level += 1
			currentCoin = coins[level]
		
			next = AMOUNT - getAmount()
			numCoins = next // currentCoin
			purse[level] = numCoins
			next -= numCoins * currentCoin
		
			if next % currentCoin > 0:
				for i in range(level, len(coins)):
					numCoins = next // coins[i]
					purse[i] += numCoins
					next -= numCoins * coins[i]
					level = i
				
		while level > 0 and purse[level] == 0:
			level -= 1
		
		count += 1

NUM_EXECS = 1
start = time()

for _ in range(NUM_EXECS):
	compute()
	
end = time()
print(count)
print(1000.0 * (end - start) / NUM_EXECS, "ms per iter")
	
	