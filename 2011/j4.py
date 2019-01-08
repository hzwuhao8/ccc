import os


def my_print(x, end="\n"):
    if os.environ.get("DEBUG", ""):
        print(x, end=end)
    else:
        pass


base_potion = [(0, -1), (0, -2), (0, -3),
               (1, -3), (2, -3), (3, -3),
               (3, -4), (3, -5),
               (4, -5), (5, -5),
               (5, -4), (5, -3),
               (6, -3), (7, -3),
               (7, -4), (7, -5), (7, -6), (7, -7),
               (6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7),
               (-1, -6), (-1, -5)
               ]


# 求出 所有的线段
# 求出 所有的点
# 也可以 用一个 list , 记录 所有的点
def is_intersection(all_point_list):
    my_print('len(all_point_list)={0}'.format(len(all_point_list)))
    my_print('len(set(all_point_list))={0}'.format(len(set(all_point_list))))
    if len(all_point_list) == len(set(all_point_list)):
        return "safe"
    else:
        return "DANGER"


def my_run_inner(position_list, all_point_list, cmd, steps):
    res = []
    if is_intersection(all_point_list) == "DANGER":
        # do nothing
        return res
    else:
        current = position_list[-1]
        x0, y0 = current
        x1, y1 = x0, y0
        if cmd == 'd':
            y1 = y0 - steps
            for i in range(1, steps + 1, 1):
                all_point_list.append((x0, y0 - i))
        elif cmd == 'u':
            y1 = y0 + steps
            for i in range(1, steps + 1, 1):
                all_point_list.append((x0, y0 + i))
        elif cmd == 'l':
            x1 = x0 - steps
            for i in range(1, steps + 1, 1):
                all_point_list.append((x0 - i, y0))
        else:
            x1 = x0 + steps
            for i in range(1, steps + 1, 1):
                all_point_list.append((x0 + i, y0))
        position_list.append((x1, y1))
        my_print("after move position_list={0}".format(position_list))
        my_print("all_point_list={0}".format(all_point_list))
        return [x1, y1, is_intersection(all_point_list)]


def my_run(position_list, all_point_list, cmd_str):
    cmd, length_str = cmd_str.split()
    my_print("cmd_str={0} cmd={1} length_str={2}, position_list={3}".format(cmd_str, cmd, length_str, position_list))
    my_print("all_point_list={0}".format(all_point_list))
    res_list = my_run_inner(position_list, all_point_list, cmd, int(length_str))
    return " ".join([str(x) for x in res_list])


def my_func_test():
    position_list = [(-1, -5)]
    all_point_list = base_potion.copy()
    assert my_run(position_list, all_point_list, "l 2") == "-3 -5 safe"
    assert my_run(position_list, all_point_list, "d 2") == "-3 -7 safe"
    assert my_run(position_list, all_point_list, "r 1") == "-2 -7 safe"

    position_list = [(-1, -5)]
    all_point_list = base_potion.copy()
    assert my_run(position_list, all_point_list, "r 2") == "1 -5 safe"
    assert my_run(position_list, all_point_list, "d 10") == "1 -15 DANGER"
    assert my_run(position_list, all_point_list, "r 4") == ""


def my_main():
    position_list = [(-1, -5)]
    all_point_list = base_potion.copy()
    while True:
        cmd_str = input()
        if cmd_str.startswith("q"):
            break
        else:
            res = my_run(position_list,all_point_list, cmd_str)
            if res:
                print(res)
            else:
                break



my_func_test()

my_main()
