def solve():
    # B -> cost to not exceed (above the line)
    # N -> Number of buildings
    [B, N] = input().split(' ')
    B = int(B)
    N = int(N)

    if N == 0:
        print(0)
        return

    allDangers = []
    allHeights = []
    allCosts = []

    # s is building heights
    S = input().split(' ')
    S = list(map(int, S))
    # Get the max of the S array
    # Loop from 0 to the max of S
    # Call the loop var the bridge
    for bridgeLine in range(max(S) + 1):
        danger = 0
        cost = 0
        # Within this loop, loop through each value of S
        for buildingheight in S:
            difference = (bridgeLine - buildingheight)
            # if the difference is positive, add that to the danger variable
            if difference > 0:
                danger += difference
            # if it's negative, add that to the cost variable
            elif difference < 0:
                cost -= difference
        # print(danger, cost)
        # at the end of the loop from 0 to max S, check if the cost doesn't exceed B
        if cost <= B:
            # print(bridgeLine, danger, cost)
            # if so, then add the danger to the allDangers
            allDangers.append(danger)
            allHeights.append(bridgeLine)
            allCosts.append(cost)
    
    smallestCost = max(allCosts)
    indexOfCost = None
    # print(allCosts, allDangers, allHeights)
    # get all the smallest danger values
    for i in range(len(allDangers)):
        if min(allDangers) == allDangers[i]:
            cost2 = allCosts[i]
            # print(cost2, smallestCost)
            # check if the cost is smaller than the smallest cost
            if cost2 < smallestCost:
                smallestCost = cost2
                indexOfCost = i
            elif cost2 == smallestCost and indexOfCost == None:
                smallestCost = cost2
                indexOfCost = i
    print(allHeights[indexOfCost])

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
