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
    x = int(input())
    y = int(input())
    z = int(input())
    total = int(input())
    return [x, y, z, total]


def my_run(data):
    my_max = 101
    x, y, z, total = data
    res = []
    for i in range(my_max):
        for j in range(my_max):
            for k in range(my_max):
                t = i * x + j * y + k * z
                if t <= total and i + j + k > 0:
                    my_print([i, j, k, t])
                    res.append([i, j, k])

    return res


def my_unit_test():
    pass


def my_func_test():
    assert my_run([1, 2, 3, 2]) == [[0, 1, 0], [1, 0, 0], [2, 0, 0], ]

    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    my_res = my_run(input_data)
    for i, j, k in my_res:
        print("{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel".format(i=i, j=j, k=k))
    print("Number of ways to catch fish: {0}".format(len(my_res)))

if os.environ.get("UNIT", None):
    my_unit_test()
elif os.environ.get("FUNC", None):
    my_func_test()
else:
    my_main()
