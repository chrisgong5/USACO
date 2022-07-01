n = int(input())
p = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]
count = 0
last_c = 0
# Just iterate through the p and t,
# Change the t to match the p and remember the change (increased x, or decreased x)
# Then for the next p and t, try to see if we can use the previous change.
for i in range(n):
    # print("step : = %d, p = %d, t = %d" % (i, p[i], t[i]))
    current_d = p[i] - t[i]
    if current_d > 0:
        if last_c >= current_d:
            last_c = current_d
        else:
            count += min(current_d, current_d - last_c)
            last_c = current_d
    elif current_d < 0:
        if last_c <= current_d:
            last_c = current_d
        else:
            count += min(-current_d, last_c - current_d)
            last_c = current_d
        # print("case 1, count = %d, total_change = %d" % (count, total_change))
    else:
        last_c = 0
        continue

print(count)

