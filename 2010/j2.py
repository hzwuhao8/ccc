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
    for i in range(5):
        data.append(int(input()))
    return data


def my_distance(a, b, s):
    total1 = 0
    distance1 = 0
    max1 = s // (a + b) + 2
    for i in range(max1):
        if i % 2 == 0:
            total1 = total1 + a
            distance1 = distance1 + a
        else:
            total1 = total1 + b
            distance1 = distance1 - b

        if total1 == s:
            break
        elif total1 > s:
            delta = total1 - s
            total1 -= delta
            if i % 2 == 0:
                distance1 = distance1 - delta
            else:
                distance1 = distance1 + delta
        else:
            pass

        my_print("i={2} total1={0},distance1={1}".format(total1, distance1, i))
    my_print("total1={0},distance1={1}".format(total1, distance1))
    return distance1


def my_run(data):
    a, b, c, d, s = data
    d1 = my_distance(a, b, s)
    d2 = my_distance(c, d, s)
    if d1 > d2:
        return "Nikky"
    elif d1 == d2:
        return "Tied"
    else:
        return "Byron"


def my_unit_test():
    assert my_distance(4, 2, 12) == 4
    assert my_distance(5, 3, 12) == 6


def my_func_test():
    assert my_run((4, 2, 4, 3, 12)) == "Byron"
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
