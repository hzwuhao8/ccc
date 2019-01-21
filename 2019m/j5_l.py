#
# 还是没有看懂
#
#


def my_print(x):
    # print(x)
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
    my_print("n={0} k={1} data={2}".format(n, k, data))
    dic = {}
    for x in data:
        dic.setdefault(x, 0)
        dic[x] = dic[x] + 1
    my_print(dic)
    if k > len(dic):
        return 0
    an = [0]
    for t1, v in dic.items():
        an.append(v)
    my_print("an={0}".format(an))
    cache = {}

    res = f(len(dic), k, an, 0, cache)
    my_print("n={0} k={1} an={2}  res={3}".format(len(dic), k, an[len(dic)], res))
    my_print(cache)
    return res
    pass


# 核心 递归 函数
# an == 1 时  就是  组合的c(n,k)
def f(n, k, an, layer, cache):
    my_print("  " * layer + "n={0} k={1} an={2} ".format(n, k, an[n]))
    if k == 0:
        return 1
    elif k > n:
        return 0
    elif (n, k) in cache:
        return cache[(n, k)]
    else:
        t1 = f(n - 1, k, an, layer + 1, cache)
        t2 = f(n - 1, k - 1, an, layer + 1, cache)
        res = t1 + an[n] * t2
        cache[(n, k)] = res
        return res


def my_main():
    n, k = [int(x) for x in input().split()]
    data = [int(x) for x in input().split()]
    res = my_run(n, k, data)
    print(res % 998244353)


my_func_test()
my_main()
