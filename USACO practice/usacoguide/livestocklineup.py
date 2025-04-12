# Setup

n = int(input())

pairone = []
pairtwo = []

for i in range(n):
    t = input().split(' ')
    first = t[0]
    second = t[len(t) - 1]
    pairone.append(first)
    pairtwo.append(second)

# first sort the names by alphabetical order
sortedarr = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
newarr = sortedarr.copy()
prevlocations = []
prevlocations2 = []

# then, go through that array and fulfill the constraints given
for i in range(len(sortedarr)):
    # if name is in pair one
    if sortedarr[i] in pairone:
        location = pairone.index(sortedarr[i])
        print(sortedarr[i], pairtwo[location])
        # either place before or after, first try before
        # check first if the location will obstruct a item previously placed
        if newarr[location - 1] in prevlocations:
            # then try location afterwards
            newarr.insert(location + 1, pairtwo[location])
        else:
            newarr.insert(location, pairtwo[location])
    # if name is in pair two
    elif sortedarr[i] in pairtwo:
        pass

print(newarr)
