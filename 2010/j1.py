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
    data = int(input())
    return data



def my_run(data):
    res = []
    for i in range(5, 0, -1):
        for j in range(0, i + 1, 1):
            if i + j == data:
                res.append((i, j))
        my_print("i={0}\tres={1}".format(i, res))
    my_print("res={0}".format(res))
    return len(res)
    pass


def my_unit_test():
    pass


def my_func_test():
    assert my_run(4) == 3
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


if os.environ.get("UNIT", None):
    my_unit_test()
elif os.environ.get("FUNC", None):
    my_func_test()
else:
    my_main()
