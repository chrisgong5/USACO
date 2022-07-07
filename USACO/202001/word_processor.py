import sys

sys.stdin = open("word.in", "r")
out_f = open("word.out", "w")
n, k = [int(x) for x in input().split()]
words = [w for w in input().split()]
essay = []
current = words[0]
c = len(current)
for i in range(1, len(words)):
    w = words[i]
    l = len(w)
    if l + c <= k:
        current += " " + w
        c += l
    else:
        essay.append(current)
        current = w
        c = l
essay.append(current)

for row in essay:
    out_f.write(row + "\n")

