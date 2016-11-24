# Project Euler Problem 15
# Lattice Paths
#
# Actually turns out to be just a clever use of Pascal's triangle.

import time
start = time.time()

print("Euler 15")

rowNumber = 3	# which row we are on of Pascal's triangle, start on 3
rowValues = (1, 2, 1) # Initialize to the 3rd row.

target = 20 # what n we are trying to compute
# this is actually the size of the grid.

while rowNumber <= target:
	newRowValues = (1,) # first value is 1
	
	# loop thru and sum (next row)
	for i in range(len(rowValues) - 1):
		newRowValues += ((rowValues[i]+rowValues[i+1]),)

	rowValues = newRowValues + (1,)
	rowNumber += 1
	

	
# the target row has been computed.
# now find the final answer
# which for the euler problem is the central value of row 2*targer
# to get this, ignore the outer values.

while len(rowValues) > 1:
	newRowValues = () # empty tuple
	for i in range(len(rowValues) - 1):
		newRowValues += ((rowValues[i]+rowValues[i+1]),)
	
	rowValues = newRowValues
	#print(rowValues)

print(rowValues[0])
print(time.time() - start)