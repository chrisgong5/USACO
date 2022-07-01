# Sleeping in Class 1

T = int(input())
for t in range(T):
    n = int(input())
    a = [int(x) for x in input().split()]
    if max(a) == 0:
        print(0)
        continue
    current_v = a[0]
    current_i = 0
    current_c = 0
    i = 1
    while i < n and current_v == 0:
        current_v += a[i]
        i += 1
        current_c += 1
    current_i = i - 1

    min_c = current_c
    new_v = 0
    while i < n:
        new_v += a[i]
        if new_v == current_v:
            i += 1
            new_v = 0
        elif new_v < current_v:
            min_c += 1
            i += 1
        else:
            i = current_i + 1
            while i < n and a[i] == 0:
                current_c += 1
                i += 1

            if current_i < n:
                current_v += a[i]
                current_c += 1
            current_i = i

            min_c = current_c
            i += 1
            new_v = 0

    print(min_c)
