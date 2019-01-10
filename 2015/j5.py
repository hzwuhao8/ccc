def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run(8, 1) == 1
    assert my_run(8, 8) == 1
    assert my_run(9, 8) == 1
    assert my_run(5, 2) == 2
    assert my_run(4, 3) == 1
    assert my_run(10, 8) == 2
    # assert my_run(11, 8) == 3
    assert my_run(7, 3) == 4
    assert my_run(8, 4) == 5
    assert my_run(6, 2) == 3


def my_run(n, k):
    layer = 0
    my_print("  " * layer + "n={0},k={1},layer={2}".format(n, k, layer))
    if n <= k:
        res = 1
    elif k == 1:
        res = 1
    else:
        n1 = n - k
        k1 = k
        if n1 < k1:
            k1 = n1
        res = my_run_inner(n1, k1, 1, zero_ok=True)
    my_print("res={0}".format(res))
    return res


def my_run_inner(n, k, layer, zero_ok):
    if layer > 5:
        print("ERROR")
        return 0;
    my_print("  " * layer + "n={0},k={1},layer={2},zero_ok={3}".format(n, k, layer, zero_ok))
    if k == 1:
        return 1
    if n < k:
        print("ERROR")
        return 0
    if n == k:
        if not zero_ok:
            total = 1
            return total
        else:
            total = 0
            pass

    if n > k:
        if zero_ok:
            # n = n - k
            total = 0
            pass
        else:
            n = n - k
            total = 0
            pass

    my_print("  " * layer + "start total = {0}".format(total))
    for i in range(1, k + 1):

        if n >= i:
            res = my_run_inner(n, i, layer + 1, False)
            my_print(
                "  " * (layer + 1) + "result n={0},k={1},layer={2},zero_ok={3} total={5} res={4}".format(n, i,
                                                                                                         layer + 1,
                                                                                                         False,
                                                                                                         res, total))
            total = total + res

    my_print("  " * layer + "total={0}, layer={1}".format(total, layer))
    return total


# 如何进行递归？
# 要求队列是 不减的
# 可以穷举，但是 对于 n  大的情况就无法处理
# k - n ; 如何进行分配；

def my_unit_test():
    assert my_run_inner(2, 2, 1, True) == 2
    assert my_run_inner(4, 3, 1, False) == 1
    assert my_run_inner(4, 3, 1, True) == 4


my_unit_test()
my_func_test()


def my_main():
    n = int(input())
    k = int(input())
    res = my_run(n, k)
    print(res)


my_main()
