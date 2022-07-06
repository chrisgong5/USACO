import sys
sys.stdin = open("swap.in", "r")
out_f = open("swap.out", "w")

n, k = [int(x) for x in input().split()]
r1 = [int(x) for x in input().split()]
r2 = [int(x) for x in input().split()]
cows = [0] * (n + 1)
for i in range(n+1):
    cows[i] = i


def swap_cows(l_cows, start, end):
    while start < end:
        t = l_cows[start]
        l_cows[start] = l_cows[end]
        l_cows[end] = t
        start += 1
        end -= 1


if k % 2 == 1:
    swap_cows(cows, r1[0], r1[1])
    swap_cows(cows, r2[0], r2[1])

for i in range(1, n+1):
    out_f.write(str(cows[i])+"\n")
