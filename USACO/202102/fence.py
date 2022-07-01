n = int(input())
for i in range(n):
    path = input()
    l = len(path)
    points = set()
    current_x = 0
    current_y = 0
    answer = "CW"
    for j in range(l):
        s = path[j]
        if s == "N":
            current_y += 1
        elif s == "S":
            current_y -= 1
        elif s == "E":
            current_x += 1
        else:
            current_x -= 1
        if (current_x, current_y) in points:
            answer = "CCW"
            break
        else:
            points.add((current_x, current_y))
    if current_x != 0 or current_y != 0:
        answer = "CCW"

    print(answer)
