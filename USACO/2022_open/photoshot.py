# NOT DONE YET!
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


r = 0
upper = n
while upper > 0:
    max_odd = 0
    max_i = 0
    g_odd = 0
    g_even = 0
    for i in range(upper):
        if (i + 1) % 2 == 0:
            if cows[i] == "G":
                g_even += 1
            d = g_odd - g_even
            if d >= max_odd:
                max_odd = d
                max_i = i
        else:
            if cows[i] == "G":
                g_odd += 1
    if max_odd == 0:
        break
    reverse(cows, max_i)
    r += 1
    upper = max_i

print(r)

