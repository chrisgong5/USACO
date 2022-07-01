input_file = "block.in"
f = open(input_file, "r")
data = f.readlines()
n = int(data[0])
blocks = []
for i in range(1, len(data)):
    line = data[i]
    c = 0
    front = []
    back = []
    while line[c] != ' ':
        front.append(line[c])
        c += 1

    c += 1
    while line[c] <= 'z' and line[c] >= 'a':
        back.append(line[c])
        c += 1
    block = [front, back]
    blocks.append(block)

global_count = [0]*26

for i in range(n - 1):
    front = blocks[i][0]
    back = blocks[i][1]
    for j in range(n):
        if j == i:
            continue


        
