# Given the great list, less list, and a position, p, this function counts the liars
def check_liars(great_l, less_l, p):
    m = len(great_l)
    l = len(less_l)
    i = 0
    while i < l and p > less_l[i]:
        i += 1
    x = i
    i = m - 1
    while i >= 0 and p < great_l[i]:
        i -= 1
    x += m - i - 1
    return x


n = int(input())
less_p = []
great_p = []
all_p = []
for i in range(n):
    d = input().split()
    r = d[0]
    p = int(d[1])
    all_p.append(p)
    if r == "L":
        less_p.append(p)
    else:
        great_p.append(p)

less_p.sort()
great_p.sort()
all_p.sort()
min_l = n

# The idea is to check all the possible positions for the one that produces minimum liars
for i in range(n):
    p = all_p[i]
    liars = check_liars(great_p, less_p, p)
    if liars < min_l:
        min_l = liars

print(min_l)







