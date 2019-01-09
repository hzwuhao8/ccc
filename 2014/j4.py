def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run(10, [2, 3]) == [1, 3, 7, 9]
    assert my_run(11, [2, 3]) == [1, 3, 7, 9]
    assert my_run(2, [2, 3]) == [1]


def my_run(k, data):
    my_list = list(range(1, k + 1, 1))
    for i in data:
        my_print(my_list)
        size = (len(my_list) + 1) // i
        for j in range(1, size + 1):
            if i * j - 1 < len(my_list):
                my_list[i * j - 1] = 0
        my_list = list((filter(lambda x: x != 0, my_list)))

    my_print(my_list)
    return my_list


my_func_test()
