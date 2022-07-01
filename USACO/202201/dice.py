T = int(input())


# return 1 if A beats B, -1 if B beats A, 0 if tire
def beat(A, B):
    a = 0
    b = 0
    for x in A:
        for y in B:
            if x > y:
                a += 1
            elif y > x:
                b += 1
    if a == b:
        return 0
    if a > b:
        return 1
    return -1


for i in range(T):
    data = [int(x) for x in input().split()]
    A = data[0:4]
    B = data[4:8]
    r = beat(A, B)
    solution = False

    if r != 0:
        for x in range(1, 11):
            if solution:
                break;
            for y in range(1, 11):
                if solution:
                    break
                for z in range(1, 11):
                    if solution:
                        break
                    for u in range(1, 11):
                        C = [x, y, z, u]
                        if (r == 1 and beat(B, C) == 1 and beat(C, A) == 1) or (
                            r == -1 and beat(A, C) == 1 and beat(C, B) == 1):
                            solution = True
                            break
    if solution:
        print("yes")
    else:
        print("no")



