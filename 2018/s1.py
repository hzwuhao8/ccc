def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run([16, 0, 10, 4, 15]) == 3.0


# 排序
# 取中点
# 计算区间长度
# 取最小的区间长度
def my_run(data):
    data.sort()
    my_print(data)
    s_list = []
    for i in range(1, len(data) - 1):
        m1 = data[i - 1] + (data[i] - data[i - 1]) / 2
        m2 = data[i] + (data[i + 1] - data[i]) / 2
        s1 = m2 - m1
        s_list.append(s1)
    my_print(s_list)
    return min(s_list)


my_func_test()


def my_main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(int(input()))
    res = my_run(data)

    print("{0}".format(res))


my_main()
