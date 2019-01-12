# 1 显示 矩阵
# 2 处理被 C  控制的节点
# 3 广度优先 搜索， 得到 结果集
# 4 数据整理，输出结果
# 4 x 100  估计 递归 可以处理的

import copy


def my_print(x, end="\n"):
    # print(x, end=end)
    pass


def my_print_m(data):
    my_print("")
    for r in data:
        my_print("".join(r))
    my_print("")


data_str2 = """WWWWWWW
WD.L.RW
W.WCU.W
WWW.S.W
WWWWWWW"""

data_str1 = """WWWWW
W.W.W
WWS.W
WWWWW"""

mask_c = '/'


def my_func_test():
    assert my_run(data_str2) == [2, 1, 3, -1, -1, 1]

    assert my_run(data_str1) == [-1, 2, 1]


def data_str_to_data(data_str):
    data = []
    rows = data_str.split("\n")
    for r in rows:
        rr = list(r)
        data.append(rr)
    return data


def my_run(data_str):
    data = data_str_to_data(data_str)
    n, m = len(data), len(data[0])
    my_print_m(data)
    my_print("===mask===" * 10)
    my_mask(data)

    my_print_m(data)
    # quit()

    # 进行 广度优先 搜索， 取到所有可以达到的 点
    next_node_list = []
    p = my_find_s(data)
    if not p:
        node_dic = {}
    else:
        next_node_list.append(p)
        node_dic = {p: ''}

        my_search(data, 0, next_node_list, node_dic)
        data2 = copy.deepcopy(data)
        for i, j in node_dic:
            if data2[i][j] == '.':
                data2[i][j] = 'X'

        my_print_m(data)

        my_print_m(data2)

    # 从 node_dic 中提取数据
    res = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == mask_c:
                res.append(-1)
            if data[i][j] == '.':
                if (i, j) in node_dic:
                    res.append(node_dic[(i, j)].count('.'))
                else:
                    res.append(-1)
    my_print("res={0}".format(res))
    return res
    pass


o_op_list = ['L', 'R', 'U', 'D']


# 将 C 控制的 设置为M
def my_mask(data):
    n = len(data)
    m = len(data[0])
    c_dic = {}
    for i in range(n):
        for j in range(m):
            c = data[i][j]
            if c == 'C':
                my_print("(i,j)=({0},{1})".format(i, j))
                c_dic[(i, j)] = c

    for (i, j), v in c_dic.items():
        # 处理  j 列   up down
        for x in range(i - 1, -1, -1):
            my_c = data[x][j]
            # my_print("[{0}][{1}]={2}".format(x, j, my_c))
            if my_c == 'W' or my_c == 'C':
                break
            elif my_c in o_op_list:
                continue
            elif my_c == 'S':
                data[x][j] = 's'
            else:
                data[x][j] = mask_c

        # my_print_m(data)

        for x in range(i + 1, n):
            my_c = data[x][j]
            # my_print("[{0}][{1}]={2}".format(x, j, my_c))
            if my_c == 'W' or my_c == 'C':
                break
            elif my_c in o_op_list:
                continue
            elif my_c == 'S':
                data[x][j] = 's'
            else:
                data[x][j] = mask_c
        # my_print_m(data)
        # columns left , right
        for x in range(j - 1, -1, -1):
            my_c = data[i][x]
            if my_c == 'W' or my_c == 'C':
                break
            elif my_c in o_op_list:
                continue
            elif my_c == 'S':
                data[i][x] = 's'
            else:
                data[i][x] = mask_c
        # my_print_m(data)
        for x in range(j + 1, m, 1):
            my_c = data[i][x]
            if my_c == 'W' or my_c == 'C':
                break
            elif my_c in o_op_list:
                continue
            elif my_c == 'S':
                data[i][x] = 's'
            else:
                data[i][x] = mask_c
        # my_print_m(data)

    pass


def my_search(data, layer, next_node_list, node_dic):
    my_print("  " * layer + "next_node_list={0} node_set={1}".format(next_node_list, node_dic))
    while True:
        if not next_node_list:
            my_print("处理完成")
            return
        layer = layer + 1

        new_next_node_list = []
        # if layer > 10:
        #     print("ERROR layer={0}".format(layer))

        for node in next_node_list:
            tmp_list, my_c = my_get_next_list(data, node)
            for new_node in tmp_list:
                if new_node in node_dic:
                    pass
                else:
                    new_next_node_list.append(new_node)
                    node_dic[new_node] = node_dic[node][:-1] + my_c + my_get_c(data, new_node)
        my_print("  " * layer + "新的 需要处理的new_next_node_list={0}".format(new_next_node_list))
        next_node_list = new_next_node_list


def my_get_next_list(data, node):
    n = len(data)
    m = len(data[0])
    i, j = node
    # 搜素 周围的4个点， 是否是可以移动的
    # 和当前的点有关系
    res = []
    my_c = data[i][j]
    # my_print("__157__  {0},{1} = {2}".format(i, j, my_c))
    if my_c == 'W' or my_c == mask_c or my_c == "C":
        my_print("__166__  {0},{1} = {2}".format(i, j, my_c))
        print("__167__ERROR")
        return []
    elif my_c == "L":
        if j > 1 and is_get_in(data, i, j - 1):
            res.append((i, j - 1))
    elif my_c == "R":
        if j < m - 1 and is_get_in(data, i, j + 1):
            res.append((i, j + 1))
    elif my_c == "U":
        if i > 1 and is_get_in(data, i - 1, j):
            res.append((i - 1, j))
    elif my_c == "D":
        if i < n - 1 and is_get_in(data, i + 1, j):
            res.append((i + 1, j))
    elif my_c == "." or my_c == 'S':
        if j > 1 and is_get_in(data, i, j - 1):
            res.append((i, j - 1))
        if j < m - 1 and is_get_in(data, i, j + 1):
            res.append((i, j + 1))
        if i > 1 and is_get_in(data, i - 1, j):
            res.append((i - 1, j))
        if i < n - 1 and is_get_in(data, i + 1, j):
            res.append((i + 1, j))
    else:
        my_print("__191__  {0},{1} = {2}".format(i, j, my_c))
        print("__192__ ERROR")
    return res, my_c


# 节点是可以进入的


def is_get_in(data, i, j):
    my_c = data[i][j]
    # my_print("__195__ my_c={0}".format(my_c))
    if my_c == '.':
        return True
    elif my_c in o_op_list:
        return True
    else:
        return False


def my_find_s(data):
    n, m = len(data), len(data[0])
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'S':
                return i, j


def my_get_c(data, node):
    i, j = node
    return data[i][j]


def my_unit_test():
    data1 = data_str_to_data(data_str2)
    my_print_m(data1)
    assert not is_get_in(data1, 0, 0)
    assert is_get_in(data1, 1, 1)
    assert is_get_in(data1, 1, 2)
    assert is_get_in(data1, 2, 1)
    assert not is_get_in(data1, 2, 3), "C"
    assert not is_get_in(data1, 3, 4), "S"

    assert my_get_next_list(data1, (1, 1)) == ([(2, 1)], 'D')
    assert my_get_next_list(data1, (1, 5)) == ([], 'R')

    assert my_get_next_list(data1, (2, 5)) == ([(2, 4), (1, 5), (3, 5)], '.')

    assert my_find_s(data1) == (3, 4)


# my_unit_test()
# my_func_test()


def my_main():
    n, m = [int(x) for x in input().split()]
    data_str_list = []
    for i in range(n):
        data_str_list.append(input())
    data_str = "\n".join(data_str_list)
    res = my_run(data_str)
    for x in res:
        print(x)


my_main()
