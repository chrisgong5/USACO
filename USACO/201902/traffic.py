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
            high -= l
    elif mark == "none":
        if low >= 0:
            low = max(low, l)
            high = min(high, h)
        else:
            low = l
            high = h
    else:
        print("Error: invalid mark %s" % mark)
    measures.append([low, high])

end_low = low if low >= 0 else 0
end_high = high if high >= 0 else 0
off_measure = str(end_low) + " " + str(end_high)

# Going backward to fill the entry traffic measures
i = n - 1
while i >= 0:
    mark = traffic[i][0]
    l = traffic[i][1]
    h = traffic[i][2]
    if mark == "on":
        low -= l
        high -= h
        x = min(low, high)
        y = max(low, high)
        low = x
        high = y
        """
        if low < 0:
            low = 0
        if high < 0:
            high = 0
        """
    elif mark == "off":
        low += h
        high += l
        x = min(low, high)
        y = max(low, high)
        low = x
        high = y
    elif mark == "none":
        low = max(low, l)
        high = min(high, h)
    else:
        print("Error: invalid mark %s" % mark)

    #if measures[i-1][0] >= 0:
    #    low = max(low, measures[i-1][0])
    #    high = min(high, measures[i-1][1])
    i -= 1

entry_low = low if low >= 0 else 0
entry_high = high if high >= 0 else 0
if entry_low > entry_high:
    entry_low = entry_high
entry_measure = str(entry_low) + " " + str(entry_high) + "\n"
out_file.write(entry_measure)
out_file.write(off_measure)




