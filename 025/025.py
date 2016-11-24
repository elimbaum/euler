# Euler 025
# 1000-digit Fibonacci number
#
# Rather than using the recursive relation, use the fact that
# F_n = round(phi ^ n / sqrt(5))
# and then logarithms (to get number of digits)

from math import *
from time import *

a = time()

phi = (1 + sqrt(5)) / 2

# Desired number of digits
digits = 1000

r = ceil((digits - 1 + log10(5) / 2) / log10(phi))

b = time()

print(r) #"is", round(phi ** r / sqrt(5)))

print(b - a)
