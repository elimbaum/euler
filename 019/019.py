# Project Euler 19
# Counting Sundays
#
# The problem I was having was that I was adding on the leap year day to the beginning
# of February, NOT the end. This had the nice effect of giving one count higher, as well
# as leaving most dates untouched.


# day counter, where 1 Jan 1900 = 1
# days % 7 = day of the week (0 = sunday)
days = 1

# month lengths, days, in a non-leap year.
monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = 1 # January

year = 0 # years since 1900.

numSundays = 0

maxY = 101

while year < maxY:

    days += monthLengths[month - 1]
    month += 1
    
	# loop
    if month > 12:
        month = 1
        year += 1

    # don't count sundays in 1900
    if days % 7 == 0 and year != 0 and year < maxY:
        numSundays += 1
        #print("#", numSundays, "\t", month, "/", 1900+year, sep='')


	# take care of leap days
    # if leap year AND february AND not 1900
    #print(days)
    if year % 4 == 0 and month == 2 and year != 0:
        days += 1  # 29 days instead of 28, tack on an extra
        #print("leap; ", days)
        
print(numSundays)
