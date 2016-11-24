# 031
# Coin Sums
# From the overview.
# Runs in ~0.4 ms

coins = [1, 2, 5, 10, 20, 50, 100, 200]

amount = 200

ways = [0 for _ in range(amount + 1)]
ways[0] = 1

for c in coins:
	for j in range(c, amount + 1):
		ways[j] += ways[j - c]

print(ways[amount])