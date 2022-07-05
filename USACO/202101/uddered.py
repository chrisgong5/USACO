letters = input()
order = {}
i = 0
for l in letters:
    order[l] = i
    i += 1
hummed = input()
count = 1
pre_order = order[hummed[0]]
l = len(hummed)
for i in range(1, l):
    a = hummed[i]
    order_a = order[a]
    if order_a <= pre_order:
        count += 1
    pre_order = order_a

print(count)
