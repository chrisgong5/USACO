n = int(input())
for i in range(n):
    path = input()
    l = len(path)
    current_x = 0
    current_y = 0
    max_n = 0
    max_s = 0
    for j in range(l):
        s = path[j]
        if s == "N":
            current_y += 1
            if current_x > max_n:
                max_n = current_x
        elif s == "S":
            current_y -= 1
            if current_x > max_s:
                max_s = current_x
        elif s == "E":
            current_x += 1
        else:
            current_x -= 1
    if max_n > max_s:
        print("CCW")
    else:
        print("CW")

