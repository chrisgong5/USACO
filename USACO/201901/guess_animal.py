import sys
sys.stdin = open("guess.in", "r")
out_f = open("guess.out", "w")
n = int(input())
max_x = 0
groups = []
animals = {}
for i in range(n):
    animal = input().split()
    name = animal[0]
    groups.append(name)
    k = int(animal[1])
    animals[name] = []
    for j in range(2, k + 2):
        feature = animal[j]
        animals[name].append(feature)


def guess(group, m):
    global max_x, animals
    if len(group) == 1:
        if m > max_x:
            max_x = m
    else:
        features = set()
        for a in groups:
            for f in animals[a]:
                features.add(f)
        for f in features:
            new_group = []
            for a in group:
                if f in animals[a]:
                    new_group.append(a)
            guess(new_group, m + 1)


guess(groups, 0)
out_f.write(str(max_x))

