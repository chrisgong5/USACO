# NOT DONE YET!
T = int(input())
for t in range(T):
    n = int(input())
    a = [int(x) for x in input().split()]
    same = False
    min_c = 0
    while not same:
        l = len(a)
        max_a = a[0]
        max_i = 0
        for i in range(l):
            if a[i] > max_a:
                max_a = a[i]
                max_i = i
        if max_a == 0:
            same = True
        v = 0
        b = []
        for i in range(max_i):
            v += a[i]
            if v > max_a:
                b.append(v)
                b = b + a[i+1:]
                a = b
                break
            elif v == max_a:
                b.append(v)
                v = 0
        if v < max_a:
            pass

    print(min_c)
