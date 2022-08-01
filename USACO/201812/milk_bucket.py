input_f = open("blist.in", "r")
data = input_f.readlines()
n = int(data[0])

max_t = 0
intervals = []

for i in range(1, n + 1):
    d = [int(x) for x in data[i].split(' ')]
    intervals.append(d)
    if d[1] > max_t:
        max_t = d[1]

times = [0] * (max_t + 1)

for i in range(n):
    d = intervals[i]
    for j in range(d[0], d[1] + 1):
        times[j] += d[2]

result = max(times)
output_f = open("blist.out", "w")
output_f.write(str(result))
