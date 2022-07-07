import sys
import copy

sys.stdin = open("swap.in", "r")
out_f = open("swap.out", "w")

n, k = [int(x) for x in input().split()]
r1 = [int(x) for x in input().split()]
r2 = [int(x) for x in input().split()]
cows = [0] * (n + 1)
for i in range(n+1):
    cows[i] = i


# Give a list, l_cows, this function perform a reverse on
# the sub-list from index start to index end
def swap_cows(l_cows, start, end):
    while start < end:
        t = l_cows[start]
        l_cows[start] = l_cows[end]
        l_cows[end] = t
        start += 1
        end -= 1


# Key observation: if the two intervals r1 and r2 do not interact with each other,
# then ever two reverse will make the list back to its original one.
# The tricky part is that, when r1 and r2 has overlap, then when we perform reverse for r1 and r2
# certain times, it will also become the original one. So we can first try to find home many reverse of r1 and r2
# turns the list back to its original (assume it's x), then we can do y = k % x, and perform reverse on r1, r2 for
# y times.

# Make a copy of the original list
original = cows.copy()

if r1[1] < r2[0] or r1[0] > r2[1]:
    if k % 2 == 1:
        swap_cows(cows, r1[0], r1[1])
        swap_cows(cows, r2[0], r2[1])
else:
    swap_cows(cows, r1[0], r1[1])
    swap_cows(cows, r2[0], r2[1])
    x = 1
    while cows != original:
        swap_cows(cows, r1[0], r1[1])
        swap_cows(cows, r2[0], r2[1])
        x += 1
    y = k % x
    for j in range(y):
        swap_cows(cows, r1[0], r1[1])
        swap_cows(cows, r2[0], r2[1])

for i in range(1, n+1):
    out_f.write(str(cows[i])+"\n")
