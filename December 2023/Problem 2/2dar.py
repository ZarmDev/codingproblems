import sys

cowlistList = list(sys.stdin.read().split("\n"))
cowlist = list(cowlistList[1])
cowlist = list(map(int, cowlist))

cowlistTest = [1]*len(cowlist)
print(cowlist)
#print(cowlistTest)
nights = 0

#while cowlist != cowlistTest:
if cowlist[i] == 1 and (cowlist[i-1] == 0 or cowlist[i+1] == 0):
    if cowlist[i-1] == 0:
        cowlist[i-1] = 1
    if cowlist[i+1] == 0:
        cowlist[i+1] = 1
    nights = nights+1
        
print(cowlist)
print("Nights number is ", nights)