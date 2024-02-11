import sys

n = int(sys.stdin.readline())
finalState = list(sys.stdin.readline().replace('\n', ''))

possible_states = []
# possible_states = ['00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110']

for i in range(2 ** n):
    possibleval = format(i, '0' + str(n) + 'b')
    if ('1' in possibleval):
        possible_states.append(possibleval)

# print(possible_states)
# exit()

mincows = []
filled = ['1'] * n

for item in possible_states:
    possible_state = list(item)
    cows = 0
    quitLoop = False

    for i in possible_state:
        if i == '1':
            cows += 1
    # In the old code, the problem was here...
    while (possible_state != finalState):
        if possible_state == filled:
            quitLoop = True
            break

        next_state = possible_state.copy()
        # The way of checking is correct here.
        for index in range(len(possible_state)):
            if possible_state[index] == '1':
                if index > 0:
                    next_state[index - 1] = '1'
                if index < len(possible_state) - 1:
                    next_state[index + 1] = '1'
        possible_state = next_state

    if quitLoop == False:
        # The lowest possible cows is 1, so you can just exit anyways
        if cows == 1:
            sys.stdout.write(str(cows))
            exit()
        mincows.append(cows)

sys.stdout.write(str(min(mincows)))