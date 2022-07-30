import sys
sys.stdin = open("shell.in", "r")
out_f = open("shell.out", "w")
n = int(input())
guesses = [0, 0, 0, 0]
# This list remembers where each initial position will be after each swap
current = [0, 1, 2, 3]
for i in range(n):
    data = [int(x) for x in input().split()]
    exchange = [data[0], data[1]]
    guess = data[2]
    t = current[exchange[0]]
    current[exchange[0]] = current[exchange[1]]
    current[exchange[1]] = t
    # increase the score for the correct initial position
    guesses[current[guess]] += 1

# figure out which initial position has the highest score
max_s = 0
for i in range(1, 4):
    if guesses[i] > max_s:
        max_s = guesses[i]

out_f.write(str(max_s))

