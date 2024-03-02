with open("blist.in") as read:
	n = int(read.readline())
	cows = [[int(i) for i in read.readline().split()] for _ in range(n)]

print(n, cows)

bucket_dictionary = {}
each_cow = {}
highest = 0

# fill up dictionary
for i in range(11):
	bucket_dictionary[i] = 'available'

for count, item in enumerate(cows):
	each_cow[count] = item
	# startimes.append(i[0])
	# endtimes.append(i[1])
	# bucketsneeded.append(i[2])
	if item[1] > highest:
		highest = item[1]

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

# each second, check with each cow at a time
for currenttime in range(highest + 1):
	for count, item in enumerate(dict.items(each_cow)):
		starttimes = item[1][0]
		endtimes = item[1][1]
		bucketsneeded = item[1][2]
		#  if the start time is currenttime
		# print(currenttime, startimes)
		if currenttime == starttimes:
			# print(count, currenttime, starttimes)
			# which cow are we talking about?
			cowNumber = count
			# find available buckets
			# print(dict.values(bucket_dictionary))
			# print(bucketsneeded)
			for i in range(bucketsneeded):
				availablelocation = available_buckets(bucket_dictionary)
				# allocate buckets to cow number
				bucket_dictionary[availablelocation] = 'in-use'
		maxatthistime = max_buckets_needed(bucket_dictionary)
		# print(currenttime, maxatthistime)
		max_buckets = max(max_buckets, maxatthistime)

	print(currenttime, bucket_dictionary)

	for count, item in enumerate(dict.items(each_cow)):
		starttimes = item[1][0]
		endtimes = item[1][1]
		bucketsneeded = item[1][2]
		if currenttime == endtimes:
				# which cow are we talking about?
				cowNumber = count
				# find available buckets
				for i in range(bucketsneeded):
					availablelocation = used_buckets(bucket_dictionary)
					# allocate buckets to cow number
					bucket_dictionary[availablelocation] = 'available'

	print(currenttime, bucket_dictionary)

print(max_buckets)
# print(max_buckets, file=open("blist.out", "w"))

# Copilot code:
# with open("blist.in") as read:
#     n = int(read.readline())
#     cows = sorted([[int(i) for i in read.readline().split()] for _ in range(n)])

# buckets_in_use = 0
# max_buckets = 0

# events = []
# for start, end, buckets in cows:
#     # Positive buckets to allocate to them
#     events.append((start, buckets))
#     # Its -buckets because its the buckets that we remove when we are done
#     events.append((end, -buckets))

# # In the format of: (start, end)
# # Events: [(2, 2), (6, -2), (4, 1), (10, -1), (8, 3), (13, -3)]
# # print(events)

# # _, change: 2 2
# # basically, _ ignores the first item and then sets change to the second item
# # the first item is the starttime and the second is the buckets that we can remove
# # we ignore it because we sorted the events and only need the relative positions
# for _, change in sorted(events):
#     # Interestingly, the previous loop ensures that there is the starttime
#     # to add buckets and endtime to remove it so it just adds by the change
#     buckets_in_use += change
#     # print(buckets_in_use)
#     # This is just like a "high score" variable
#     max_buckets = max(max_buckets, buckets_in_use)
#     # print(max_buckets)

# # print(max_buckets, file=open("blist.out", "w"))