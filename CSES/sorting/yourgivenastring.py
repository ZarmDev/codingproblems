# Source: https://usaco.guide/general/io

strInput = input()
# make sure the string itself doesn't also get included
uniqueOccurances = []

# first find the longest substring
# one way is just get all unique occurances and attempt to split the string by those occurances

for i in range(len(strInput)):
	for z in range(len(strInput)):
		occurance = strInput[z:len(strInput)]
		if not occurance in uniqueOccurances and occurance != strInput:
			uniqueOccurances.append(occurance)
		# print(strInput[z:len(strInput)])

for z in range(len(strInput)):
	occurance = strInput[z]
	if not occurance in uniqueOccurances:
		uniqueOccurances.append(occurance)
	# print(strInput[z:len(strInput)])

print(uniqueOccurances)

highscore = 0
highestAmount = ''

for i in uniqueOccurances:
	timesappeared = strInput.count(i)
	print(i, timesappeared)
	if timesappeared > highscore:
		highscore = timesappeared
		highestAmount = i

# must be atleast 2
if highscore >= 2:
	print(highscore)
else:
	print(0)

# then find the count the amount fo that substring
