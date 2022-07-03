n = int(input())
# The idea is to use a dict as the board and the tuple of coordinators (x, y) as the key.
# The value of the dict is a list of two values, first value could be 0 or 1 to indicate if that position has been taken
# The second value could be 0, 1, 2, 3, 4, indicating the neighbors.
# When a position (x, y) has a vlue, [1, 3], it is a comfortable cow. Note that if the value is [1, 4], we need to
# decrease the number of comfortable cows by one.
board = {}
count = 0

for i in range(n):
    q = [int(d) for d in input().split()]
    x = q[0]
    y = q[1]
    p = x, y
    if p not in board:
        board[p] = [1, 0]
    else:
        board[p][0] += 1
        if board[p][1] == 3:
            count += 1
    if x > 0:
        key = (x - 1, y)
        if key not in board:
            board[key] = [0, 1]
        else:
            elem = board[key]
            elem[1] += 1
            if elem[0] == 1:
                if elem[1] == 3:
                    count += 1
                elif elem[1] == 4:
                    count -= 1
    if x < n - 1:
        key = (x + 1, y)
        if key not in board:
            board[key] = [0, 1]
        else:
            elem = board[key]
            elem[1] += 1
            if elem[0] == 1:
                if elem[1] == 3:
                    count += 1
                elif elem[1] == 4:
                    count -= 1
    if y > 0:
        key = (x, y - 1)
        if key not in board:
            board[key] = [0, 1]
        else:
            elem = board[key]
            elem[1] += 1
            if elem[0] == 1:
                if elem[1] == 3:
                    count += 1
                elif elem[1] == 4:
                    count -= 1
    if y < n - 1:
        key = (x, y + 1)
        if key not in board:
            board[key] = [0, 1]
        else:
            elem = board[key]
            elem[1] += 1
            if elem[0] == 1:
                if elem[1] == 3:
                    count += 1
                elif elem[1] == 4:
                    count -= 1

    print(count)

