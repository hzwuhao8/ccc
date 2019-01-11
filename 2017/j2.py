def my_func_test():
    assert my_run(12, 0) == 12
    assert my_run(12, 1) == 132
    assert my_run(12, 3) == 13332


def my_run(n, k):
    data = []
    for i in range(0, k + 1):
        data.append(n * 10 ** i)
    return sum(data)


def my_main():
    n = int(input())
    k = int(input())
    res = my_run(n, k)
    print(res)


my_func_test()

my_main()
