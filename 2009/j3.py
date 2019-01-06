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
    my_time = int(input())
    return my_time


def my_run(data):
    tz = [0, -3, -2, -1, 0, 1]
    if data <= 59:
        h, m = 0, data
    else:
        h = data // 100
        m = data % 100

    res = [(h + x) % 24 * 100 + m for x in tz]
    if m >= 30:
        last = (h + 1 + 1) % 24 * 100 + (m + 30) % 60
    else:
        last = (h + 1) % 24 * 100 + (m + 30)
    res.append(last)
    my_print(res)
    return res


def my_unit_test():
    pass


def my_func_test():
    assert my_run(1300) == [1300, 1000, 1100, 1200, 1300, 1400, 1430]
    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    my_res = my_run(input_data)

    print("""{ll[0]} in Ottawa.
{ll[1]} in Victoria.
{ll[2]} in Edmonton.
{ll[3]} in Winnipeg.
{ll[4]} in Toronto.
{ll[5]} in Halifax.
{ll[6]} in St. John's.""".format(ll=my_res))


if os.environ.get("UNIT", None):
    my_unit_test()
elif os.environ.get("FUNC", None):
    my_func_test()
else:
    my_main()
