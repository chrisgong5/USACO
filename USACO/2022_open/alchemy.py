# NOT DONE YET!
n = int(input())
metals = [int(x) for x in input().split()]
k = int(input())
recipes = {}
triggers = {}

for i in range(k):
    d = [int(y) for y in input().split()]
    l = d[0]
    m = d[1]
    components = tuple(d[2:])
    recipes[components] = [l, 0]
got_new = True
while got_new:
    got_new = False
    for k, v in recipes.items():
        if v[1] == 1:
            continue
        l = v[0]
        min_unit = n
        for c in k:
            if metals[c-1] == 0:
                min_unit = 0
                break
            else:
                if metals[c-1] < min_unit:
                    min_unit = metals[c-1]

        if min_unit > 0:
            metals[l-1] += min_unit
            v[1] = 1
            got_new = True

print(metals[n-1])


        

