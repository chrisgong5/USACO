n = int(input())
cows = [c for c in input()]


def reverse(l_cows, end):
    start = 0
    while start < end:
        t = l_cows[start]
        l_cows[start] = l_cows[end]
        l_cows[end] = t
        start += 1
        end -= 1


book = [0]*n
g_even = 0
g_odd = 0
i = 0
while i < n:
    # print("cows at %d" % i)
    if cows[i] == "H":
        if (i+1) % 2 == 0:
            book[i] = (g_even, g_odd)
    else:
        if (i+1) % 2 == 0:
            g_even += 1
            book[i] = (g_even, g_odd)
        else:
            g_odd += 1

    i += 1

j = n - 1 if n % 2 == 0 else n - 2
r = 0
while j > 0:
    if (r % 2 == 0 and book[j][1] > book[j][0] and cows[j] == "H") or (r % 2 == 1 and book[j][0] > book[j][1] and cows[j] == "H"):
        reverse(cows, j)
        r += 1
    j -= 2

print(r)

