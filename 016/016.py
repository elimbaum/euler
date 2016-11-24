# Project Euler 16
# Digit sum of 2^1000
#
# need to do "custom" multiplication to handle the huge number
# starting with 2, build the number backwards until done (like
# school multiplication).
#
# note that python, with arbitrary precision ints, can calculate
# 2**1000 just fine.

bigNumList = [2] # start off with 2

currentExponent = 1

targetExponent = 1000


while currentExponent < targetExponent:
	# run through the number and multiply by 2
	# start at the end
	carry = 0
	for position in reversed(range(len(bigNumList))):
		digit = bigNumList[position]
		
		bigNumList[position] = digit * 2 + carry
		
		carry = 0 # reset carry
		if digit >= 5:
			# carry multiply, subtract 10
			bigNumList[position] -= 10
			
			# mark the carry variable.
			# if at the end of the number, expand the list.
			if position > 0:
				carry = 1
			else:
				bigNumList = [1] + bigNumList
			
	
	# multiply it again
	currentExponent += 1

# now we have calculated the number.

sum = 0
for d in bigNumList:
	# sum the digits
	sum += d

print(sum)
