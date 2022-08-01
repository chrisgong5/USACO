import sys
sys.stdin = open("mixmilk.in", "r")
out_f = open("mixmilk.out", "w")
b1 = [int(x) for x in input().split()]
b2 = [int(x) for x in input().split()]
b3 = [int(x) for x in input().split()]

for i in range(1, 101):
    k = i % 3
    if k == 1:
        # b1 -> b2
        room = b2[0] - b2[1]
        if room >= b1[1]:
            b2[1] += b1[1]
            b1[1] = 0
        else:
            b2[1] = b2[0]
            b1[1] -= room
    elif k == 2:
        # b2 -> b3
        room = b3[0] - b3[1]
        if room >= b2[1]:
            b3[1] += b2[1]
            b2[1] = 0
        else:
            b3[1] = b3[0]
            b2[1] -= room
    else:
        # b3 -> b1
        room = b1[0] - b1[1]
        if room >= b3[1]:
            b1[1] += b3[1]
            b3[1] = 0
        else:
            b1[1] = b1[0]
            b3[1] -= room
out_f.write(str(b1[1]) + "\n")
out_f.write(str(b2[1]) + "\n")
out_f.writelines(str(b3[1]))
