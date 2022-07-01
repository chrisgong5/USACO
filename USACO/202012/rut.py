n = int(input())
max_x = 0
max_y = 0
east_cows = []
north_cows = []
x_lines = []
y_lines = []
cows = []
grid = {}
for i in range(n):
    data = input().split()
    direction = data[0]
    x = int(data[1])
    if x > max_x:
        max_x = x
    y = int(data[2])
    if y > max_y:
        max_y = y
    cows.append([direction, x, y])
    grid[(x, y)] = [(0, i)]
    if direction == "N":
        x_lines.append(x)
        north_cows.append([x, y, i])
    else:
        y_lines.append(y)
        east_cows.append([x, y, i])
x_lines.sort()
y_lines.sort()

result = ["Infinity"] * n

for cow in north_cows:
    x = cow[0]
    y = cow[1]
    for y_line in y_lines:
        if y_line > y:
            step = y_line - y
            if (x, y_line) in grid:
                grid[(x, y_line)].append((step, cow[2]))
            else:
                grid[(x, y_line)] = [(step, cow[2])]

for cow in east_cows:
    x = cow[0]
    y = cow[1]
    for x_line in x_lines:
        if x_line > x:
            step = x_line - x
            if (x_line, y) in grid:
                grid[(x_line, y)].append((step, cow[2]))
            else:
                grid[(x_line, y)] = [(step, cow[2])]

for k, cow in grid.items():
    x = k[0]
    y = k[1]
    cow.sort()
    step_0 = cow[0][0]
    cow_0 = cow[0][1]
    for i in range(1, len(cow)):
        step_i = cow[i][0]
        cow_i = cow[i][1]
        c = cows[cow_i]
        d = c[0]
        m = 0
        if d == "N":
            m = y - c[2]
        else:
            m = x - c[1]

        if step_0 < step_i:
            if result[cow_i] == "Infinity" or result[cow_i] > m:
                result[cow_i] = m

for r in result:
    print(r)











