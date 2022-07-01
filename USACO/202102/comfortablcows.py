n = int(input())
board = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    board.append(row)

count = 0


def check(x, y):
    m = 0
    if x > 0 and board[x-1][y]:
        m += 1
    if y > 0 and board[x][y-1]:
        m += 1
    if x < n - 1 and board[x+1][y]:
        m += 1
    if y < n - 1 and board[x][y+1]:
        m += 1
    return m


for i in range(n):
    p = [int(d) for d in input().split()]
    x = p[0]
    y = p[1]
    board[x][y] = 1

    if check(x, y) == 3:
        count += 1
    if x > 0:
        u = check(x - 1, y)
        if u == 3:
            count += 1
        elif u == 4:
            count -= 1
    if y > 0:
        u = check(x, y - 1)
        if u == 3:
            count += 1
        elif u == 4:
            count -= 1
    if x < n - 1:
        u = check(x+1, y)
        if u == 3:
            count += 1
        elif u == 4:
            count -= 1
    if y < n - 1:
        u = check(x, y + 1)
        if u == 3:
            count += 1
        elif u == 4:
            count -= 1

    print(count)

