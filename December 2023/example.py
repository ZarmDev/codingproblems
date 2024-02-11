with open("speeding.in") as read:
	road_seg_num, speed_seg_num = [int(i) for i in read.readline().split()]
	limit_segs = [
		[int(i) for i in read.readline().split()] for _ in range(road_seg_num)
	]

	bessie_segs = [
		[int(i) for i in read.readline().split()] for _ in range(speed_seg_num)
	]

limit = []
for s in limit_segs:
	for _ in range(s[0]):
		limit.append(s[1])
bessie = []
for s in bessie_segs:
	for _ in range(s[0]):
		bessie.append(s[1])

worst = 0
for a, b in zip(limit, bessie):
	worst = max(worst, b - a)
print(worst, file=open("speeding.out", "w"))