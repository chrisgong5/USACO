# photoshot-5

n = int(input())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
a_position = [0] * n
for i in range(n):
    cow = a[i] - 1
    a_position[cow] = i


b_position = [0] * n
for i in range(n):
    cow = b[i] - 1
    b_position[cow] = i

min_m = 0
shift_m = 0

for i in range(n):
    cow = b[i] - 1
    a_p = a_position[cow]
    if a_p < 0:
        shift_m -= 1
    else:
        if a_p + shift_m > i:
            min_m += 1
            shift_m += 1
            a_position[cow] = -1

print(min_m)
