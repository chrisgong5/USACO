import sys
sys.stdin = open("lineup.in", "r")
out_f = open("lineup.out", "w")
cows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]

n = int(input())
for i in range(n):
    r = input().split()
