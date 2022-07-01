n = int(input())
A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]
a_pos = {}
b_pos = {}

for i in range(n):
    a_pos[A[i]] = i
    b_pos[B[i]] = i

# Idea: just look at the first no-in-position cow and move those that should be
# in front of this one. Mark those that have been moved to 0 in A.
count = 0
a = A[0]
current = 0

for i in range(n):
    if a != B[i]:
        count += 1
        b = B[i]
        a_p = a_pos[b]
        A[a_p] = 0
    else:
        current += 1
        while current < n and A[current] == 0:
            current += 1
        if current < n:
            a = A[current]

print(count)

