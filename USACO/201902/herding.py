import sys
sys.stdin = open("herding.in", "r")
out_f = open("herding.out", "w")
positions = [int(x) for x in input().split()]
min_m = 0
max_m = 0

positions.sort()
p1 = positions[0]
p2 = positions[1]
p3 = positions[2]
if p2 == p1 + 1 and p3 == p2 + 1:
    min_m = 0
    max_m = 0
elif p2 == p1 + 2 or p3 == p2 + 2:
    min_m = 1
    if p2 == p1 + 1 or p3 == p2 + 1:
        max_m = 1
    else:
        max_m = max(p3 - p2, p2 - p1) - 1
else:
    min_m = 2
    max_m = max(p3 - p2, p2 - p1) - 1

out_f.write(str(min_m) + "\n")
out_f.write(str(max_m))
