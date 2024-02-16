lines = None
with open('./2.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split() for line in lines]

sum = 0
valid = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numberCorresponding = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in lines:
    print('-------------------------------')
    print(i[0])
    # just getting the current line
    remainingFragments = i[0]
    current = ''
    combinedNumberWords = []

    # get first number
    combine = ''
    for z in range(len(remainingFragments)):
        combine += remainingFragments[z]
        # we found the first number!
        print(combine, valid)
        for count, eachvalidword in enumerate(valid):
            # if number in fragment
            eachvalidnumber = str(numberCorresponding[count])
            # print(eachvalidword, eachvalidword in combine)
            if eachvalidnumber in combine:
                print('v2', combine.index(eachvalidnumber), f"valid.index({combine[combine.index(eachvalidnumber):combine.index(eachvalidnumber)]} + {len(eachvalidnumber)}")
                # if it can find the word in the fragment
                if combine.index(eachvalidnumber) != -1:
                    combinedNumberWords.append(eachvalidnumber)
                    combine = ''
            # if number word in fragment
            elif eachvalidword in combine:
                print('v', combine.index(eachvalidword))
                # if it can find the word in the fragment
                if combine.index(eachvalidword) != -1:
                    combinedNumberWords.append(str(numberCorresponding[valid.index(combine[combine.index(eachvalidword):combine.index(eachvalidword) + len(eachvalidword)])]))
                    combine = ''

    print(combinedNumberWords, 'c')
    print('test', combinedNumberWords[0] + combinedNumberWords[-1])
    sum += int(combinedNumberWords[0] + combinedNumberWords[-1])

    
print(sum)