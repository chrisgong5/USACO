import sys
sys.stdin = open("lineup.in", "r")
out_f = open("lineup.out", "w")
cows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
relation = {}
result = []
n = int(input())
for i in range(n):
    r = input().split()
    cow1 = r[0]
    cow2 = r[5]
    if cow1 in relation:
        relation[cow1].append(cow2)
        if cow2 in cows:
            cows.remove(cow2)
    elif cow2 in relation:
    else:
        relation[cow1] = [cow2]
        if cow1 in cows:
            cows.remove(cow1)
        if cow2 in cows:
            cows.remove(cow2)
ones = [[x] for x in cows]
threes = []
twos = []
for c, neighbors in relation.items():
    l = len(neighbors)
    print("cow %s has %d neighbors" % (c, l))
    if l == 1:
        c1 = min(c, neighbors[0])
        c2 = max(c, neighbors[0])
        x = [c1, c2]
        twos.append(x)
    else:
        c1 = min(neighbors[0], neighbors[1])
        c2 = max(neighbors[0], neighbors[1])
        x = [c1, c, c2]
        k = len(threes)
        for i in range(k):
            if threes[i][0] == c1:
                threes[i].insert(0, c)
                threes[i].insert(0, c2)
                break
            elif threes[i][0] == c2:
                threes[i].insert(0, c)
                threes[i].insert(0, c1)
                break
            elif threes[i][-1] == c1:
                threes[i].append(c)
                threes[i].append(c2)
                break
            elif threes[i][-1] == c2:
                threes[i].append(c)
                threes[i].append(c1)
                break
            elif threes[i][0] > c1:
                threes.insert(i, x)
                break
        if i == k:
            threes.append(x)
twos.sort()
for e in ones:
    print(e[0] + " ")
print("\n")
for e in twos:
    print("%s %s" % (e[0], e[1]))
i = 0
j = 0
k = 0
l1 = len(ones)
l2 = len(twos)
l3 = len(threes)
#print("l3: %d, l2: %d" % (l3, l2))
while i < l1 and j < l2 and k < l3:
    x = ones[i][0]
    y = twos[j][0]
    z = threes[k][0]
    min_e = min([x, y, z])
    if x == min_e:
        for e in ones[i]:
            result.append(e)
        i += 1
    elif y == min_e:
        for e in twos[j]:
            result.append(e)
        j += 1
    else:
        for e in threes[k]:
            result.append(e)
        k += 1
if i < l1 and j < l2:
    u = ones
    v = twos
    u_i = i
    v_i = j
elif i < l1 and k < l3:
    u = ones
    v = threes
    u_i = i
    v_i = k
    l2 = l3
else:
    u = twos
    v = threes
    u_i = j
    v_i = k
    l1 = l2
    l2 = l3
while u_i < l1 and v_i < l2:
    if u[u_i][0] < v[v_i][0]:
        for e in u[u_i]:
            result.append(e)
        u_i += 1
    else:
        for e in v[v_i]:
            result.append(e)
        v_i += 1
while u_i < l1:
    for e in u[u_i]:
        result.append(e)
    u_i += 1
while v_i < l2:
    for e in v[v_i]:
        result.append(e)
    v_i += 1

for e in result:
    out_f.write(e + "\n")
