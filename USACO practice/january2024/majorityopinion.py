# Source: https://usaco.guide/general/io

amountoftestcases = int(input())

for i in range(amountoftestcases):
	lengthOfList = int(input())
	cows = list(map(int, input().split()))
	# print(cows)
	dictOfOccurances = [0] * (lengthOfList + 1)
	indexesOfOccuranceStarts = [0] * (lengthOfList + 1)

	splitter = -1
	temp = []
	# z is index
	for z in range(lengthOfList):
		# print(temp, z)
		if splitter != cows[z]:
			if z == 0:
				dictOfOccurances[cows[z]] = 1
				indexesOfOccuranceStarts[cows[z]] = z
				continue
			if z == lengthOfList - 1:
				dictOfOccurances[cows[z]] = 1
				indexesOfOccuranceStarts[cows[z]] = z
				# print(len(temp), dictOfOccurances[int(splitter)], splitter, z)
			# if this clump is larger than the last
			# print(temp, cows[z], z)
			if len(temp) > dictOfOccurances[int(splitter)]:
				dictOfOccurances[int(splitter)] = len(temp)
				indexesOfOccuranceStarts[int(splitter)] = len(temp)
			temp = []
			splitter = cows[z]
		
		temp.append(cows[z])
	
	highScore = 0
	highestIndex = 0
	for j in range(len(dictOfOccurances)):
		if j > highScore:
			highScore = dictOfOccurances[j]
			print(j)
			highestIndex = j
	print(highestIndex)
	

	# print(indexesOfOccuranceStarts)

	# get amount of occurances for each
	# for z in range(lengthOfList):
	# 	# count amount of certain occurance
	# 	amount = cows.count(z)
	# 	if amount != 0:
	# 		dictOfOccurances[str(z)] = amount
	
	# print(dictOfOccurances)

	# # highest amount of occurances
	# highest = 0
	# val = 0
	# for x in dict.items(dictOfOccurances):
	# 	# print(x)
	# 	if x[1] > highest:
	# 		highest = x[1]
	# 		val = x[0]
	# 	elif x[1] == highest:
	# 		val = -1
	
	# print(val)


