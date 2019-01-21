n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

v1 = sum(data)
v2 = sum(data) / n

print("{0:0.1f}".format(v2))
