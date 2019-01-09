def my_func_test():
    assert my_run(5, 10) == 15
    assert my_run(12, 15) == 18
    assert my_run(10, 10) == 10


def my_run(a, b):
    c = b + (b - a)
    return c


my_func_test()


def my_main():
    a = int(input())
    b = int(input())
    c = my_run(a, b)
    print(c)


my_main()
