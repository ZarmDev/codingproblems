# Source: https://usaco.guide/general/io

n, m, k = map(int, input().split())

allOf = []

for j in range(m + 1):
	original = input()
	new = ''
	for i in original:
		for z in range(k):
			new += i
	
	for z in range(k):
		allOf.append(new)

for i in allOf:
	print(i)