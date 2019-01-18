# j5  测试数据

import random

my_max = 100
n = random.randint(1, my_max)
k = random.randint(0, n)
data = []
for i in range(n):
    data.append(random.randint(1, my_max))

print("{0} {1}".format(len(data), k))
print(" ".join([str(x) for x in data]))
