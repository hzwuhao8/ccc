def my_func_test():
    assert my_run("W L W W L W") == 2
    assert my_run("L L L L L L") == -1


def my_run(my_str):
    w_count = my_str.count("W")
    l_count = my_str.count("L")
    if w_count == 5 or w_count == 6:
        return 1
    elif w_count == 3 or w_count == 4:
        return 2
    elif w_count == 1 or w_count == 2:
        return 3
    else:
        return -1


my_func_test()


def my_main():
    my_str_list = []
    for i in range(6):
        my_str_list.append(input())
    my_str = " ".join(my_str_list)
    res = my_run(my_str)
    print(res)


my_main()
