# Source: https://usaco.guide/general/io

fin = open("paint.in", "r")
fout = open("paint.out", "w")

# One way to read the file using .readline()
line1 = [int(x) for x in fin.readline().split()]
a, b = line1
line2 = [int(x) for x in fin.readline().split()]
c, d = line2
# readline() will pick up where you left off
# line2 = fin.readline()

overlap = 0

for i in range(max(a, b, c, d)):
    if (i >= a and i <= b) or (i >= c and i <= d):
        overlap += 1

print(overlap)
fout.write(str(overlap))