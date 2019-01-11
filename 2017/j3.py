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
    my_print(dic_cache)
    assert my_run((0, 0), (1, 2), 4) == 'N'
    my_print(dic_cache)
    assert my_run((3, 4), (3, 3), 3) == 'Y'
    assert my_run((10, 2), (10, 4), 2) == 'Y'
    assert my_run((10, 2), (10, 4), 4) == 'Y'
    assert my_run((10, 2), (10, 4), 6) == 'Y'
    my_print(dic_cache)
    assert my_run((10, 2), (10, 4), 5) == 'N'


dic_cache = {}


def my_run(p1, p2, steps, layer=0):
    delta_x = (p2[0] - p1[0])
    delta_y = (p2[1] - p1[1])

    s = delta_x ** 2 + delta_y ** 2
    my_print("  " * layer + "layer={3} p1={0},p2={1},steps={2},s={4},".format(p1, p2, steps, layer, s))
    my_print("  " * layer + "dx={0},dy={1},steps={2},cache={3}".format(delta_x, delta_y, steps,
                                                                       dic_cache.get((delta_x, delta_y, steps), '')))
    if (delta_x, delta_y, steps) in dic_cache:
        return dic_cache[(delta_x, delta_y, steps)]

    if layer > 100:
        return "N"
    if s == 1 and steps == 1:
        dic_cache[(delta_x, delta_y, steps)] = 'Y'
        return 'Y'
    else:
        if s > 1 and steps == 1:
            dic_cache[(delta_x, delta_y, steps)] = 'N'
            return 'N'
        if s > steps ** 2:
            dic_cache[(delta_x, delta_y, steps)] = 'N'
            return 'N'
        # 4个方向 进行 递归
        x1, y1 = p1
        x2, y2 = p2
        next_1 = my_run((x1 - 1, y1), (x2, y2), steps - 1, layer + 1)
        if next_1 == "Y":
            delta_x = (x2 - (x1 - 1))
            delta_y = (y2 - y1)
            dic_cache[(delta_x, delta_y, steps)] = 'Y'
            return "Y"
        next_2 = my_run((x1 + 1, y1), (x2, y2), steps - 1, layer + 1)
        if next_2 == "Y":
            delta_x = (x2 - (x1 + 1))
            delta_y = (y2 - y1)
            dic_cache[(delta_x, delta_y, steps)] = 'Y'
            return "Y"
        next_3 = my_run((x1, y1 + 1), (x2, y2), steps - 1, layer + 1)
        if next_3 == "Y":
            delta_x = (x2 - x1)
            delta_y = (y2 - (y1 + 1))
            dic_cache[(delta_x, delta_y, steps)] = 'Y'
            return "Y"
        next_4 = my_run((x1, y1 - 1), (x2, y2), steps - 1, layer + 1)
        if next_4 == "Y":
            delta_x = (x2 - x1)
            delta_y = (y2 - (y1 - 1))
            dic_cache[(delta_x, delta_y, steps)] = 'Y'
            return "Y"
        delta_x = (p2[0] - p1[0])
        delta_y = (p2[1] - p2[1])
        dic_cache[(delta_x, delta_y, steps)] = 'N'
        return "N"

    pass


def my_main():
    p1 = [int(x) for x in input().split()]
    p2 = [int(x) for x in input().split()]
    steps = int(input())
    res = my_run(p1, p2, steps)
    print(res)


my_func_test()

my_main()
