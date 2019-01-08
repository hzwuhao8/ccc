# 广度优先
#
import copy


def my_print(x, end="\n"):
    # print(x, end=end)
    pass


def my_run(n, init_data):
    if is_goal(init_data):
        return 0
    else:
        layer = 0
        node_set = set([data_to_str(init_data)])
        my_print("start node_set={0}".format(node_set))
        next_data = [init_data]
        res = my_run_inner(n, layer, node_set, next_data)
        return res
    pass


# 广度优先？如何 体现
def my_run_inner(n, layer, node_set, next_data):
    my_print("next_data={0}".format(next_data))
    for i in range(30000):
        my_print("layer={0} node_set={1}\n\n".format(layer, node_set))
        layer = layer + 1
        new_next_data = []
        # my_print("  " * layer + "node_set=\n{0}\n\n".format(node_set))
        if not next_data:
            my_print("  " * layer + ",没有新的状态了 已经无路可走了")
            return -1
        else:
            for data in next_data:
                # my_print("  " * layer + "data={0}".format(data_to_str(data)))
                next_steps = get_next_move(n, data)
                my_print("  " * layer + "next_steps={0}".format(next_steps))
                if not next_steps:
                    my_print("  " * layer + "已经无路可走了")
                    return -1
                else:
                    for f, t in next_steps:
                        # my_print("  " * layer + "begin move f={0},t={1}, data={2}".format(f, t, data_to_str(data)))
                        # my_print("  " * layer + "data={0}".format(data))
                        if try_move(data, f, t, node_set):
                            data_orig = copy.deepcopy(data)
                            do_move(data_orig, f, t, node_set)
                            # my_print("  " * layer + "move f={0},t={1}, data={2}".format(f, t, data_to_str(data_orig)))
                            if is_goal(data_orig):
                                return layer
                            else:
                                data_str = data_to_str(data_orig)
                                if data_str not in node_set:
                                    new_next_data.append(data_orig)
                                    node_set.add(data_str)
                        else:
                            pass
                            # my_print("  " * layer + "已经存在的状态 f={0},t={1}".format(f, t))
            # my_run_inner(n, layer + 1, node_set, next_data)
        next_data = new_next_data
        # my_print("  " * layer + "new_next_data=\n{0}".format("\n".join([data_to_str(x) for x in new_next_data])))
        pass


# 得到 所有可能的移动
def get_next_move(n, data):
    my_print("data={0}".format(data))
    res = []
    for f in range(n):
        if is_validate_move(data, f, f + 1):
            res.append([f, f + 1])
        else:
            pass
            # my_print("非法 f={0},t={1}".format(f, f + 1))
        if is_validate_move(data, f, f - 1):
            res.append([f, f - 1])
        else:
            pass
            # my_print("非法 f={0},t={1}".format(f, f - 1))
    return res


def data_to_str(data):
    data2 = copy.deepcopy(data)
    res_str = []
    for x in data2:
        x.reverse()
        tmp_str = "".join(["{0}".format(i) for i in x])
        res_str.append("{0:^5}".format(tmp_str))
    my_str = ",".join(res_str)
    return my_str


# 移动 f 位置的 coin 到 t 位置
def is_validate_move(data, f, t):
    if abs(f - t) != 1:
        return False
    elif t >= len(data) or t < 0:
        return False
    else:
        if not data[f]:
            return False
        elif not data[t]:
            return True
        else:
            if data[f][-1] < data[t][-1]:
                return True
            else:
                return False


# 移动尝试，如果已经在 已有的状态中， 就不要移动了
def try_move(data_orig, f, t, node_set):
    data = copy.deepcopy(data_orig)
    if is_validate_move(data, f, t):
        coin = data[f].pop()
        data[t].append(coin)
        state_str = data_to_str(data)
        return state_str not in node_set

    else:
        return False


# 执行实际的移动
# 状态用 字符串表示 比较简单
# 如何 避免 直接 退回到上一步？

def do_move(data, f, t, node_set):
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
    node_set = set()
    my_print(data_to_str(data))
    do_move(data, 2, 1, node_set)
    my_print(data_to_str(data))
    assert data == [[3], [2, 1], []]
    do_move(data, 1, 0, node_set)
    my_print(data_to_str(data))
    assert data == [[3, 1], [2], []]
    do_move(data, 1, 2, node_set)
    my_print(data_to_str(data))
    assert data == [[3, 1], [], [2]]

    # 所有可能的移动
    data = [[3], [2], [1]]
    res = get_next_move(3, data)
    my_print("get_next_move={0}".format(res))
    assert res == [[1, 0], [2, 1]]

    data = [[], [2, 1], [3]]
    res = get_next_move(3, data)
    my_print("get_next_move={0}".format(res))
    assert res == [[1, 2], [1, 0]]

    data = [[3, 2, 1], [], []]
    res = get_next_move(3, data)
    my_print("get_next_move={0}".format(res))
    assert res == [[0, 1]]


def my_func_test():
    my_print("====" * 30)
    data = [[2], [1]]
    my_print(data_to_str(data))
    assert my_run(2, data) == -1

    my_print("====" * 30)
    data = [[3], [2], [1]]
    my_print(data_to_str(data))
    assert my_run(3, data) == 20


my_unit_test()
#my_func_test()


def my_main():
    while True:
        xx = int(input())
        if xx == 0:
            break
        else:
            data_str = input()
            dd = [int(x) for x in data_str.split()]
            data = []
            for x in dd:
                data.append([x])
            my_print(data)

            res = my_run(xx, data)
            #print(res)
            if res == -1:
                print("IMPOSSIBLE")
            else:
                print(res)


my_main()
