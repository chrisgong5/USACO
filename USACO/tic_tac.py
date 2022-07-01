in_f = open("tttt.in", "r")
board = []
for i in range(3):
    d = in_f.readline()
    board.append(d)

one_win = set()
team_win = set()
for row in range(3):
    r = {board[row][0], board[row][1], board[row][2]}
    if len(r) == 1:
        for e in r:
            one_win.add(e)
    elif len(r) == 2:
        c1 = r.pop()
        c2 = r.pop()
        x = "".join([c1, c2]) if c1 < c2 else "".join([c2, c1])
        team_win.add(x)

for col in range(3):
    c = {board[0][col], board[1][col], board[2][col]}
    if len(c) == 1:
        for e in c:
            one_win.add(e)
    elif len(c) == 2:
        c1 = c.pop()
        c2 = c.pop()
        x = "".join([c1, c2]) if c1 < c2 else "".join([c2, c1])
        team_win.add(x)

diag_1 = {board[0][0], board[1][1], board[2][2]}
if len(diag_1) == 1:
    one_win.add(diag_1.pop())
elif len(diag_1) == 2:
    c1 = diag_1.pop()
    c2 = diag_1.pop()
    x = "".join([c1, c2]) if c1 < c2 else "".join([c2, c1])
    team_win.add(x)

diag_2 = {board[0][2], board[1][1], board[2][0]}
if len(diag_2) == 1:
    one_win.add(diag_2.pop())
elif len(diag_2) == 2:
    c1 = diag_2.pop()
    c2 = diag_2.pop()
    x = "".join([c1, c2]) if c1 < c2 else "".join([c2, c1])
    team_win.add(x)

out_f = open("tttt.out", "w")
out_f.writelines(str(len(one_win)))
out_f.writelines('\n')
out_f.writelines(str(len(team_win)))
