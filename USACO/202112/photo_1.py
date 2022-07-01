n = int(input())
cows = input()

# The idea is to group the same type of cows as segment and then look at the first 3 segments.
# For example, if we have GGHGHGGGHH, then we have 6 segments and the first 3 are:
# GG H G
# Key observation: no cow in the first segment may form a throwable photo with any cow in the fourth segment since
# that will have at least 2 G and 2 H. So we can just look at the first 3 segments and calculate all throwable photos
# that involves at least one cow from the first segment.
# To do that, we don't care the type of each segment, just the length. So for the example above, we have
# 2, 1, 1,
# Two cases,
# 1. the second segment (the middle one) has only one cow. To form a throwable photo with at least one cow from
# the first segment, we have len_of_seg1 * (len_of_seg2 + 1) - 1
# Note that we could pick 0 cow from segment 2, that's why we have len_of_seg2 + 1. Finally, we need to delete the
# one photo that only have one cow from seg1 and 0 cow from seg2 (it has only two cows).
# 2. the second segment has more than one cow. We can use the first cow in seg2 to form throwable photos with cows
# in seg1, totally len_of_seg1 - 1. Similarly, use the last cow in seg1 to form throwable photos with cows in seg2,
# len_of_seg2 -1.
# After this, we can safely disregard the first segment, and get another 3 segments by add the fourth segments, then
# perform the same computation as in above.
# After iterating over all cows, we have either 2 or 3 segments left. If 3 segments left, we need to calculate
# the throwable photos formed by cows in seg2 and seg3.

throw_n = 0
current_v = cows[0]
current_c = 1
segments = [0, 0, 0]
current_s = 0

for i in range(1, n):
    if cows[i] == current_v:
        current_c += 1
    else:
        if current_s < 2:
            segments[current_s] = current_c
            current_s += 1
        else:
            segments[2] = current_c
            if segments[1] == 1:
                throw_n += segments[0] * (segments[2] + 1) - 1
            else:
                throw_n += segments[0] - 1
                throw_n += segments[1] - 1
            segments[0] = segments[1]
            segments[1] = segments[2]
            current_s = 2
        current_v = cows[i]
        current_c = 1

if current_s == 1:
    segments[1] = current_c
    throw_n += segments[0] - 1 + segments[1] - 1
elif current_s == 2:
    segments[2] = current_c
    if segments[1] == 1:
        throw_n += (segments[0] + 1) * (segments[2] + 1) - 3
    else:
        throw_n += segments[0] - 1
        throw_n += 2 * (segments[1] - 1)
        throw_n += segments[2] - 1

print(throw_n)
