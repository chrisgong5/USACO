import sys
sys.stdin = open("race.in", "r")
out_f = open("race.out", "w")
k, n = [int(x) for x in input().split()]

for i in range(n):
    x = int(input())
    current = 0
    trip = k
    count = 0
    speed = current + 1

