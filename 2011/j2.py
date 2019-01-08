def my_print(x, end="\n"):
    print(x, end=end)


def my_f(h, t):
    a = -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t
    return a




def my_func_test():
    assert my_run(30, 10) == 6
    assert my_run(70, 10) == -1
