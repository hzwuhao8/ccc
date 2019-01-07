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
    pass


def my_run(data):
    pass


def my_1(dic, x, v):
    dic[x] = v
    return dic


def my_2(dic, x):
    return dic[x]


def my_3(dic, x, y):
    dic[x] = dic[x] + dic[y]


def my_3(dic, x, y):
    dic[x] = dic[x] + dic[y]


def my_4(dic, x, y):
    dic[x] = dic[x] * dic[y]


def my_5(dic, x, y):
    dic[x] = dic[x] - dic[y]


def my_6(dic, x, y):
    dic[x] = dic[x] // dic[y]


def my_unit_test():
    my_dic = {}
    assert my_1(my_dic, 'A', 3) == {'A': 3}
    assert my_1(my_dic, 'B', 4) == {'A': 3, 'B': 4}
    assert my_2(my_dic, 'A') == 3
    assert my_2(my_dic, 'B') == 4
    my_3(my_dic, 'A', 'B')
    assert my_2(my_dic, 'A') == 7
    my_5(my_dic, 'A', 'A')
    assert my_2(my_dic, 'A') == 0
    assert my_2(my_dic, 'B') == 4


def my_func_test():
    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    dic = {'A': 0, 'B': 0}
    while True:
        my_str = input()
        my_print("my_str={0}, split={1}".format(my_str, my_str.split()))
        if my_str == "7":
            break
        elif my_str.startswith("1"):
            cmd, x, v = my_str.split()
            my_1(dic, x, int(v))
        elif my_str.startswith("2"):
            cmd, x = my_str.split()
            print(my_2(dic, x))
        elif my_str.startswith("3"):
            cmd, x, y = my_str.split()
            my_3(dic, x, y)
        elif my_str.startswith("3"):
            cmd, x, y = my_str.split()
            my_3(dic, x, y)
        elif my_str.startswith("4"):
            cmd, x, y = my_str.split()
            my_4(dic, x, y)
        elif my_str.startswith("5"):
            cmd, x, y = my_str.split()
            my_5(dic, x, y)
        elif my_str.startswith("6"):
            cmd, x, y = my_str.split()
            my_6(dic, x, y)
        else:
            pass


if os.environ.get("UNIT", None):
    my_unit_test()
elif os.environ.get("FUNC", None):
    my_func_test()
else:
    my_main()
