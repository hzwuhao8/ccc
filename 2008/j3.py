#


def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_input():
    input_data = input()
    return input_data
    pass


def my_move(form, to):
    steps = 0
    return steps


def my_run(data):
    pass


def my_unit_test():
    assert my_move('A', 'A') == 0
    assert my_move('A', 'G') == 1
    assert my_move('G', 'P') == 4
    assert my_move('P', 'S') == 4
    assert my_move('S', 'enter') == 6
    pass


def my_func_test():
    assert my_run("GPS") == 15
    assert my_run("ECHO ROCK") == 29
    pass


def my_main_test():
    my_print("==unit==" * 10)
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
