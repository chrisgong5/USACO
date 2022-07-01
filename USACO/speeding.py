import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

inputs = iter(sys.stdin.readlines())

n, m = map(int, next(inputs).split())

limit = []
bessie = []

for i in range(n):
    a, b = map(int, next(inputs).split(' '))
    limit.extend([b] * a)

for j in range(m):
    c, d = map(int, next(inputs).split(' '))
    bessie.extend([d] * c)

print(max(0, max(list(map(lambda x, y: x - y, bessie, limit)))))
