n = int(input())
data = []
for n in range(n):
    t_str, p_str = input().split()
    t = int(t_str)
    p = int(p_str)
    data.append((t, p))

data.sort()

# print(data)

data2 = zip(data, data[1:])

data3 = []
for p1, p2 in data2:
    delta_t = p2[0] - p1[0]
    delta_p = p2[1] - p1[1]
    v = abs(delta_p / delta_t)
    data3.append(v)

res = max(data3)
print(res)
