n = int(input())
east_cows = []
north_cows = []

for i in range(n):
    data = input().split()
    direction = data[0]
    x = int(data[1])
    y = int(data[2])
    # each cow will be recorded as a 4-element list, coordinators, id, and where it is blocked
    # For cows moving north, put its x first, so we can sort the north cows according to their x
    # and for cows moving east, put its y first.
    if direction == "N":
        north_cows.append([x, y, i, 0])
    else:
        east_cows.append([y, x, i, 0])
north_cows.sort()
east_cows.sort()

result = ["Infinity"] * n

for n_cow in north_cows:
    for e_cow in east_cows:
        # if either cow has been blocked, then go to the next pair
        if e_cow[3] > 0 or n_cow[3] > 0:
            continue
        # check to see if one can block the other
        if n_cow[1] < e_cow[0] and n_cow[0] > e_cow[1]:
            if e_cow[0] - n_cow[1] < n_cow[0] - e_cow[1]:
                e_cow[3] = n_cow[0]
                result[e_cow[2]] = n_cow[0] - e_cow[1]
            elif n_cow[0] - e_cow[1] < e_cow[0] - n_cow[1]:
                n_cow[3] = e_cow[0]
                result[n_cow[2]] = e_cow[0] - n_cow[1]
for r in result:
    print(r)


















