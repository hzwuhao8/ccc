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
    my_str = input()
    return my_str


# 如果出现2次以上
# 可以 正则处理
# 联系出现2次以上
# 可以用字符串的  字串处理
# 也可以用 列表处理吗？

# 用字符串 搜索  可能更简单

def is_cycle(data, cycle):
    my_print("data={0}  cycle={1}".format(data, cycle))
    min_count = max(len(data) // len(cycle), 2)
    c2 = cycle * min_count
    for i in range(len(data) - len(cycle)):
        # my_print("data[i:i + len(c2)]={0}".format(data[i:i + len(c2)]))
        # my_print("data[i:i + len(c2)] == c2={0}".format(data[i:i + len(c2)] == c2))
        tmp = data[i:i + len(c2)]
        my_print("data[i:i + len(c2)]={0}".format(tmp))
        if tmp == c2:
            return True
        elif i + len(cycle) >= len(tmp) and len(cycle) > 1 and min_count <=2:
            if tmp == c2[0:len(tmp)]:
                my_print("最后一部分匹配")
                return True
    return False


def my_run(data):
    my_print("=====" * 20)

    data_list = [int(x) for x in data.split()]
    data_list = data_list[1:]
    tmp_1 = []
    for i in range(len(data_list) - 1):
        tmp_1.append(data_list[i + 1] - data_list[i])
    my_print(data_list)
    my_print(tmp_1)
    my_print("search")
    for i in range(1, len(tmp_1)):
        for j in range(len(tmp_1) - i):
            may_be = tmp_1[j:j + i]
            is_c = is_cycle(tmp_1, may_be)
            if is_c:
                my_print("may_be={0} is_cycle={1}".format(may_be, is_c))
                return len(may_be)
    return len(data_list) - 1
    pass


def my_unit_test():
    assert is_cycle([-4, 1, 2, -2, 1, 2, -2], [1, 2, -2])
    assert not is_cycle([-4, 1, 2, -2, 1, 2, -2], [1, 2])
    assert not is_cycle([-4, 1, 2, -2, 1, 2, -2], [2, -2])
    assert not is_cycle([-4, 1, 2, -2, 1, 2, -2], [-2, 1])
    assert is_cycle([1, 2, 1], [1, 2])
    pass


def my_func_test():
    assert my_run("7 3 4 6 4 5 7 5") == 3
    assert my_run("3 1 3 5") == 1
    assert my_run("4 3 4 6 7") == 2
    assert my_run("3 1 4 5") == 2
    assert my_run("6 1 4 7 12 43 -31") == 5

    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    while True:
        my_str = input()
        if "0" == my_str:
            break
        else:
            res = my_run(my_str)
            print(res)


if os.environ.get("UNIT", None):
    my_unit_test()
elif os.environ.get("FUNC", None):
    my_func_test()
else:
    my_main()
