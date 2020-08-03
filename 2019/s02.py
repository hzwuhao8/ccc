n = int(input())
data = [int(input()) for x in range(n)]

# 计算 需要计算的质数的范围
# 最大数的 一半？
max_n = 2 * max(data)
p_data = list(range(max_n + 1))
# 计算质数， 用筛法
for i in range(2, len(p_data)):
    if p_data[i] != 0:
        for k in range(2, max_n // p_data[i] + 1):
            p_data[p_data[i] * k] = 0

# print(p_data)
pp_data = []
for x in p_data[3:]:
    if x > 0:
        pp_data.append(x)
# print(pp_data)

p_set = set(pp_data)


def my_func(y):
    for a in pp_data:
        b = y - a
        if b in p_set:
            print(a, b)
            return


for y in data:
    # print(y)
    my_func(2 * y)
