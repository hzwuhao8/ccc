def my_func_test():
    assert my_run([[5, 6], [6, 6], [4, 3], [5, 2]]) == [94, 91]


def my_run(data):
    a = 100
    d = 100
    for xa, xd in data:
        if xa > xd:
            d -= xa
        elif xa == xd:
            pass
        else:
            a -= xd
    return [a, d]


def my_main():
    total = int(input())
    data = []
    for i in range(total):
        data.append([int(x) for x in input().split()])
    res = my_run(data)
    res_str = "\n".join([str(x) for x in res])
    print(res_str)


my_func_test()

my_main()

