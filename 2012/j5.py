# 广度优先
#
import copy


def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_run(n, init_data):
    if is_goal(init_data):
        return 0
    else:
        layer = 0
        node_set = set()
        my_run_inner(n, init_data, layer, node_set)

    pass


def my_run_inner(n, init_data, layer, node_set):
    pass


# 得到 所有可能的移动
def get_next_move(n, data):
    res = []
    for f in range(n):
        if is_validate_move(data, f + 1):
            res.append((f, f + 1))
        elif is_validate_move(data, f - 1):
            res.append(f, f - 1)
    return res


def data_to_str(data):
    data2 = copy.deepcopy(data)
    res_str = []
    for x in data2:
        x.reverse()
        tmp_str = "".join(["{0}".format(i) for i in x])
        res_str.append("{0:^10}".format(tmp_str))
    my_str = ",".join(res_str)
    return my_str


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


# 执行实际的移动
# 状态用 字符串表示 比较简单
def do_move(data, f, t, node_set=set()):
    if is_validate_move(data, f, t):
        coin = data[f].pop()
        data[t].append(coin)
        pass

    else:
        pass


def is_goal(data):
    tmp_data = sum(data, [])
    tmp2 = sorted(tmp_data)
    return tmp2 == tmp_data


def my_unit_test():
    my_print(data_to_str([[1], [2], [3]]))
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

    data = [[3], [2], [1]]
    my_print(data_to_str(data))
    do_move(data, 2, 1)
    my_print(data_to_str(data))
    assert data == [[3], [2, 1], []]
    do_move(data, 1, 0)
    my_print(data_to_str(data))
    assert data == [[3, 1], [2], []]
    do_move(data, 1, 2)
    my_print(data_to_str(data))
    assert data == [[3, 1], [], [2]]


def my_func_test():
    assert my_run(3, [[3], [2], [1]]) == 20
    assert my_run(2, [[2], [1]]) == -1


my_unit_test()
my_func_test()
