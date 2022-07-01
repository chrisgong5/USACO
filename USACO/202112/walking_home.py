T = int(input())


# Use a recursive function to solve the problem:
# If we are at point (i, j), either from left (row == True) or above (row == False), using no more than k turn,
# How many paths to the destination?
# To save time, we also use a dict (book) to remember the points that we already reached in the same way (left or above)
board = []
book = {}


def paths(i, j, n, k, row):
    if board[i][j] == "H":
        return 0
    if i == n - 1 and j == n - 1:
        return 1
    if row and i < n - 1 and k == 0:
        return 0
    if (not row) and j < n - 1 and k == 0:
        return 0
    if (i, j, k, row) not in book:
        down = 0
        right = 0
        if i < n - 1:
            u = k - 1 if row else k
            down = paths(i + 1, j, n, u, False)
        if j < n - 1:
            u = k if row else k - 1
            right = paths(i, j + 1, n, u, True)
        book[(i, j, k, row)] = down + right
    return book[(i, j, k, row)]


for t in range(T):
    y = [int(x) for x in input().split()]
    n = y[0]
    k = y[1]
    board = []
    for i in range(n):
        board.append(input().strip())
    book = {}
    c1 = paths(0, 1, n, k, True)
    c2 = paths(1, 0, n, k, False)
    print(c1 + c2)
