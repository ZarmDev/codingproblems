<<<<<<< HEAD
lines = None
with open('./1.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split() for line in lines]

sum = 0

for i in lines:
    current = ''
    for letter in i[0]:
        if letter.isdigit():
            current += letter

    if current != '':
        print(current[0], current[-1])
        sum += int(str(current[0]) + str(current[-1]))
    


print(sum)

=======
lines = None
with open('./1.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split() for line in lines]

sum = 0

for i in lines:
    current = ''
    for letter in i[0]:
        if letter.isdigit():
            current += letter

    if current != '':
        print(current[0], current[-1])
        sum += int(str(current[0]) + str(current[-1]))
    


print(sum)

>>>>>>> 0fff3dde763a26420bbc9da5080af7fd810f75bd
