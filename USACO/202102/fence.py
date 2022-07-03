n = int(input())
for i in range(n):
    path = input()
    l = len(path)
    current_x = 0
    current_y = 0

    for j in range(l):
        s = path[j]
        if s == "N":
            current_y += 1
            last_n = current_x
        elif s == "S":
            current_y -= 1
            last_s = current_x
        elif s == "E":
            current_x += 1
        else:
            current_x -= 1
    if last_n > last_s:
        print("CCW")
    else:
        print("CW")

