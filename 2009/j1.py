#
import os
import sys
import copy
import time


def my_print(x, end="\n"):
    if os.environ.get('DEBUG', None) or os.environ.get('TRACE', None):
        print(x, file=sys.stderr, end=end)
    else:
        pass


def my_print_trace(x, end="\n"):
    if os.environ.get('TRACE', None):
        print(x, file=sys.stderr, end=end)
    else:
        pass


def my_input():
    data = []
    for i in range(3):
        data.append(int(input("Digit {0}?\n".format(11 + i))))
    return data


def my_run(data):
    prefix_list = [int(x) for x in "9780921418"]
    data_list = prefix_list + data
    total = 0
    for i in range(len(data_list)):
        if i % 2 == 1:
            m = 3
        else:
            m = 1
        total += data_list[i] * m
    return total


def my_unit_test():
    pass


def my_func_test():
    assert my_run([9, 4, 8]) == 120
    assert my_run([0, 5, 2]) == 108
    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    my_res = my_run(input_data)
    print("The 1-3-sum is {0}".format(my_res))


if os.environ.get("UNIT", None):
    my_unit_test()

if os.environ.get("FUNC", None):
    my_func_test()

my_main()
