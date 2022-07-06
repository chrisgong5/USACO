import sys
sys.stdin = open("breedflip.in", "r")
out_f = open("breedflip.out", "w")
n = int(input())
A = input()
B = input()

count = 0
i = 0
while i < n:
    while i < n and A[i] == B[i]:
        i += 1
    if i < n:
        count += 1
    while i < n and A[i] != B[i]:
        i += 1
out_f.write(str(count))




