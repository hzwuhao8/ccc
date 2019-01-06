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
    width = int(input())
    return width


STR_LIST = "WELCOME TO CCC GOOD LUCK TODAY".split()


def my_split(width):
    my_print(STR_LIST)
    my_len = len(STR_LIST)
    next_str_list = STR_LIST.copy()
    res = []
    for s in range(8):
        for i in range(my_len + 1, 0, -1):
            tmp_str = ".".join(next_str_list[:i])
            my_print("s={0} i={1} tmp_str={2}".format(s, i, tmp_str))
            if len(tmp_str) <= width:
                res.append(tmp_str)
                next_str_list = next_str_list[i:]
                break
        if len(next_str_list) == 0:
            break
    my_print(res)
    return res


def my_add_dot(my_str, width):
    max_add_dot = width - len(my_str)
    tmp_list = my_str.split(".")
    if len(tmp_list) == 1:
        tmp_str = tmp_list[0] + "." * max_add_dot
        return tmp_str
    else:
        for i in range(max_add_dot + 1):
            for j in range(len(tmp_list) - 1):
                tmp_str = ".".join(tmp_list)
                my_print("tmp_str={0},len={1}".format(tmp_str, len(tmp_str)))
                if len(tmp_str) >= width:
                    return tmp_str
                else:
                    step_str = tmp_list[j]
                    step_str += "."
                    tmp_list[j] = step_str

    return my_str


def my_run(width):
    tmp_list = my_split(width)
    my_print("tmp_list={0}".format(tmp_list))
    tmp2_list = [my_add_dot(my_str, width) for my_str in tmp_list]
    my_print("tmp2_list={0}".format(tmp2_list))
    return tmp2_list


def my_unit_test():
    assert my_split(15) == ["WELCOME.TO.CCC", "GOOD.LUCK.TODAY"]
    assert my_split(26) == ["WELCOME.TO.CCC.GOOD.LUCK", "TODAY"]

    assert my_add_dot("GOOD.LUCK", 14) == "GOOD......LUCK"

    assert my_add_dot("WELCOME.TO.CCC", 15) == "WELCOME..TO.CCC"
    assert my_add_dot("WELCOME.TO.CCC.GOOD.LUCK", 26) == "WELCOME..TO..CCC.GOOD.LUCK"
    assert my_add_dot("TODAY", 26) == "TODAY....................."
    pass


def my_func_test():
    assert my_run(15) == ["WELCOME..TO.CCC", "GOOD.LUCK.TODAY"]
    assert my_run(26) == ["WELCOME..TO..CCC.GOOD.LUCK", "TODAY....................."]
    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    my_res = my_run(input_data)
    print("\n".join(my_res))


if os.environ.get("UNIT", None):
    my_unit_test()
elif os.environ.get("FUNC", None):
    my_func_test()
else:
    my_main()
