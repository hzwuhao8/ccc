#
# 这个 题目 比较好 理解
# 就是 需要判断 相邻位置  和  大量的 运算； 对于  比较大的N /T  可能有性能问题
#
#


def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run(7, 1, "0000001") == "1000010"
    assert my_run(5, 3, "01011") == "10100"


def my_run(n, t, my_str):
    data = [int(x) for x in my_str]
    my_print(data)
    for i in range(t):
        data = change(n, data)
        my_print(data)

    return "".join([str(x) for x in data])


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


