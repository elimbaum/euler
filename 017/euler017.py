# Project Euler 17
#
# Number letter counts
#
# originally, actually used strings. for speed, now only adds the length of the string.

upperLimit = 1000

digitLengths = [3, # one
                3, # two
                5, # three
                4, # four
                4, # five
                3, # six
                5, # seven
                5, # eight
                4] # nine

teenLengths = [3, # ten
               6, # eleven
               6, # twelve
               8, # thirteen
               8, # fourteen
               7, # fifteen
               7, # sixteen
               9, # seventeen
               8, # eighteen
               8] # nineteen

decadeLengths = [0,	# ten itself is in the teens.
              	 6, # twenty
              	 6, # thirty
              	 5, # forty
              	 5, # fifty
             	 5, # sixty
              	 7, # seventy
              	 6, # eighty
            	 6] # ninety

wordLength = 0

for n in range(1, upperLimit):
    numString = str(n).zfill(3) # fill with zeroes

    # check hundreds place
    if numString[-3] != '0':
        wordLength += digitLengths[int(numString[-3]) - 1] + 7 # 'hundred'

    # check for 'and' - if hundreds is not zero, and both ones and tens are not zero.
    if numString[-3] != '0' and (numString[-2] != '0' or numString[-1] != '0'):
        wordLength += 3 # 'and'

    # check tens place
    if numString[-2] > '1':
        wordLength += decadeLengths[int(numString[-2]) - 1]
        
    # teens
    if numString[-2] == '1':
        wordLength += teenLengths[int(numString[-1])]
        continue # skip the ones
                             

    # check ones place
    if numString[-1] != '0':
        wordLength += digitLengths[int(numString[-1]) - 1]
    
    #print(wordLength)
    
# now add 1000
wordLength += 11 # one thousand
        
print(wordLength)
