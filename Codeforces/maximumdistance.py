# Source: https://usaco.guide/general/io
import math

n = int(input())

xcords = list(map(int, input().split()))
ycords = list(map(int, input().split()))

# distance formula: sqrt((x2-x1)^2+(y2-y1)^2))

highest = 0

for i in range(n):
    # not overcounting here...
    for z in range(i + 1, n): # start from i + 1 instead of 0
        x2 = xcords[i]
        x1 = xcords[z]
        y2 = ycords[i]
        y1 = ycords[z]

        highest = max((((x2-x1) ** 2) + ((y2-y1) **2)), highest)

print(highest)