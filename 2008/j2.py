#


def my_print(x, end="\n"):
    # print(x, end=end)
    pass


def my_input():
    input_data = []
    while True:
        tmp = int(input())
        input_data.append(tmp)
        if tmp == 1 and len(input_data) >= 2 and input_data[-2] == 4:
            break
    return input_data

    pass


def my_change(start_l, button, press_count):
    data_input = start_l.copy()
    next_data = data_input
    my_print("data_input={0}".format(data_input))
    for i in range(press_count):
        if button == 1:
            next_data = data_input[1:5] + [data_input[0]]
        elif button == 2:
            next_data = [data_input[-1]] + data_input[0:-1]
        elif button == 3:
            next_data = [data_input[1], data_input[0]] + data_input[2:]
        else:
            next_data = data_input
        my_print(next_data)
        data_input = next_data
    return next_data

    pass


def my_run(data):
    size = len(data)
    start_l = list("ABCDE")
    next_l = start_l
    for i in range(0, size, 2):
        button = data[i]
        press_num = data[i + 1]
        my_print("start_l={0}\t button={1} press_num={2} ".format(next_l, button, press_num))
        next_l = my_change(next_l, button, press_num)
        my_print("next_l={0}".format(next_l))
    return " ".join(next_l)
    pass


def my_unit_test():
    assert my_change(list("ABCDE"), 2, 1) == list('EABCD')
    assert my_change(list('EABCD'), 3, 1) == list('AEBCD')
    assert my_change(list('AEBCD'), 2, 3) == list('BCDAE')
    pass


def my_func_test():
    assert my_run([2, 1, 3, 1, 2, 3, 4, 1]) == "B C D A E"
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

# quit()

my_main()
