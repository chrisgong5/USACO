answer = []
guess = []
a_count = [0]*26
g_count = [0]*26

for i in range(3):
    answer.append(input())
    for c in answer[i]:
        a_count[ord(c) - ord("A")] += 1

for i in range(3):
    guess.append(input())
    for c in guess[i]:
        g_count[ord(c) - ord("A")] += 1

yellow = 0
green = 0

for i in range(3):
    for j in range(3):
        a = answer[i][j]
        g = guess[i][j]
        if a == g:
            index = ord(a) - ord("A")
            green += 1
            a_count[index] -= 1
            g_count[index] -= 1

for i in range(26):
    yellow += min(a_count[i], g_count[i])

print(green)
print(yellow)

