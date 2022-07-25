import sys
sys.stdin = open("revegetate.in", "r")
out_f = open("revegetate.out", "w")
parm = input().split()
n = int(parm[0])
m = int(parm[1])
for i in range(n):
    p = [int(x) for x in input().split()]

