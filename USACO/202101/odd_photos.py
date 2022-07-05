N = int(input())
ids = [int(x) for x in input().split()]
odd = 0
even = 0
for i in ids:
    if i % 2 == 1:
        odd += 1
    else:
        even += 1
count = 0
if even == odd:
    count = 2 * even
elif even > odd:
    count = 2 * odd + 1
else:
    count = 2*even
    odd = odd - even
    addition = odd // 3
    rem = odd % 3
    if rem == 1:
        addition -= 1
        count += 2 * addition + 1
    elif rem == 2:
        count += 2 * addition + 1
    else:
        count += 2 * addition
print(count)


