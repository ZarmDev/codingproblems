<<<<<<< HEAD
lines = None
with open('./1part2.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split() for line in lines]

# The Elf would first like to know which games would have been possible
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

config = {
        "red": 12,
        "blue": 14,
        "green": 13
    }
sum=0

for i in lines:
    # print('Game:', i[1][0:i[1].index(':')])
    count = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    # print(i)
    # add values in dict
    for index, value in enumerate(i):
        # if found red/blue/green add the number after
        if value.isdigit():
            color = i[index + 1]
            if ',' in color or ';' in color:
                color = color[0:-1]
            
            count[color] += int(value)

    found = False
    # iterate through each color
    for z in count:
        print(count[z], config[z])
        # find out if it fits config
        if count[z] > config[z]:
            found = True
    
    if found:
        continue

    # add up ids
    sum += int(i[1][0:i[1].index(':')])
    print(i[1][0:i[1].index(':')], sum, 'fits')

    
    
    
=======
lines = None
with open('./1part2.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split() for line in lines]

# The Elf would first like to know which games would have been possible
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

config = {
        "red": 12,
        "blue": 14,
        "green": 13
    }
sum=0

for i in lines:
    # print('Game:', i[1][0:i[1].index(':')])
    count = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    # print(i)
    # add values in dict
    for index, value in enumerate(i):
        # if found red/blue/green add the number after
        if value.isdigit():
            color = i[index + 1]
            if ',' in color or ';' in color:
                color = color[0:-1]
            
            count[color] += int(value)

    found = False
    # iterate through each color
    for z in count:
        print(count[z], config[z])
        # find out if it fits config
        if count[z] > config[z]:
            found = True
    
    if found:
        continue

    # add up ids
    sum += int(i[1][0:i[1].index(':')])
    print(i[1][0:i[1].index(':')], sum, 'fits')

    
    
    
>>>>>>> 0fff3dde763a26420bbc9da5080af7fd810f75bd
print(sum)