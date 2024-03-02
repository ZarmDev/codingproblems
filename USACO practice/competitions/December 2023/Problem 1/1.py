import sys

n, m = [int(i) for i in sys.stdin.readline().split()]
# print(n, m)

initialCowHeights = list(map(int, sys.stdin.readline().split()))

# print(initialCowHeights)

candyHeights = list(map(int, sys.stdin.readline().split()))

# print(candyHeights)

candyCanesLeft = 0
cowInLine = 0

## Base case: Until the candy canes left is zero
# MAKE SURE NOT TO CHANGE CANDYHEIGHTS
overflow = 0

currentCandyCane = [0, candyHeights[candyCanesLeft]]

while candyCanesLeft < len(candyHeights):
    overflow += 1
    if overflow > 20:
        break

    # reset currentcow every turn
    currentCow = initialCowHeights[cowInLine]

    print(currentCandyCane, currentCow, 'cowline', cowInLine)
    '''if the currentcow is taller than the candy canes initial height
      minus it's current height then add to cows height '''
    if currentCow > (currentCandyCane[0]):
        # remove from candy cane
        currentCandyCane[0] += currentCow
        # if the first y value passes the second
        if (currentCandyCane[0] > currentCandyCane[1]):
            candyCanesLeft += 1
            currentCow += currentCandyCane[1]
            print('prevcane', currentCandyCane)
            print(candyCanesLeft, candyHeights)
            if candyCanesLeft == len(candyHeights):
                initialCowHeights[cowInLine] = currentCow
                break
            # reset candy cane
            currentCandyCane = [0, candyHeights[candyCanesLeft]]
        else:
            currentCow += currentCow
    
    # if the currentcow is not tall enough, do nothing
    initialCowHeights[cowInLine] = currentCow
    print('keep track', initialCowHeights)
    # reset cowInLine variable every cycle
    if cowInLine >= len(initialCowHeights) - 1:
        cowInLine = 0
    else:
        cowInLine += 1

print(initialCowHeights)