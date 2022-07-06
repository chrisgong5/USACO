import sys
sys.stdin = open("triangles.in", "r")
out_f = open("triangles.out", "w")

n = int(input())
x_p = {}
y_p = {}

for i in range(n):
    p = [int(x) for x in input().split()]
    x = p[0]
    y = p[1]
    if x in x_p:
        x_p[x].append(y)
    else:
        x_p[x] = [y]
    if y in y_p:
        y_p[y].append(x)
    else:
        y_p[y] = [x]

max_a = 0
for x in x_p:
    x_p[x].sort()
for y in y_p:
    y_p[y].sort()

for x in x_p:
    for y in x_p[x]:
        if y not in y_p:
            continue
        h = max(y - x_p[x][0], x_p[x][-1] - y)
        xs = y_p[y]
        for x2 in xs:
            l = x2 - x if x2 >= x else x - x2
            a = h*l
            if a > max_a:
                max_a = a
out_f.write(str(max_a))



