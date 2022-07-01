n = int(input())

comfortable = [int(x) for x in input().split()]
current = [int(x) for x in input().split()]

command_count = 0
i = 0

while i < n:
    if comfortable[i] == current[i]:
        while i < n and comfortable[i] == current[i]:
            i += 1
    elif comfortable[i] > current[i]:
        c = comfortable[i] - current[i]
        j = i
        while j < n and comfortable[j] > current[j]:
            tmp = comfortable[j] - current[j]
            if tmp < c:
                c = tmp
            j += 1
        for k in range(i, j):
            current[k] += c
        command_count += c
    else:
        c = current[i] - comfortable[i]
        j = i
        while j < n and comfortable[j] < current[j]:
            temp = current[j] - comfortable[j]
            if temp < c:
                c = temp
            j += 1
        command_count += c
        for k in range(i, j):
            current[k] -= c
            
print(command_count)



