def my_func_test():
    assert my_run(1, 7) == "Before"
    assert my_run(8, 31) == "After"
    assert my_run(2, 18) == "Special"

my_func_test()


def my_run(m, d):
    if m <= 1:
        return "Before"
    elif m == 2 and d < 18:
        return "Before"
    elif m == 2 and d == 18:
        return "Special"
    else:
        return "After"





