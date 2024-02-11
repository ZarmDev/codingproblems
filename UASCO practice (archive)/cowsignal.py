# Enters read mode
with open('cowsignal.in') as read:
	# Splits the input by each line and assigns the first three lines to height, width and scale
	height, width, scale = map(int, read.readline().split())
	# Reads every line and stores each line to signal
	# Sample: ['XXX.\n', 'X..X\n', 'XXX.\n', 'X..X\n', 'XXX.']
	signal = [read.readline() for _ in range(height)]

'''
Sample Input:
5 4 2
XXX.
X..X
XXX.
X..X
XXX.
'''

# Enters write mode
with open('cowsignal.out', 'w') as written:
	# Loops through the new height after scaling it up (rows)
	for i in range(scale * height):
		# Loops through the new width after scaling it up (columns)
		for j in range(scale * width):
			# the floor division // rounds the result down to the nearest whole number
			# 1 // 2 == -0
			print(signal[i // scale], signal[i // scale][j // scale], j, scale, 'end=')
			# XXX. -> 'XXX.'[j // scale] which j is 1 so 1 // 2 == 0
			# j == 0 -> 0 // 2 = 0
			# j == 1 -> 1 // 2 = 0
			# j == 2 -> 2 // 2 = 1
			# j == 3 -> 3 // 2 = 1
			# so on, therefore adding each letter twice to the new signal with double the height and width
			print(signal[i // scale][j // scale], end='', file=written)
		
		print(file=written)