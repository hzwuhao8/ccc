def my_func_test():
    assert my_run(12, 5) == 1
    assert my_run(12, -5) == 4
    assert my_run(-12, 5) == 2
    assert my_run(-12, -5) == 3


def my_run(x, y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3


def my_main():
    x = int(input())
    y = int(input())
    res = my_run(x, y)
    print(res)


my_func_test()


my_main()

