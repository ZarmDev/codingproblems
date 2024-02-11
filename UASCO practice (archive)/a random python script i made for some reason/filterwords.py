listofWords = []

with open('10000 words.txt', encoding="utf8") as f:
  for line in f:
    listofWords.append(line.replace('\n', ''))
    #print(line, end="")
#print(listofWords)

allLines = []

with open('data.txt', encoding="utf8") as f2:
  for line in f2:
    try:
      for i in line.split(' '):
        if i != '' and i != '\n':
          allLines.append(i)
    except:
      pass

listofHardwords = []

for z in allLines:
  if not z in listofWords:
    listofHardwords.append(z)

with open("datafrompy.txt", "w") as output_file:
  output_file.write(str(listofHardwords))