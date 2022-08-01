import sys
sys.stdin = open("backforth.in", "r")
out_f = open("backforth.out", "w")
b1 = [int(x) for x in input().split()]
b2 = [int(x) for x in input().split()]

b1 = set(b1)
b2 = set(b2)
