##
#
#  图
#  1 图的变化
#  2 路径搜索  广度优先， 可以得到 最短的 路径
#
# 连接表  dict   方式保存  1 -> set(1,2,3)
#
#

import os
import sys
import copy
import time

base_data = {1: set([6]),
             2: set([6]),
             3: set([4, 5, 6, 15, ]),
             4: set([3, 5, 6]),
             5: set([3, 4, 6]),
             6: set([1, 2, 3, 4, 5, 7]),
             7: set([6, 8]),
             8: set([7, 9]),
             9: set([8, 12, 10]),
             10: set([9, 11]),
             11: set([10, 12]),
             12: set([11, 9, 13]),
             13: set([12, 15, 14]),
             14: set([13]),
             15: set([3, 13]),
             16: set([17, 18]),
             17: set([16, 18]),
             18: set([16, 17]),
             }


def my_print(x, end="\n"):
    if os.environ.get('DEBUG', None) or os.environ.get('TRACE', None):
        print(x, file=sys.stderr, end=end)
    else:
        pass


def my_print_trace(x, end="\n"):
    if os.environ.get('TRACE', None):
        print(x, file=sys.stderr, end=end)
    else:
        pass


def my_i(graph, x, y):
    if x in graph:
        graph[x].add(y)
    else:
        graph[x] = set([y])
    if y in graph:
        graph[y].add(x)
    else:
        graph[y] = set([x])


def my_d(graph, x, y):
    if x in graph:
        graph[x].remove(y)
    if y in graph:
        graph[y].remove(x)


def my_n(graph, x):
    return len(graph.get(x, set()))


def my_f(graph, x):
    s1 = graph.get(x, set())
    res = set()
    for y in s1:
        ss = graph.get(y, set())
        my_print("ss={0}".format(ss))
        res = res.union(ss)
        my_print("res={0}".format(res))
    res = res.difference(s1)
    my_print("res={0}".format(res))
    if x in res:
        res.remove(x)
    my_print("res={0}".format(res))
    return res


# 广度优先
def my_s_width(graph, x, y):
    my_print("line 91 x={0},y={1}".format(x, y))
    my_print("graph=\n{0}".format(graph))
    # 题目已知条件
    max_layer = 5
    path_list = [set([x])]
    node_set = set([x])
    if x == y:
        return [x]
    new_set = set([x])
    node_set = node_set.union(new_set)
    for i in range(max_layer):
        new_set_2 = set()
        for node in new_set:
            my_print("node={0}".format(node))
            friends = graph.get(node, set())
            my_print("friends={0}".format(friends))

            new_set_2 = new_set_2.union(friends)
            if y in friends:
                break
            my_print("new_set_2={0}".format(new_set_2))
        new_set_2 = new_set_2.difference(node_set)
        path_list.append(new_set_2)
        node_set = node_set.union(new_set_2)
        new_set = new_set_2
        my_print("node_set={0}".format(node_set))
        my_print("path_list={0}".format(path_list))
        if y in node_set:
            break
    return path_list


# 一层 一层扩展
#
def my_s(graph, x, y):
    my_print("line 92 x={0},y={1}".format(x, y))
    if x == y:
        return [x]
    else:

        paths = []

        my_s_inner(graph, x, y, [], 0, paths)

        my_print("paths=".format(paths))
        paths.sort(key=len)
        if len(paths) > 0:
            return paths[0]
        else:
            return [x]


def my_s_inner(graph, x, y, path, layer, paths):
    my_print("  " * layer + "layer={0} path={1},x={2},y={3}".format(layer, path, x, y))

    if x in path:
        return path
    else:
        friends = graph.get(x, set())
        my_print("  " * layer + "{1} 's  friends={0}".format(friends, x))
        if not friends:
            # del graph[x]
            return path
        elif y in friends:
            path.append(x)
            path.append(y)
            paths.append(path)
            return path
        else:
            for next_x in friends:
                if next_x not in path:
                    next_path = path.copy()
                    next_path.append(x)
                    my_print("  " * layer + " 138 next_path={0}".format(path))
                    new_path = my_s_inner(graph, next_x, y, next_path, layer + 1, paths)
                    my_print("  " * layer + "new_path={0}".format(new_path))
                    if len(new_path) > 0 and new_path[-1] == y:
                        my_print("  " * layer + "find path path={0}".format(new_path))
                        paths.append(new_path)
                    # return new_path
                else:
                    my_print("  " * layer + "next_x {0} in path {1}".format(next_x, path))
                    pass
            return path


def my_input():
    g = copy.deepcopy(base_data)
    while True:
        my_print("=====" * 20)
        my_print(g)
        my_print("=====" * 20)
        cmd = input()
        if cmd == "q":
            break
        elif cmd == "i":
            x = int(input())
            y = int(input())
            my_i(g, x, y)
        elif cmd == "d":
            x = int(input())
            y = int(input())
            my_d(g, x, y)
        elif cmd == "n":
            x = int(input())
            res = my_n(g, x)
            print(res)
        elif cmd == "f":
            x = int(input())
            res = my_f(g, x)
            print(len(res))
        elif cmd == "s":
            x = int(input())
            y = int(input())
            res = my_s(g, x, y)
            if len(res) == 1:
                print("Not connected")
            else:
                print(len(res) - 1)

    pass


def my_unit_test():
    g1 = copy.deepcopy(base_data)
    my_i(g1, 20, 10)
    my_i(g1, 20, 9)
    assert my_n(g1, 20) == 2
    assert my_f(g1, 20) == set([8, 11, 12])
    assert len(my_s_width(g1, 20, 20)) == len([20])
    assert len(my_s_width(g1, 20, 6)) == len([20, 9, 8, 7, 6])
    pass


def my_func_test():
    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    # my_res = my_run(input_data)
    # print(my_res)


if os.environ.get("UNIT", None):
    my_unit_test()
elif os.environ.get("FUNC", None):
    my_func_test()
else:
    my_main()
