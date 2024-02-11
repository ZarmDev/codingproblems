# remember to change file directory later
with open('shuffle.in') as read:
    i = 0
    for line in read:
        if i == 0:
            numberOfCows = line
        if i == 1:
            shuffle = line.replace(" ", "")
        if i == 2:
            finalPositions = line.split(' ')
        i += 1
        #print(line, end="")

with open('shuffle.out', 'w') as write:
    #print(finalPositions)
    shuffleBack = []
    # Add empty space as a placeholder for each cow in the last shuffle
    for i in range(int(numberOfCows)):
        shuffleBack.append('')
    # Loop through final positions of cows and find original postion one shuffle ago
    # 3 Shuffles
    for z in range(3):
        # Loop through cows
        for i in range(int(numberOfCows)):
            # find the index of the position the cow is at currently, since
            # indexes start from zero, and 1 to i
            shuffleBack[shuffle.index(str(i + 1))] = finalPositions[i]
            #print(shuffle, shuffle.index(i))
        #print(shuffleBack, z)
        if z == 2:
            break
        finalPositions = shuffleBack
        shuffleBack = []
        for i in range(int(numberOfCows)):
            shuffleBack.append('')
    for i in range(len(shuffleBack)):
        print(shuffleBack[i], file=write)
    #print(file=write)