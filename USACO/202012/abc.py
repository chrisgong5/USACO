nums = [int(x) for x in input().split()]

nums.sort()
a = nums[0]
b = nums[1]
c = nums[6] - (a + b)
print("%d %d %d" % (a, b, c))
