def my_func_test():
    assert my_run([30, 10, 20, 20]) == "No Fish"
    assert my_run([1, 10, 12, 13]) == "Fish Rising"


def my_run(data):
    if data.count(data[0]) == 4:
        return "Fish At Constant Depth"
    ll = sorted(data)
    if ll == data:
        return "Fish Rising"
    elif ll == data.reverse():
        return "Fish Diving"
    else:
        return "No Fish"


my_func_test()


def my_main():
    data = [int(input()) for i in range(4)]
    res = my_run(data)
    print("{0}".format(res))


my_main()
