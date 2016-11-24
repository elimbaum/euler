# Project Euler 14
# Longest Collatz Sequence
#
# >> 1 is fast integer div 2.

import time
start = time.time()

UPPER_BOUND = 1000000	# 1 million, per the problem description

starter = UPPER_BOUND >> 1	# start at the halfway point (500k)

# make starer odd if its even
if starter % 2 == 0:
	starter += 1
	
recordSteps = 0
recordNumber = None # stores the record number

while starter < UPPER_BOUND:
	steps = 0
	x = starter
	
	while x > 1:
		if x % 2 == 0:	# even
			x >>= 1
		else: # odd
			x = (3*x + 1) >> 1	# both odd and even rules
			steps += 1 # so add an extra step
			
		steps += 1
		
	# x is now 1, all done with that starter.
	# check record
	if steps > recordSteps:
		recordSteps = steps
		recordNumber = starter
	
	# next number
	# actually, from the forum: only check odds.
	starter += 2
	

print(recordNumber, "has", recordSteps, "steps.")

print(time.time() - start)