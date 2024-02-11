# first, read the input
'''
6
011101
'''

n = int(input())
finalState = list(input().replace('\n', ''))

# assume 11111 has an answer of 1 to prevent problems
if (not '0' in finalState):
    print(1)

# then, simulate all clumps going backwards:
# count the amount of "occurances" or clumps
# then, reverse engineer the center of the clump
# or, on odd 1's, you can ASSUME they are neccesary since lone 1's have not "expanded"

# ok, now, go through each possible occurance and de-expand the clump (n + 1, n - 1)
# when, all the clumps are now lone 1's and there are only lone 1's, expand every single one
# until the list looks like '11111'
# then, count the number of nights it took

# 001001 - 0 night
# we are trying to get 011101
# if we attempted this, it would be 011111
# then 111111
# SO, it's impossible to get that night and the original number of cows is correct

# in the case of say, 110111
# we deexpand and get 100010
# then, we try to expand the clumps
# In one night we get 110111
# Therefore, it takes 1 night
# Also, mathematically, 110111 is gonna be '11' and '111' where '11' takes one night 
# (Since it's odd, 2 infected / 2 = 1 and since it's not a float, no need to round, but it would be rounded
# up if neccesary)
# And '111' takes one night (Since it's odd, 3 infected / 2 = 1.5 and rounded down is 1)

# in the case of multiple 1's like: 11111110111100
# we count the clump of '1111111' and since it's 7, it has to be '0111110' and then '0011100' and so on
# it takes 1 -> '0111110' 2-> '0011100' 3-> '0001000' [3 NIGHTS]
# so generally, on uneven clumps, you can say 7/2=3.5 and round down to 3
# therefore, we can generalize it as amountofinfected/2 rounded down