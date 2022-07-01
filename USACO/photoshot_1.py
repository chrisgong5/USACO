# photoshot-1

n = int(input())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
b_position = [0] * n
for i in range(n):
    cow = b[i] - 1
    b_position[cow] = i

min_m = 0

for current_position in range(n - 1):
    cow = a[current_position] - 1
    final_position = b_position[cow]
    while current_position + min_m < final_position:
        min_m += 1

print(min_m)


