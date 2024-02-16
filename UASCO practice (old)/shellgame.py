# f = open("shellgameinput.txt", "r")

# f = f.read()

# arrayOfShells = [1, 2, 3]
# print(len(f))

# organized = []
# temp = []

# for i in range(len(f)):
#     if not f[i] == '1' and not f[i] == '2' and not f[i] == '3' or i == 0:
#         continue
#     if i % 3 == 0:
#         temp.append(f[i])
#         organized.append(temp)
#         temp = []
#     else:
#         temp.append(f[i])

# print(organized)

# for i in range(len(organized)):
#     for z in range(len(organized[i]) - 1):
#         print(organized[i][z])


read = open("UASCO practice\shellgameinput.txt")

n = int(read.readline())

# shell_at_pos[i] stores the label of the shell located at position i
# The shells can be placed arbitrarily at the start.
shell_at_pos = [i for i in range(3)]

print(shell_at_pos)

# counter[i] stores the number of times the shell with label i was picked
counter = [0 for _ in range(3)]

print(counter)


for _ in range(n):
	# Zero indexing: offset all positions by 1
	a, b, g = [int(i) - 1 for i in read.readline().split()]
	print(a, b, g)
	# Perform Bessie's swapping operation
	shell_at_pos[a], shell_at_pos[b] = shell_at_pos[b], shell_at_pos[a]
	print(shell_at_pos[a], shell_at_pos[b])
	# Count the number of times Elsie guesses each particular shell
	counter[shell_at_pos[g]] += 1
	print(counter[shell_at_pos[g]], shell_at_pos[g], 'A')
print(counter)
print(max(counter), file=open("shell.out", "w"))
