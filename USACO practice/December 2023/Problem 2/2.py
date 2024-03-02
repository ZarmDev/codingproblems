import sys

# Time complexity: O(2(2^n) * m^2) plus potentially O(n) for the min function
# Very inefficient

# fin = open("December 2023\Problem 2\cowntacttracing.in", 'r')
# fout = open("December 2023\Problem 2\cowntacttracing.out", "w")

n = int(sys.stdin.readline())
# print(n)
finalState = list(sys.stdin.readline().replace('\n', ''))
# print(finalState)

possible_states = []

## Get every possible binary value
# 2 ** n - O(2^n)
for i in range(2 ** n):
    # Neat binary trick
    possibleval = format(i, '0' + str(n) + 'b')
    # Make sure there is infected in it (All of these initial states contain at least one infected cow.)
    if ('1' in possibleval):
        possible_states.append(possibleval)
    

# print(possible_states)
mincows = []
filled = ['1'] * n

## O(2^n) - looping through every possible state which is length of O(2^n)
for item in possible_states:
    # Setup
    possible_state = list(item)
    night = -1
    cows = 0
    quitLoop = False

    # Get amount infected before doing virus simulation
    # O(m)
    for i in possible_state:
        if i == '1':
            cows += 1

    # print(possible_state, finalState)

    # Usually takes about 10 times worst case (O(1))
    while (possible_state != finalState):
        # If it didn't work, just break
        if possible_state == filled:
            quitLoop = True
            break
    
        night += 1
        ## O(m)
        for index in range(len(possible_state)):
            if possible_state[index] == '1':
                # print('in')
                # if out of bounds (positive)
                if (index + 1) == (len(possible_state)):
                    # print('1')
                    possible_state[index - 1] = '1'
                # if out of bounds (negative)
                elif (index - 1) == -1:
                    # print('2')
                    possible_state[index + 1] = '1'
                else:
                    # print('3')
                    possible_state[index + 1] = '1'
                    possible_state[index - 1] = '1'
        
    
    # If the possible state aligns with the final state,
    # then add min cows to array
    if quitLoop == False:
        # appending takes O(1) in average time but worst case O(n)
        mincows.append(cows)
    
sys.stdout.write(str(min(mincows)))
# fout.write(str(min(mincows)))