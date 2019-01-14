#
# 题目理解
# 城市  (e,f)  来表示
# flights e 可以取全集， f 固定
# portals  e 固定，  f 可以取全集
# 原来存在 很多 重复的 路径
# 目标是 只保留  权重 最小的 全联通图，  不需要  自己到 自己 的  联通

# 这样 理解，不知道 对不对


# 处理方法 读取 初始数据
# P Q
# 读取 一条 规则， 然后 输出 所有可能的 路径 ； 然后和 已有的比较， 只保留最小能量的路径   移除 其他路径， 并进行 记录
# 最后可以得到 能够  节省的 能量


def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_func_test():
    my_str1 = """
    2 2 1 2
    1 2 1
    2 1 1
    2 1 1
"""
    assert my_run(my_str1) == 6

    my_str2 = """
     2 3 4 1
     2 3 5 
     3 2 7 
     1 2 6 
     1 1 8 
     2 1 5"""
    assert my_run(my_str2) == 41


def str_to_data(my_str):
    str_list = my_str.strip().split("\n")
    my_print("str_list={0}".format(str_list))
    n, m, p, q = [int(x) for x in str_list[0].strip().split()]
    my_print("n={0},m={1},p={2},q={3}".format(n, m, p, q))
    data_p = []
    for i in range(1, p + 1):
        data_p.append([int(x) for x in str_list[i].split()])
    my_print("data_p={0}".format(data_p))
    data_q = []
    for i in range(p + 1, p + 1 + q):
        data_q.append([int(x) for x in str_list[i].split()])
    my_print("data_q={0}".format(data_q))
    return n, m, data_p, data_q


def my_run(my_str):
    n, m, data_p, data_q = str_to_data(my_str)
    path_dic = {}
    remove_path_dic = {}
    total = 0

    def reach_p(c1, c2, p_rule):
        e1, f1 = c1
        e2, f2 = c2

        a, b, c = p_rule
        if (f1 == a and f2 == b) or (f1 == b and f2 == a):
            return True, c
        else:
            return False, c

    def reach_q(c1, c2, q_rule):
        e1, f1 = c1
        e2, f2 = c2
        x, y, z = q_rule

        if (e1 == x and e2 == y) or (e1 == y and e2 == x):
            return True, z
        else:
            return False, z

    # 共有 nxm 个城市
    city_list = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            city_list.append((i, j))
    my_print("city_list={0}".format(city_list))

    for index, c1 in enumerate(city_list):
        for c2 in city_list[index:]:
            key = (c1, c2)
            my_print(key)
            if c1 == c2:
                for p_index, p_rule in enumerate(data_p):
                    flag, distance = reach_p(c1, c2, p_rule)
                    if flag:
                        tmp = remove_path_dic.get(key, [])
                        tmp.append(("p{0}".format(p_index), distance))
                        remove_path_dic[(c1, c2)] = tmp
                    else:
                        pass

                for q_index, q_rule in enumerate(data_q):
                    flag, distance = reach_q(c1, c2, q_rule)
                    if flag:
                        tmp = remove_path_dic.get(key, [])
                        tmp.append(("q{0}".format(q_index), distance))
                        remove_path_dic[(c1, c2)] = tmp
                    else:
                        pass
            else:
                flag_p_total = False
                for p_index, p_rule in enumerate(data_p):
                    flag_p, distance = reach_p(c1, c2, p_rule)
                    flag_p_total = flag_p_total or flag_p
                    if flag_p:
                        if key not in path_dic:
                            path_dic[key] = ("p{0}".format(p_index), distance)
                        else:
                            # 和已经有的 权重比较 保留较小的权重
                            t1, z = path_dic[key]
                            if z > distance:
                                tmp = remove_path_dic.get(key, [])
                                tmp.append((t1, z))
                                remove_path_dic[(c1, c2)] = tmp
                                path_dic[key] = ("p{0}".format(p_index), distance)
                            else:
                                tmp = remove_path_dic.get(key, [])
                                tmp.append(("p{0}".format(p_index), distance))
                                remove_path_dic[(c1, c2)] = tmp

                    else:
                        pass
                flag_q_total = False
                for q_index, q_rule in enumerate(data_q):
                    flag_q, distance = reach_q(c1, c2, q_rule)
                    flag_q_total = flag_q_total or flag_q
                    if flag_q:
                        if key not in path_dic:
                            path_dic[key] = ("q{0}".format(q_index), distance)
                        else:
                            # 和已经有的 权重比较 保留较小的权重
                            t1, z = path_dic[key]
                            if z > distance:
                                tmp = remove_path_dic.get(key, [])
                                tmp.append((t1, z))
                                remove_path_dic[(c1, c2)] = tmp
                                path_dic[key] = ("q{0}".format(q_index), distance)
                            else:
                                tmp = remove_path_dic.get(key, [])
                                tmp.append(("q{0}".format(q_index), distance))
                                remove_path_dic[(c1, c2)] = tmp

                    else:
                        pass
                if not (flag_p_total or flag_q_total):
                    my_print("ERROR ({0},{1}) not found , p {2} q {3}".format(c1, c2, flag_p_total, flag_q_total))

    path_dic_list = list(path_dic.items())
    path_dic_list.sort()

    my_print("path_dic=\n{0} len={1}".format("\n".join([str(x) for x in path_dic_list]), len(path_dic)))

    remove_dic_list = list(remove_path_dic.items())
    remove_dic_list.sort()
    my_print("remove_path_dic=\n{0}".format("\n".join([str(x) for x in remove_dic_list])))

    for k, v in remove_path_dic.items():
        total += sum([x[1] for x in v])
    my_print("total={0}".format(total))

    return total


my_func_test()
