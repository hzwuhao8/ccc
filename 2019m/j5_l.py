#
# 还是没有看懂
#
#


def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run(1, 2, [1]) == 0
    assert my_run(1, 1, [1]) == 1

    assert my_run(3, 1, [1, 1, 1]) == 3
    assert my_run(3, 1, [1, 1, 1, 2, 3, 2, 2, 3]) == 3 + 3 + 2
    assert my_run(3, 2, [1, 1, 1]) == 0
    assert my_run(4, 3, [1, 2, 2, 3]) == 2
    assert my_run(4, 1, [1, 2, 2, 3]) == 4  # 有疑问， 1+2+1 = 4 种
    assert my_run(2, 1, [1, 2]) == 2
    my_print("***" * 20)
    assert my_run(3, 2, [1, 2, 3]) == 3
    my_print("***" * 20)
    assert my_run(4, 1, [1, 2, 3, 4]) == 4
    assert my_run(4, 3, [1, 2, 3, 4]) == 4  # C(4,3) = C(4,1)
    assert my_run(4, 2, [1, 2, 3, 4]) == 4 * 3 / 2


def my_run(n, k, data):
    dic = {}
    for x in data:
        dic.setdefault(x, 0)
        dic[x] = dic[x] + 1
    my_print(dic)
    if k > len(dic):
        return 0
    res = f(len(dic), k, dic, 0)
    return res
    pass


cache = {}


def f(n, k, dic, layer):
    my_print("  " * layer + "n={0} k={1} an={2} ".format(n, k, dic.get(n, 0)))
    if n == 0 and k == 0:
        return 1
    elif k > n:
        return 0
    elif (n, k) in cache:
        return cache[(n, k)]
    else:
        t1 = f(n - 1, k, dic, layer + 1)
        t2 = f(n - 1, k - 1, dic, layer + 1)
        res = t1 + dic.get(n, 0) * t2
        cache[(n, k)] = res
        return res


def my_main():
    n, k = [int(x) for x in input().split()]
    data = [int(x) for x in input().split()]
    res = my_run(n, k, data)
    print(res % 998244353)


my_func_test()
