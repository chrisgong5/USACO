# blocks

n = int(input())
blocks = []
for i in range(4):
    blocks.append(input())

words = []
for i in range(n):
    words.append(input())

block_records = [[0]*26, [0]*26, [0]*26, [0]*26]

for i in range(4):
    for j in range(6):
        block_records[i][ord(blocks[i][j]) - ord('A')] = 1


def four_spell_one(c1):
    for k in range(4):
        if block_records[k][c1] == 1:
            return True
    return False


def three_spell_one(c1, b1, b2, b3):
    return block_records[b1][c1] == 1 or block_records[b2][c1] == 1 or block_records[b3][c1] == 1


def two_spell_one(c1, b1, b2):
    return block_records[b1][c1] == 1 or block_records[b2][c1] == 1

def two_spell_two(c1, c2, b1, b2):
    return (block_records[b1][c1] == 1 and block_records[b2][c2] == 1) or (block_records[b2][c1] == 1 and block_records[b1][c2] == 1)

def four_spell_two(c1, c2):
    if block_records[0][c1] == 1 and three_spell_one(c2, 1, 2, 3):
        return True
    if block_records[1][c1] == 1 and three_spell_one(c2, 0, 2, 3):
        return True
    if block_records[2][c1] == 1 and three_spell_one(c2, 0, 1, 3):
        return True
    if block_records[3][c1] == 1 and three_spell_one(c2, 0, 1, 2):
        return True

    return False


def three_spell_two(c1, c2, b1, b2, b3):
    if block_records[b1][c1] == 1 and two_spell_one(c2, b2, b3):
        return True
    if block_records[b2][c1] == 1 and two_spell_one(c2, b1, b3):
        return True
    if block_records[b3][c1] == 1 and two_spell_one(c2, b1, b2):
        return True
    return False


def four_spell_three(c1, c2, c3):
    if block_records[0][c1] == 1 and three_spell_two(c2, c3, 1, 2, 3):
        return True
    if block_records[1][c1] == 1 and three_spell_two(c2, c3, 0, 2, 3):
        return True
    if block_records[2][c1] == 1 and three_spell_two(c2, c3, 0, 1, 3):
        return True
    if block_records[3][c1] == 1 and three_spell_two(c2, c3, 0, 1, 2):
        return True
    return False


def four_spell_four(c1, c2, c3, c4):
    if two_spell_two(c1, c2, 0, 1) and two_spell_two(c3, c4, 2, 3):
        return True
    if two_spell_two(c1, c2, 0, 2) and two_spell_two(c3, c4, 1, 3):
        return True
    if two_spell_two(c1, c2, 0, 3) and two_spell_two(c3, c4, 1, 2):
        return True
    if two_spell_two(c1, c2, 1, 2) and two_spell_two(c3, c4, 0, 3):
        return True
    if two_spell_two(c1, c2, 1, 3) and two_spell_two(c3, c4, 0, 2):
        return True
    if two_spell_two(c1, c2, 2, 3) and two_spell_two(c3, c4, 0, 1):
        return True
    return False


for i in range(n):
    word = words[i]
    s = len(word)
    if s == 1:
        k = ord(word[0]) - ord('A')
        if not four_spell_one(k):
            print("NO")
        else:
            print("YES")
    elif s == 2:
        k1 = ord(word[0]) - ord('A')
        k2 = ord(word[1]) - ord('A')
        if not four_spell_two(k1, k2):
            print("NO")
        else:
            print("YES")
    elif s == 3:
        k1 = ord(word[0]) - ord('A')
        k2 = ord(word[1]) - ord('A')
        k3 = ord(word[2]) - ord('A')
        if not four_spell_three(k1, k2, k3):
            print("NO")
        else:
            print("YES")
    else:
        k1 = ord(word[0]) - ord('A')
        k2 = ord(word[1]) - ord('A')
        k3 = ord(word[2]) - ord('A')
        k4 = ord(word[3]) - ord('A')
        if not four_spell_four(k1, k2, k3, k4):
            print("NO")
        else:
            print("YES")
