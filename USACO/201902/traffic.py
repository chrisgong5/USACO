# NOT DONE YET!
import sys
sys.stdin = open("traffic.in", "r")
out_file = open("traffic.out", "w")
n = int(input())

traffic = []
for i in range(n):
    data = [x for x in input().split()]
    mark = data[0]
    low = int(data[1])
    high = int(data[2])
    traffic.append([mark, low, high])

measures = []
# Going forward first, not going to have measure before the first "none" segment
low = -1
high = -1
for i in range(n):
    mark = traffic[i][0]
    l = traffic[i][1]
    h = traffic[i][2]
    if mark == "on":
        if low >= 0:
            low += l
            high += h
    elif mark == "off":
        if low >= 0:
            low -= h
            if low < 0:
                low = 0
            high -= l
            if high < 0:
                high = 0
    else:
        if low >= 0:
            low = max(low, l)
            high = min(high, h)
        else:
            low = l
            high = h
    measures.append([low, high])

off_measure = str(low) + " " + str(high)

# Going backward to fill the entry traffic measures
i = n - 1
while i > 0:
    mark = traffic[i][0]
    l = traffic[i][1]
    h = traffic[i][2]
    if mark == "on":
        low -= l
        high -= h
        if low < 0:
            low = 0
        if high < 0:
            high = 0
    elif mark == "off":
        low += h
        high += l
    else:
        low = max(low, l)
        high = min(high, h)
    #if measures[i-1][0] > 0:
    #    low = max(low, measures[i-1][0])
    #if measures[i-1][1] > 0:
    #    high = min(high, measures[i-1][1])
    i -= 1
mark = traffic[0][0]
l = traffic[0][1]
h = traffic[0][2]
if mark == "on":
    low -= l
    high -= h
    if low < 0:
        low = 0
    if high < 0:
        high = 0
elif mark == "off":
    low += h
    high += l
else:
    low = max(low, l)
    high = min(high, h)

entry_measure = str(low) + " " + str(high) + "\n"

out_file.write(entry_measure)
out_file.write(off_measure)




