# 广度优先
#
import copy


def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_run(n, init_list):
    pass


def my_print_data(data):
    data2 = copy.deepcopy(data)
    my_print("")
    for x in data2:
        x.reverse()
        my_print("".join(["{0:^5}".format(i) for i in x]), end=" ")
    my_print("")


# 移动 f 位置的 coin 到 t 位置
def is_validate_move(data, f, t):
    if abs(f - t) != 1:
        return False
    elif t >= len(data) or t < 0:
        return False
    else:
        if not data[t]:
            return True
        else:
            if data[f][-1] < data[t][-1]:
                return True
            else:
                return False


def is_goal(data):
    tmp_data = sum(data, [])
    tmp2 = sorted(tmp_data)
    return tmp2 == tmp_data


def my_unit_test():
    my_print_data([[1], [2], [3]])
    assert is_goal([[1], [2], [3]])
    assert is_goal([[1], [2], [3], [4]])
    assert not is_goal([[1], [5], [2], [3], [4]])

    data = [[3], [2], [1]]
    assert is_validate_move(data, 2, 1)
    assert not is_validate_move(data, 0, 1)
    assert not is_validate_move(data, 0, -1)
    assert not is_validate_move(data, 0, 2)
    assert not is_validate_move(data, 1, 2)

    data = [[2, 1], [3], []]
    assert is_validate_move(data, 1, 2)

    data = [[3, 1], [], [2]]
    assert is_validate_move(data, 0, 1)
    data = [[3, 1], [], [2]]
    assert not is_validate_move(data, 0, 2)


def my_func_test():
    assert my_run(3, [3, 2, 1]) == 20
    assert my_run(2, [2, 1]) == -1


my_unit_test()
my_func_test()
