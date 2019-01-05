# 需要 使用tree

import copy
import time


def my_print(x, end="\n"):
    print(x, end=end)
    pass


class Node:
    def __init__(self, action, static_value=0):
        self.action = action
        self.static_value = static_value

    def __repr__(self):
        return "{0}, {1}".format(self.action, self.static_value)


class Tree:
    def __init__(self, node, layer=0):
        self.node = node
        self.layer = layer
        self.sub_tree = []

    def add_sub_tree(self, tree):
        self.sub_tree.append(tree)
        tree.layer = self.layer + 1

    def add_node(self, node):
        tmp_tree = Tree(node, self.layer + 1)
        self.sub_tree.append(tmp_tree)

    def __repr__(self):
        my_str = "  " * self.layer + "{0} layer={1}\n".format(self.node, self.layer)
        my_str2 = ""
        for t in self.sub_tree:
            my_str2 += str(t)
        return my_str + my_str2


def my_unit_test():
    n0 = Node("a", 1)
    t0 = Tree(n0, 1)
    my_print("n0={0}".format(n0))
    my_print("t0={0}".format(t0))

    n10 = Node("b10", -1)
    t10 = Tree(n10, 1)
    t0.add_sub_tree(t10)
    my_print("t1={0}".format(t10))

    n11 = Node("b11", 1)
    t11 = Tree(n11, 1)

    t0.add_sub_tree(t11)

    n100 = Node("c100", 1)
    t10.add_node(n100)

    n1000 = Node("d1000", 10)
    t10.sub_tree[0].add_node(n1000)
    my_print("t0=\n{0}".format(t0))

    # my_print("t10=\n{0}".format(t10))


def my_unit_test_a():
    root = Tree(Node("A", 0), 0)
    root.add_node(Node("B1", 0))
    root.add_node(Node("B2", 0))

    root.sub_tree[0].add_node(Node("C1", 0))
    root.sub_tree[0].sub_tree[0].add_node(Node("D1", 0))
    root.sub_tree[0].sub_tree[0].sub_tree[0].add_node(Node("E1", 10))
    root.sub_tree[0].sub_tree[0].sub_tree[0].add_node(Node("E2", 99999))
    root.sub_tree[0].sub_tree[0].add_node(Node("D2", 0))
    root.sub_tree[0].sub_tree[0].sub_tree[1].add_node(Node("E3", 5))
    root.sub_tree[0].add_node(Node("C2", 0))
    root.sub_tree[0].sub_tree[1].add_node(Node("D3", 0))
    root.sub_tree[0].sub_tree[1].sub_tree[0].add_node(Node("E4", -10))

    root.sub_tree[1].add_node(Node("C3", 0))
    root.sub_tree[1].sub_tree[0].add_node(Node("D4", 0))
    root.sub_tree[1].sub_tree[0].sub_tree[0].add_node(Node("E5", 7))
    root.sub_tree[1].sub_tree[0].sub_tree[0].add_node(Node("E6", 5))
    root.sub_tree[1].sub_tree[0].add_node(Node("D5", 0))
    root.sub_tree[1].sub_tree[0].sub_tree[1].add_node(Node("E7", -99999))
    root.sub_tree[1].add_node(Node("C4", 0))
    root.sub_tree[1].sub_tree[1].add_node(Node("D6", 0))
    root.sub_tree[1].sub_tree[1].sub_tree[0].add_node(Node("E8", -7))
    root.sub_tree[1].sub_tree[1].sub_tree[0].add_node(Node("E9", -5))

    my_print(root)

    root2 = copy.deepcopy(root)

    my_min_max(root2, "max")
    my_print("===" * 10)
    my_print(root2)

    my_print("my_path={0}".format(my_path(root2)))


def my_min_max(tree, flag="max"):
    if len(tree.sub_tree) == 0:
        return tree.node.static_value
    else:
        if flag == "max":
            value_list = [my_min_max(t, "min") for t in tree.sub_tree]
            tmp_value = max(value_list)
            tree.node.static_value = tmp_value
            return tmp_value
        else:
            value_list = [my_min_max(t, "max") for t in tree.sub_tree]
            tmp_value = min(value_list)
            tree.node.static_value = tmp_value
            return tmp_value


def my_min_max_a_b(tree, flag="max", a=[-9999], b=[9999]):
    if a[0] > b[0]:
        return;
    if len(tree.sub_tree) == 0:
        return tree.node.static_value
    else:
        if flag == "max":

            value_list = [my_min_max_a_b(t, "min", a, b) for t in tree.sub_tree]
            tmp_value = max(value_list)
            tree.node.static_value = tmp_value
            if tmp_value > a[0]:
                a[0] = tmp_value
            return tmp_value
        else:
            value_list = [my_min_max_a_b(t, "max", a, b) for t in tree.sub_tree]
            tmp_value = min(value_list)
            tree.node.static_value = tmp_value
            if tmp_value < b[0]:
                b[0] = tmp_value
            return tmp_value


# 计算完成后显示 计算 路径
def my_path(tree, path=[]):
    if not tree.sub_tree:
        path.append(tree.node.action)
        return path
    else:
        for t in tree.sub_tree:
            if t.node.static_value == tree.node.static_value:
                path.append(tree.node.action)
                my_path(t, path)
                return path


# 所有合法的取法
VALID = ((2, 1, 0, 2),
         (1, 1, 1, 1),
         (0, 0, 2, 1),
         (0, 3, 0, 0),
         (1, 0, 0, 1),
         )

R = "Roland"
P = "Patrick"

TEST_DATA = [
    [0, 2, 0, 2],
    [1, 3, 1, 3],
    [1, 5, 0, 3],
    [3, 3, 3, 3],
    [8, 8, 6, 7],
    [8, 8, 8, 8],
]

TEST_RESULT = [R, P, R, R, R, P]


def is_validate(v, data):
    # my_print("v={0} data={1}".format(v, data))
    tmp = [data[i] - v[i] >= 0 for i in range(4)]
    return tmp.count(True) == 4


# 得到 所有可能的 取法
def get_all_method(data):
    # my_print("get_all_method({0})".format(data))
    res = []
    for v in VALID:
        if is_validate(v, data):
            res.append(v)
    return set(res)
    pass


def find_all_path(data, layer=0, tree=Tree(Node("root"))):
    my_print("  " * layer + "layer={0} data={1}  tree={2}".format(layer, data, tree))
    steps = get_all_method(data)
    if not steps:
        if layer % 2 == 1:
            tree.add_node(Node(P, 1))
        else:
            tree.add_node(Node(R, -1))

        return tree
        pass
    else:
        for step in steps:
            next_data = [data[i] - step[i] for i in range(4)]
            t = Tree(Node(step))
            tree.add_sub_tree(t)
            find_all_path(next_data, layer + 1, t)


def find_all_path_a_b(data, layer=0, tree=Tree(Node("root")), a=[-9999], b=[9999]):
    my_print("  " * layer + "layer={0} data={1}  tree={2}".format(layer, data, tree))
    if a[0] > b[0]:
        return tree
    if tree.node.static_value == -1:
        return tree
    steps = get_all_method(data)
    if not steps:
        if layer % 2 == 1:
            tree.add_node(Node(P, 1))
        else:
            tree.add_node(Node(R, -1))
            # 能够 到达 这里的 都不用选择吗？
            # 至少 他的上一层 是不用再考虑了
            tree.node.static_value = -1

        return tree
        pass
    else:
        # 这一步可以 计算 a,b
        tmp_list = []
        for step in steps:
            next_data = [data[i] - step[i] for i in range(4)]
            t = Tree(Node(step))
            tree.add_sub_tree(t)
            find_all_path_a_b(next_data, layer + 1, t, a, b)
            tmp_list.append(t)
        #对 a b 进行修正
        val_list = [t.node.static_value for t in tmp_list]
        if layer % 2 == 0:
            max_val = max(val_list)
            tree.node.static_value = max_val
        else:
            min_val = min(val_list)
            tree.node.static_value = min_val


def my_run(data):
    s1 = time.time()

    tree = Tree(Node("root"))
    find_all_path_a_b(data, 0, tree)
    my_print("tree={0}".format(tree))
    root2 = copy.deepcopy(tree)
    s2 = time.time()
    # my_min_max_a_b(root2, "max")
    s3 = time.time()
    my_print(root2)
    my_print("my_path={0}".format(my_path(root2)))
    s4 = time.time()

    print("search:{0} min_max={1}".format(s2 - s1, s3 - s2))
    if root2.node.static_value == 1:
        return P
    else:
        return R


def my_func_test():
    for i in range(0, 5):
        print(TEST_DATA[i])
        assert my_run(TEST_DATA[i]) == TEST_RESULT[i], my_run(TEST_DATA[i])

    pass


# my_unit_test_a()
my_func_test()
