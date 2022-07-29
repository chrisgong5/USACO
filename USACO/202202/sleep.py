# Sleeping in Class 1

T = int(input())
for t in range(T):
    n = int(input())
    a = [int(x) for x in input().split()]
    max_a = max(a)
    min_a = min(a)
    # Special case: all the numbers are already the same, no need to change anything
    if max(a) == min(a):
        print(0)
        continue
    # Idea: we need to find the number X such that A can be break into several segments and each segment can be
    # summed up to X. Note that X can not be smaller than the max(A).
    # So we keep adding the numbers at the beginning of A until the sum is not smaller than max(A), try to see if
    # is the correct X. If not, adding one more and keep trying.
    current_v = a[0]
    current_i = 0
    min_first = 0
    # adding numbers until the sum is no smaller than the max(a)
    while current_i < n and current_v < max_a:
        current_i += 1
        current_v += a[current_i]
        min_first += 1

    min_c = min_first
    i = current_i + 1
    while current_i < n - 1:
        v = a[i]
        while i < n - 1 and v < current_v:
            i += 1
            v += a[i]
            min_c += 1
        if v != current_v:
            current_i += 1
            current_v += a[current_i]
            min_first += 1
            min_c = min_first
            i = current_i + 1
        else:
            if i >= n - 1:
                current_i = n
            else:
                i += 1

    print(min_c)
