in_file = open("traffic.in", "r")
out_file = open("traffic.out", "w")

data = in_file.readlines()
n = int(data[0])
measure = []
for i in range(1, n + 1):
    line = data[i].split()
    measure.append(line)

entry = [-1, -1]
current = [-1, -1]
on_and_off = [0, 0]
for i in range(n):
    mode = measure[0]
    r = [int(measure[1]), int(measure[2])]
    if mode == "on":
        if current[0] != -1:
            current[0] += r[0]
            current[1] += r[1]
        else:
            on_and_off = [on_and_off[0] + r[0], on_and_off[1] + r[1]]
    elif mode == "off":
        if current[0] != -1:
            current[1] -= r[0]
        else:
            on_and_off = [on_and_off[0], on_and_off[1] - r[0]]
    else:
        current = [r[0], r[1]]
        if entry[0] == -1:
            entry = [current[0] - r[0], current[1] - r[1]]


