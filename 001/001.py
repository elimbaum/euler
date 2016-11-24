#! /usr/bin/env python3.3

"""
Project Euler problem 001
Multiples of 3 and 5

by Eli Baum
14 April 2013

----------------------------

Adds all multiples of 3 and 5 less then an integer.

"""

from sys import exit

print("Project Euler problem 001\n\
Multiples of 3 and 5")

n = int(input("n = ")) # Program will sum all multiples less than n.


"""
I found (through regression) that the sum of all multiples of 3 and 5 less than
n closely follows the quadratic equation

(7*n^2 - 15*n)/30

If n is a multiple of 15, the equation is exactly correct. Therefore, the
program will first get close to n with the quadratic, then add the remaining
few values to the sum.

"""

n_floor = (n // 15) * 15  # Floor to the nearest multiple of 15

sum = int((7 * (n_floor ** 2) - 15 * n_floor) / 30)  # Use the quadratic

if n_floor == n:  # n was a multiple of 15; all done.
    print(sum)
    exit()

sum += n_floor # Add in the multiples of 15 that the quadratic doesn't count.

""" The differences between multiples of 3 and 5 follow this pattern:
    3, 2, 1, 3, 1, 2, 3
    I will use that to get to n from n_floor
    
    """

diffs = [3, 2, 1, 3, 1, 2, 3]

for i in diffs:
    
    if (n - n_floor) <= i:  # All multiples have been summed; Done.
        print(sum)
        exit()

    n_floor += i
    sum += n_floor
