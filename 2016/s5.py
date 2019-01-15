#
# 这个 题目 比较好 理解
# 就是 需要判断 相邻位置  和  大量的 运算； 对于  比较大的N /T  可能有性能问题
#
#
import math


def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run(7, 1, "0000001") == "1000010"
    assert my_run(5, 3, "01011") == "10100"
    data = "0101011111011000010"
    d1 = [int(x) for x in data]
    d2 = d1.copy()
    n = len(data)
    k = 16
    for i in range(k):
        d1 = change(n, d1)

    assert change_2x(n, d2, 4) == d1


# 如何找到 周期？
# 会存在 不变 模式吗？
# 会存在 周期 模式吗？
#
# 用 2 的 指数次  进行 逼近
#  x =
#  change 1
#
#
#
#

def my_run(n, t, my_str):
    data = [int(x) for x in my_str]
    my_print(data)
    # 按照 2**k 进行逼近
    # 562949953421311  math.log  存在误差， 导致  k  有可能 偏大
    while t > 2:
        k = int(math.log(t, 2))
        if 2 ** k > t:
            k = k - 1
        t = t - 2 ** k
        data = change_2x(n, data, k)
    my_print("t={0}".format(t))
    for i in range(t):
        data = change(n, data)

    return "".join([str(x) for x in data])


# 2**x
def change_2x(n, data, x):
    data_result = data.copy()
    t = 2 ** x
    for i in range(n):
        pre = (n + (i - t) % n) % n
        suf = (i + t) % n
        c0 = data[pre]
        c1 = data[suf]
        if c0 + c1 == 1:
            data_result[i] = 1
        else:
            data_result[i] = 0
    return data_result


def change(n, data):
    # 取 附近
    data_result = data.copy()

    for i in range(n):
        pre = i - 1
        suf = i + 1
        if suf == n:
            suf = 0
        c0 = data[pre]
        c1 = data[suf]
        if c0 + c1 == 1:
            data_result[i] = 1
        else:
            data_result[i] = 0
    return data_result


my_func_test()


def my_main():
    n, t = [int(x) for x in input().split()]
    my_str = input()
    res = my_run(n, t, my_str)
    print(res)


my_main()
