maxCapacity = []
initialState = []
with open('mixmilk.in') as f:
  for line in f:
    print(line, end="")
    maxCapacity.append(int(line.split(' ')[0]))
    initialState.append(int(line.split(' ')[1].replace("\n", "")))

#print(maxCapacity, initialState)

for z in range(100):
    for i in range(len(initialState)):
        if i == len(initialState) - 1:
            if initialState[i] > maxCapacity[0]:
                initialState[i] = initialState[i] - maxCapacity[0]
                initialState[0] = maxCapacity[0]
            else:
                initialState[0] = initialState[i]
                initialState[i] = 0
            print(initialState)
            continue
        if initialState[i] <= maxCapacity[i] and initialState[i + 1] + initialState[i] <= maxCapacity[i + 1]:
            initialState[i + 1] = initialState[i + 1] + initialState[i]
            initialState[i] = 0
            print(initialState)

with open("mixmilk.out", "w") as f:
    f.write('\n'.join(str(v) for v in initialState))
    f.write('\n')

#print(''.join(str(v) + '\n' for v in initialState), file=open("mixmilk.out", "w"))