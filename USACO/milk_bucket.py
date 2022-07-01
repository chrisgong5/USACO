input_data = open("blist.in", "r")
n = int(input_data.readline())
start=[]
end=[]

data=[]
for i in range(n):
    l = [int(x) for x in input_data.readline().split()]
    start.append([l[0], l[2]])
    end.append([l[1], l[2]])
start.sort()
end.sort()

max_b = start[0][1]
current_b = max_b
end_i = 0
for i in range(1, n):
    current_b += start[i][1]
    while start[i][0] > end[end_i][0]:
        current_b -= end[end_i][1]
        end_i += 1
    if current_b > max_b:
        max_b = current_b

out_d = open("blist.out", "w")
out_d.write(str(max_b))
