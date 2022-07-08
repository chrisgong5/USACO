import sys
sys.stdin = open("gymnastics.in", "r")
out_f = open("gymnastics.out", "w")

k, n = [int(x) for x in input().split()]
ranks = []
for i in range(k):
    r = {}
    rank = [int(x) for x in input().split()]
    j = 0
    for cow in rank:
        r[cow] = j
        j += 1
    ranks.append(r)

count = 0
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if ranks[0][i] < ranks[0][j]:
            x = i
            y = j
        else:
            x = j
            y = i
        consistent = True
        for m in range(1, k):
            if ranks[m][x] > ranks[m][y]:
                consistent = False
                break

        if consistent:
            count += 1
out_f.write(str(count))

