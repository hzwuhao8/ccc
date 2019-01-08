def my_print(x, end="\n"):
    print(x, end=end)


def is_intersection(position_list):
    return "safe"



def my_run_inner(position_list, cmd, steps):
    res = []
    if is_intersection(position_list) == "DANGER":
        # do nothing
        return res
    else:
        current = position_list[-1]
        x0, y0 = current
        x1, y1 = x0, y0
        if cmd == 'd':
            x1, y1 = x0, y0 - steps
        elif cmd == 'u':
            x1, y1 = x0, y0 + steps
        elif cmd == 'l':
            x1, y1 = x0 - steps, y0
        else:
            x1, y1 = x0 + steps, y0
        position_list.append((x1, y1))
        return [x1, y1, is_intersection(position_list)]


def my_run(position_list, cmd_str):
    cmd, length_str = cmd_str.split()
    my_print("cmd_str={0} cmd={1} length_str={2}".format(cmd_str, cmd, length_str))
    res_list = my_run_inner(position_list, cmd, int(length_str))
    return " ".join([str(x) for x in res_list])


def my_func_test():
    position_list = [(-1, -5)]
    assert my_run(position_list, "l 2") == "-3 -5 safe"
    assert my_run(position_list, "d 2") == "-3 -7 safe"
    assert my_run(position_list, "r 1") == "-2 -7 safe"

    position_list = [(-1, -5)]
    assert my_run(position_list, "r 2") == "1 -5 safe"
    assert my_run(position_list, "d 10") == "1 -15 DANGER"
    assert my_run(position_list, "r 4") == ""


my_func_test()
