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
    recipes[components] = l

got_new = True
while got_new:
    got_new = False
    pass
        

