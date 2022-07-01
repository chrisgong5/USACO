in_f = open("censor.in", "r")
out_f = open("censor.out", "w")

s = in_f.readline().strip()
t = in_f.readline().strip()
s_len = len(s)
t_len = len(t)
result = ""
if t_len == 0:
    out_f.write(result)
else:
    for i in range(s_len):
        # construct the result one character at one time
        result += s[i]
        r_len = len(result)
        # if the result is long enough and its end part matches t, then delete the t part
        if r_len >= t_len and t == result[r_len - t_len:]:
            result = result[0:r_len - t_len]

    out_f.write(result)
