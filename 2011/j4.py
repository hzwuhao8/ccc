def my_print(x, end="\n"):
    print(x, end=end)


def my_run(position_list, cmd,length):
    pass


def my_run(position_list,cmd_str):
    pass


def my_func_test():
    position_list = [(-1, -5)]
    assert my_run(position_list, "l 2") == "-3 -5 safe"
    assert my_run(position_list, "d 2") == "-3 -7 safe"
    assert my_run(position_list, "r 1") == "-2 -7 safe"

    position_list = [(-1, -5)]
    assert my_run(position_list, "r 2") == "1 -5 safe"
    assert my_run(position_list, "d 10") == "1 -15 DANGER"
    assert my_run(position_list, "r 4") == ""


my_func_test()

