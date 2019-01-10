def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run(1, 1) == 1
    assert my_run(1, 8) == 1
    assert my_run(2, 2) == 1
    assert my_run(8, 4) == 5
    assert my_run(6, 2) == 3


dic = {}


# 都是不允许 zero 的
def my_run(n, k, layer=0):

    if n <= k:
        res = 1
    elif k == 1:
        res = 1
    elif n == k:
        res = 1
    else:
        if (n, k) in dic:
            my_print("ca" * layer + "at cache n={0},k={1},layer={2}".format(n, k, layer))
            return dic[(n, k)]
        else:
            my_print("  " * layer + "n={0},k={1},layer={2}".format(n, k, layer))

        n1 = n - k
        k1 = k
        if n1 < k1:
            k1 = n1
        total = 0
        for i in range(1, k1 + 1):
            res2 = my_run(n1, i, layer + 1)
            total += res2
        res = total
    my_print("  " * layer + "n={0},k={1},layer={2} res={3}".format(n, k, layer, res))
    dic[(n, k)] = res
    return res


my_func_test()


def my_main():
    n = int(input())
    k = int(input())
    res = my_run(n, k)
    print(res)


my_main()
