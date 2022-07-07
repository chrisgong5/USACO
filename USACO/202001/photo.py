import sys
sys.stdin = open("photo.in", "r")
out_f = open("photo.out", "w")

n = int(input())
B = [int(x) for x in input().split()]
A = [0] * n

# The idea is to decide how to break b1 into a1 and a2, once this is done correctly, the rest will be determined
# To make the minimum permutation, we will want to try the smallest a1 possible.
# So we start by assuming a1 = 1, and a2 = b1 - 1, etc.
# During the process, we need to make sure: A is a permutation (each number can only occur once, no negative values)
# If this checking fails, try the next break-up from b1
j = 1
while j > 0:
    used = set()
    A[0] = j
    rem = B[0] - j
    used.add(j)
    success = True
    for i in range(1, n - 1):
        if rem in used:
            success = False
            break
        A[i] = rem
        used.add(rem)
        rem = B[i] - A[i]
        if rem <= 0:
            success = False
            break
    if success:
        A[n-1] = rem
        break
    j += 1

out_f.write(str(A[0]))
for i in range(1, n):
    out_f.write(" " + str(A[i]))



