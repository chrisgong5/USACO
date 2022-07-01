# photoshot-4

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

for current_p in range(n):
    cow = a[current_p] - 1
    if cow < 0:
        shift_m -= 1
    else:
        final_p = b_position[cow]
        k = current_p
        while current_p + shift_m < final_p:
            min_m += 1
            shift_m += 1
            b_cow = b[k] - 1
            a[a_position[b_cow]] = -1
            k += 1

print(min_m)
