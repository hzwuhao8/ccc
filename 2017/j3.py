#
#
# 找到 一条 正好 用完 电力的路， 也就是 正好 距离正好是要求的
#
#
#

def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run((3, 4), (3, 3), 3) == 'Y'
    assert my_run((10, 2), (10, 4), 5) == 'N'


def my_run(p1, p2, steps, layer=0):
    s = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    my_print("  " * layer + "layer={3} p1={0},p2={1},steps={2},s={4},".format(p1, p2, steps, layer, s))
    if layer > 100:
        return "N"
    if s == 1 and steps == 1:
        return 'Y'
    else:
        if s > 1 and steps == 1:
            return 'N'
        if s > steps ** 2:
            return 'N'
        # 4个方向 进行 递归
        x1, y1 = p1
        x2, y2 = p2
        next_1 = my_run((x1 - 1, y1), (x2, y2), steps - 1, layer + 1)
        if next_1 == "Y":
            return "Y"
        next_2 = my_run((x1 + 1, y1), (x2, y2), steps - 1, layer + 1)
        if next_2 == "Y":
            return "Y"
        next_3 = my_run((x1, y1 + 1), (x2, y2), steps - 1, layer + 1)
        if next_3 == "Y":
            return "Y"
        next_4 = my_run((x1, y1 - 1), (x2, y2), steps - 1, layer + 1)
        if next_4 == "Y":
            return "Y"
        return "N"

    pass


my_func_test()
