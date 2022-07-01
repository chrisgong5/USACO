in_f = open("mowing.in", "r")
n = int(in_f.readline())
visited = False
record = {(0, 0): 0}
min_x = 10000000000
current_t = 0
x = 0
y = 0
for i in range(n):
    data = in_f.readline().split()
    direction = data[0]
    t = int(data[1])
    if direction == 'N':
        for j in range(t):
            current_t += 1
            y += 1
            if (x, y) in record:
                visited = True
                last_t = record[(x, y)]
                duration = current_t - last_t
                if duration < min_x:
                    min_x = duration
            record[(x, y)] = current_t
    elif direction == 'S':
        for j in range(t):
            current_t += 1
            y -= 1
            if (x, y) in record:
                visited = True
                last_t = record[(x, y)]
                duration = current_t - last_t
                if duration < min_x:
                    min_x = duration
            record[(x, y)] = current_t
    elif direction == 'W':
        for j in range(t):
            current_t += 1
            x -= 1
            if (x, y) in record:
                visited = True
                last_t = record[(x, y)]
                duration = current_t - last_t
                if duration < min_x:
                    min_x = duration
            record[(x, y)] = current_t
    else:
        for j in range(t):
            current_t += 1
            x += 1
            if (x, y) in record:
                visited = True
                last_t = record[(x, y)]
                duration = current_t - last_t
                if duration < min_x:
                    min_x = duration
            record[(x, y)] = current_t

out_f = open("mowing.out", "w")
if visited:
    out_f.write(str(min_x))
else:
    out_f.write("-1")
