# 需要 使用tree

import copy


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
        tree.layer += 1

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


my_unit_test_a()
