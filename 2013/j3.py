def my_func_test():
    assert my_run(1987) == 2013
    assert my_run(999) == 1023


def my_run(start):
    i = 1
    while True:
        year = start + i
        if len(set(str(year))) == len(str(year)):
            return year
        else:
            i += 1


my_func_test()


def my_main():
    start = int(input())
    res = my_run(start)
    print(res)


my_main()
