def my_func_test():
    assert my_run("pusheen") == 0
    assert my_run("neehsup") == 6


def my_run(my_str):
    base_str = "pusheen"
    x1 = len(base_str) - len(my_str)
    tmp_list = list(zip(base_str, my_str))
    tmp2_list = [x[0] == x[1] for x in tmp_list]
    return x1 + tmp2_list.count(False)


my_func_test()


def my_main():
    my_str = input()
    res = my_run(my_str)
    print(res)


my_main()
