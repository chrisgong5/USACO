import sys
sys.stdin = open("whereami.in", "r")
out_f = open("whereami.out", "w")

n = int(input())
colors = input()
k = 1
success = False
while not success:
    book = set()
    success = True
    for i in range(n - k + 1):
        if colors[i: i + k] in book:
            success = False
            break
        else:
            book.add(colors[i:i+k])
    if not success:
        k += 1
out_f.write(str(k))
