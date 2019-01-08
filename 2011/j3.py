def my_print(x, end="\n"):
    print(x, end=end)


def my_run(t1, t2):
    n = 2
    while True:
        t3 = t1 - t2
        if t3 < 0:
            break
        else:
            t1 = t2
            t2 = t3
            n = n + 1
    return n


def my_func_test():
    assert my_run(120, 71) == 5


def my_main():
    t1 = int(input())
    t2 = int(input())
    res = my_run(t1, t2)
    print(res)


my_func_test()

my_main()
