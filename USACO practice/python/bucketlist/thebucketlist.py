with open("blist.in") as read:
	n = int(read.readline())
	cows = [[int(i) for i in read.readline().split()] for _ in range(n)]

print(n, cows)

bucket_dictionary = {}

# fill up dictionary
for i in range(11):
	bucket_dictionary[i] = 'available'

highest = 0
startimes = []
endtimes = []
bucketsneeded = []

for i in cows:
	startimes.append(i[0])
	endtimes.append(i[1])
	bucketsneeded.append(i[2])
	if i[1] > highest:
		highest = i[1]

print(highest)

buckets_used = []

def available_buckets(dictionarygiven):
	for count, item in enumerate(dict.values(dictionarygiven)):
		# print(count, item, 't')
		if item == 'available':
			return count

def used_buckets(dictionarygiven):
	for count, item in enumerate(dict.values(dictionarygiven)):
		# print(count, item, 't')
		if item == 'in-use':
			return count

def max_buckets_needed(dictionarygiven):
	needed = 0
	for count, item in enumerate(dict.values(dictionarygiven)):
		# print(count, item, 't')
		if item == 'in-use':
			needed += 1
	return needed

max_buckets = 0

for currenttime in range(highest):
	#  if the start time is currenttime
	# print(currenttime, startimes)
	if currenttime in startimes:
		# which cow are we talking about?
		cowNumber = startimes.index(currenttime)
		# find available buckets
		# print(dict.values(bucket_dictionary))
		for i in range(bucketsneeded[cowNumber]):
			availablelocation = available_buckets(bucket_dictionary)
			# allocate buckets to cow number
			bucket_dictionary[availablelocation] = 'in-use'
	if currenttime in endtimes:
		# which cow are we talking about?
		cowNumber = endtimes.index(currenttime)
		# find available buckets
		for i in range(bucketsneeded[cowNumber]):
			availablelocation = used_buckets(bucket_dictionary)
			# allocate buckets to cow number
			bucket_dictionary[availablelocation] = 'available'
	maxatthistime = max_buckets_needed(bucket_dictionary)
	print(currenttime, maxatthistime, bucket_dictionary)
	if maxatthistime > max_buckets:
		max_buckets = maxatthistime

print(max_buckets, file=open("blist.out", "w"))
