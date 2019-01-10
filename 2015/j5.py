def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run(8, 8) == 1
    assert my_run(1, 8) == 1
    assert my_run(8, 9) == 2
    assert my_run(8, 10) == 2
    assert my_run(8, 11) == 3
    assert my_run(7, 3) == 4
    assert my_run(8, 4) == 5
    assert my_run(6, 2) == 3


def my_run(k, n):
    if k == 1:
        return 1
    if k == n:
        return 1


# 如何进行递归？
# 要求队列是 不减的
# 可以穷举，但是 对于 n  大的情况就无法处理
# k - n ; 如何进行分配；


my_func_test()
