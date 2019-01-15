def my_func_test():
    assert my_run(3, "1 3 3", "2 2 6") == 2
    assert my_run(3, "1 2 3", "4 5 6") == 0
    assert my_run(4, "1 2 3 4", "1 3 2 4") == 4


def my_run(n, str1, str2):
    d1 = [int(x) for x in str1.split()]
    d2 = [int(x) for x in str2.split()]
    if sum(d1) == sum(d2):
        return n
    else:
        for i in range(-1, -n, -1):
            if sum(d1[:i]) == sum(d2[:i]):
                return n + i
        return 0


my_func_test()


def my_main():
    n = int(input())
    str1 = input()
    str2 = input()
    res = my_run(n, str1, str2)
    print(res)


my_main()
