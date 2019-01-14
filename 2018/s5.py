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
    assert my_run(my_str1) == 3

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

    def my_one_p(my_p_rule, p_index):
        a, b, c = my_p_rule
        rule_id = "p{0}".format(p_index)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                key1 = ((i, a), (j, b))

                if (i, a) == (j, b):
                    t = remove_path_dic.get(key1, [])
                    t.append((rule_id, c))
                    remove_path_dic[key1] = t
                elif key1 in path_dic:
                    r, z = path_dic.get(key1)
                    if z > c:
                        path_dic[key1] = (rule_id, c)
                        t = remove_path_dic.get(key1, [])
                        t.append((rule_id, z))
                        remove_path_dic[key1] = t

                    else:
                        t = remove_path_dic.get(key1, [])
                        t.append((rule_id, c))
                        remove_path_dic[key1] = t
                else:
                    path_dic[key1] = (rule_id, c)

        pass

    def my_one_q(my_q_rule, q_index):
        x, y, z = my_q_rule
        rule_id = "q{0}".format(q_index)
        if x > y:
            x, y = y, x
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                key1 = ((x, i), (y, j))

            if (x, i) == (y, j):
                t = remove_path_dic.get(key1, [])
                t.append((rule_id, z))
                remove_path_dic[key1] = t

            elif key1 in path_dic:
                r, c = path_dic[key1]
                if z >= c:
                    t = remove_path_dic.get(key1, [])
                    t.append((rule_id, z))
                    remove_path_dic[key1] = t

                else:
                    t = remove_path_dic.get(key1, [])
                    t.append((rule_id, c))
                    remove_path_dic[key1] = t
                    path_dic[key1] = (rule_id, z)
            else:
                path_dic[key1] = (rule_id, z)

        pass

    for index in range(len(data_p)):
        p_rule = data_p[index]
        my_one_p(p_rule, index + 1)
        my_print("path_dic={0} len={1}".format(path_dic, len(path_dic)))
        my_print("remove_path_dic={0}".format(remove_path_dic))
        my_print("total={0}".format(total))

    for index in range(len(data_q)):
        q_rule = data_q[index]
        my_one_q(q_rule, index + 1)
    path_dic_list = list(path_dic.items())
    path_dic_list.sort()

    my_print("path_dic=\n{0} len={1}".format("\n".join([str(x) for x in path_dic_list]), len(path_dic)))
    my_print("remove_path_dic={0}".format(remove_path_dic))

    for k, v in remove_path_dic.items():
        total += sum([x[1] for x in v])
    my_print("total={0}".format(total))

    return total


my_func_test()
