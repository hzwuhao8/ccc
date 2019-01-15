#
# 这个 题目 比较好 理解
# 就是 需要判断 相邻位置  和  大量的 运算； 对于  比较大的N /T  可能有性能问题
#
#


def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run(7, 1, "0000001") == "1000010"
    assert my_run(5, 3, "01011") == "10100"


def my_run(n, t, my_str):
    data = [int(x) for x in my_str]
    my_print(data)


my_func_test()