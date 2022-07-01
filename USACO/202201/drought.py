T = int(input())

# Key observation: the first cow has to eat together with the second cow
# If the second cow is less hungry than the first cow, then there is no way we can make them the same.
# Otherwise, try to see if it's possible to bring the second cow to the same level by feeding it together with
# the third, and so on.
for i in range(T):
    n = int(input())
    h = [int(x) for x in input().split()]
    min_l = h[0]

    count = 0
    j = 1
    while j < n:
        # print("j=%d, h[j-1]=%d, h[j]=%d" % (j, h[j-1], h[j]))
        if h[j-1] < min_l:
            min_l = h[j-1]
        if h[j] < h[j-1]:
            count = -1
            break
        elif h[j] == h[j-1]:
            j += 2
            continue
        else:
            d = h[j] - h[j-1]
            if j + 1 >= n or h[j+1] < d:
                count = -1
                break
            count += 2*d
            h[j] -= d
            h[j+1] -= d
            j += 2
    if j == n:
        if h[j-1] > h[j-2]:
            count = -1
        else:
            min_l = min(min_l, h[j-1])

    if count == -1:
        print(-1)
    else:
        for j in range(n):
            count += h[j] - min_l
        print(count)



