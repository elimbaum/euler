# Euler 21
# Amicable Numbers
#
# Loop through each integer below 10000.
# Find sum of divisors.
# Lookup, if exists.
#
# As suspected, all amicable numbers must be even
# (the odds wouldn't have enough divisors because they lose out on 2)
#
# Improvements from the overview
# + only check factors up to sqrt(n). add in n and d//n
# + 

import time
startTime = time.time()

target = 10000

# use a dict to store numbers and their divisors
dictDivs = {}
totalSum = 0

n = 220 # lower bound

while n < target:
    # loop through all divisors
    sumD = 0
    d = 2
    # only check up to sqrt(n)
    while d*d <= n:
        if n % d == 0:
            # the two divisors are d and n/d
            sumD += (d + n//d)
        d += 1
        
    sumD += 1
    dictDivs[n] = sumD

    try:
        if dictDivs[sumD] == n and sumD != n:
            # add in the amicable, but not perfect numbers.
            # note that pairs only show up once. while [284] = 220 and
            # [220] = 284, 220 when 220 is reached, 284 won't be there yet.
            totalSum += (n + sumD) # count both
            print(n, sumD)
    except:
        # does not exist
        pass

    n += 2

print(totalSum)
print(time.time() - startTime)
