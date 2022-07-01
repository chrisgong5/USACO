import sys

sys.stdin = open('measurement.in', 'r')
sys.stdout = open('measurement.out', 'w')

n = int(input())
changes = 0
data = {}
my_cows = {"Bessie": 7,
           "Mildred": 7,
           "Elsie": 7}

for i in range(n):
    day, cow, out = input().split()
    data[int(day)] = [cow, int(out)]

display = set({"Bessie", "Mildred", "Elsie"})
days = sorted(list(data.keys()))
changes = 0

for i in days:
    x = data[i]
    my_cows[x[0]] += x[1]
    max_v = max(my_cows.values())
    new_display = set()
    for cow in my_cows:
        if my_cows[cow] == max_v:
            new_display.add(cow)
    if new_display != display:
        changes += 1
    display = new_display

print(changes)
