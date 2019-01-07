#
#
# x,y => x+1, y+2 ; x+2 , y+1 ; 4+4   共 8中可能的情况
# 这里是搜索 最短路径
# 当前位置， 所有可能的合法的移动； 然后在进一步 搜索， 直到 达到目标点
#
# 使用广度优先 搜索， 发现最短路径
#
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


# 所有可能的移动
def move_able(x, y):
    x_dir = [1, 2]
    y_dir = [2, 1]

    res = []
    for i in range(2):
        x0 = x + x_dir[i]
        y0 = y + y_dir[i]
        if is_validate(x0, y0):
            res.append((x0, y0))
        x1 = x + x_dir[i]
        y1 = y - y_dir[i]
        if is_validate(x1, y1):
            res.append((x1, y1))

        x2 = x - x_dir[i]
        y2 = y + y_dir[i]
        if is_validate(x2, y2):
            res.append((x2, y2))
        x3 = x - x_dir[i]
        y3 = y - y_dir[i]
        if is_validate(x3, y3):
            res.append((x3, y3))
    return res


def is_validate(x, y):
    return 0 < x <= 8 and 0 < y <= 8


def find_path(start, stop, layer=0, node_set=set()):
    if stop in node_set:
        my_print("已经在 结果集中，直接返回, layer={0}".format(layer))
        return layer
    else:
        all_next_steps = move_able(start)
        all_next_steps_set = set(all_next_steps)
        # 已经处理过的就不用再处理了
        may_next_steps = all_next_steps_set.difference(node_set)
        my_print("may_next_steps={0}".format(may_next_steps))
        if stop in may_next_steps:
            my_print("找到 目标节点")
            return layer
        else:
            for s in may_next_steps:
                node_set.add(s)
                find_path(s, stop, layer + 1, node_set)

    return "NOT FOUND"


def my_run(start, stop):
    (x0, y0), (x1, y1) = start, stop
    dx = x1 - x0
    dy = y1 - y0

    s = dx * dx + dy * dy
    may_be = s // 5
    my_print(may_be)
    # 可以作为 一个估计  粗略的近似
    layer = find_path(start, stop, 0, set([start]))
    my_print(layer)
    return layer
    pass


def my_unit_test():
    res = move_able(4, 4)
    my_print(res)
    assert len(res) == 8
    assert (5, 6) in res
    pass


def my_func_test():
    assert my_run((2, 1), (2, 1)) == 0
    assert my_run((2, 1), (3, 3)) == 1
    assert my_run((4, 2), (7, 5)) == 2
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
