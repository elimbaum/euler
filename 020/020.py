# Euler 20
# Digit sum of 100!

# store the product in an array or digits
product = [1]

target = 99
n = 1
carry = 0

while n <= target:
			
	for p in reversed(range(len(product))):
		interProd = product[p] * n + carry
		# compute new carry
		product[p] = interProd % 10
		carry = interProd // 10
		
	# carry may be multi digit.
	while carry > 0:
		product = [carry % 10] + product
		carry = carry // 10

	n += 1

# asterisk returns pointer, allows concatenation of array elements
#print(*product, sep='')
print("sum =", sum(product))