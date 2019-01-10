def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run("05:00") == "07:00"
    assert my_run("07:00") == "10:30"
    assert my_run("23:20") == "01:20"



def my_run():
    pass


my_func_test()
