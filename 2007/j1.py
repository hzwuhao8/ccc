#


def my_print(x, end="\n"):
    #print(x, end=end)
    pass


def my_input():
    data = [0] * 3
    for i in range(3):
        data[i] = int(input())
    return data
    pass


def my_run(data):
    res = sorted(data)
    return res[1]
    pass


def my_unit_test():
    pass


def my_func_test():
    assert my_run([10, 5, 8]) == 8
    pass


def my_main():
    my_print("==unit=="*10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()
    input_data = my_input()
    res = my_run(input_data)
    print(res)


my_main()
