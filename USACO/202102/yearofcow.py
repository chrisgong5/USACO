n = int(input())
zodiac = {"Ox": 0, "Tiger": 1, "Rabbit": 2, "Dragon": 3,
          "Snake": 4, "Horse": 5, "Goat": 6, "Monkey": 7,
          "Rooster": 8, "Dog": 9, "Pig": 10, "Rat": 11}
relation = {"Bessie": "Ox"}
positions = {"Bessie": 0}

for i in range(n):
    x = input().split()
    cow1 = x[0]
    cow2 = x[7]
    y = x[3]
    z = x[4]

    relation[cow1] = z

    cow2_p = positions[cow2]
    cow2_z = relation[cow2]
    cow2_z_p = zodiac[cow2_z]
    cow1_z_p = 12 if zodiac[z] == 0 else zodiac[z]

    if y == "previous":
        d = cow2_z_p - cow1_z_p if cow2_z_p > cow1_z_p else 12 - cow1_z_p + cow2_z_p
        p = cow2_p - d
    else:
        d = cow1_z_p - cow2_z_p if cow1_z_p > cow2_z_p else 12 - cow2_z_p + cow1_z_p
        p = cow2_p + d
    positions[cow1] = p

answer = positions["Elsie"] if positions["Elsie"] > 0 else 0 - positions["Elsie"]
print(answer)


