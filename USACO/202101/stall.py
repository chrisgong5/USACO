n = int(input())
cows = [int(x) for x in input().split()]
stalls = [int(x) for x in input().split()]

cows.sort()
stalls.sort()

count = 1

for i in range(1, n):
    cow = cows[i]
    j = i
    x = 0
    while j >= 0 and stalls[j] >= cow:
        x += 1
        j -= 1
    count *= x
print(count)
