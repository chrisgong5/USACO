# photoshot-3

n = int(input())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]

b_position = [0] * n
for i in range(n):
    cow = b[i] - 1
    b_position[cow] = i

min_m = 0

for current_p in range(n):
    cow = a[current_p] - 1
    final_p = b_position[cow]

    while current_p + min_m < final_p:
        min_m += 1

print(min_m)
