import sys
sys.stdin = open("sleepy.in", "r")
out_f = open("sleepy.out", "w")

n = int(input())
p = [int(x) for x in input().split()]
# Append n + 1 to the end so don't need to deal with the spacial case for i = n - 1
p.append(n + 1)
i = n - 1
first = p[0]
moves = 0

# The idea: for each cow in the first position, need to decide where it should be moved to.
# We start looking from the end, set i = n - 1. Two cases:
# 1. if first > p[i], we definitely need to move first after p[i], just look each of the cows after i and
#    move first to the correct position
# 2. if p[i] is out of order, we need to move first after p[i] to expose p[i] so we can move p[i]
#    to its correct position
while i > 0:
    if first > p[i]:
        moves += 1
        j = n
        while first < p[j]:
            j -= 1
        p.insert(j + 1, first)
        p.pop(0)
        first = p[0]
    elif p[i] > p[i+1]:
        moves += 1
        p.insert(i+1, first)
        p.pop(0)
        first = p[0]
    else:
        i -= 1
out_f.write(str(moves))


