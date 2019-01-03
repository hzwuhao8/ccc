#


def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_input():
    pass


def my_run(data):

    pass


def my_unit_test():
    pass


def my_func_test():

    pass


def my_main_test():
    my_print("==unit=="*10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    my_res = my_run(input_data)
    print(my_res)


my_main_test()

quit()

my_main()

