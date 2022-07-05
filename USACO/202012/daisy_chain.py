n = int(input())
petals = [int(x) for x in input().split()]
totals = [0] * n
totals[0] = petals[0]
for i in range(1, n):
    totals[i] = totals[i-1] + petals[i]
average = {}

for i in range(n):
    for j in range(i, n):
        if i == 0:
            total = totals[j]
        else:
            total = totals[j] - totals[i - 1]
        num = j - i + 1
        if total % num == 0:
            a = total // num
            if a not in average:
                average[a] = [[i, j]]
                #print("average %d, for [%d, %d]" % (a, i, j))
            else:
                average[a].append([i, j])
                #print("average %d, for [%d, %d]" % (a, i, j))
count = 0
for i in range(n):
    p = petals[i]
    if p in average:
        intervals = average[p]
        for interval in intervals:
            if interval[0] <= i <= interval[1]:
                count += 1
                interval[1] = -1
print(count)


