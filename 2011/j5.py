import os


def my_print(x, end="\n"):
    if os.environ.get("DEBUG", ""):
        print(x, end=end)
    else:
        pass


class Tree:
    def __init__(self, v, sub_tree=[], layer=0):
        self.v = v
        self.sub_tree = sub_tree
        self.layer = layer

    def __repr__(self):
        my_str = "  " * self.layer + "{0},{1};{2}".format(self.v, [x.v for x in self.sub_tree], self.layer)
        return my_str

    def add_subtree(self, sub):
        self.sub_tree.append(sub)

    def add_node(self, v):
        t = Tree(v, sub_tree=[], layer=self.layer + 1)
        self.sub_tree.append(t)
        return t

    def get_all_sub_node(self):
        tmp1 = [x.v for x in self.sub_tree]
        my_print("tmp1={0}".format(tmp1))
        tmp2 = []
        for t in self.sub_tree:
            res = t.get_all_sub_node()
            my_print("res={0}".format(res))
            tmp2 = tmp2 + res
        my_print("tmp2={0}".format(tmp2))
        return (tmp1 + tmp2)


def my_unit_test():
    n = 4
    a = [0] * (n + 1)
    a[n] = Tree(n)
    my_print("a[{0}]={1}".format(n, a[n]))
    root = a[n]
    a[3] = a[n].add_node(3)
    my_print("a[{0}]={1}".format(3, a[3]))
    a[2] = a[n].add_node(2)
    my_print("a[{0}]={1}".format(2, a[2]))
    a[1] = a[3].add_node(1)
    my_print("a[{0}]={1}".format(1, a[1]))
    my_print("root={0}".format(root))
    for i in range(1, n + 1):
        my_print("a[{0}]={1}".format(i, a[i]))
    my_print(a[4].get_all_sub_node())
    dic = {}
    for i in range(1, n + 1):
        dic[i] = a[i].get_all_sub_node()
    my_print(dic)
    assert dic[1] == []
    assert dic[3] == [1]
    assert set(dic[4]) == set([1, 2, 3])


my_unit_test()
