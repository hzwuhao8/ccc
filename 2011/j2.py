def my_print(x, end="\n"):
    print(x, end=end)


def my_f(h, t):
    a = -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t
    return a


def my_run(h, m):
    res = -1;
    for i in range(1, m + 1):
        a = my_f(h, i)
        if a <= 0:
            res = i
            break
    return res


def my_func_test():
    assert my_run(30, 10) == 6
    assert my_run(70, 10) == -1


def my_main():
    h = int(input())
    m = int(input())
    res = my_run(h,m)
    if res ==-1:
        print("The balloon does not touch ground in the given time.")
    else:
        print("The balloon first touches ground at hour:")
        print(res)


my_func_test()

my_main()
