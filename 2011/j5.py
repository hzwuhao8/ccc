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

    # 加入一棵子树
    def add_subtree(self, sub):
        self.sub_tree.append(sub)
        # 如何 对 所有的 节点的 layer 进行调整
        sub.update_layer(self.layer + 1)

    def update_layer(self, layer):
        self.layer = layer
        if not self.sub_tree:
            for t in self.sub_tree:
                t.update_layer(layer + 1)
            return
        else:
            return

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
        return tmp1 + tmp2

    def sub_tree_count(self):
        if self.sub_tree:
            tmp2 = 1
            for t in self.sub_tree:
                res = t.sub_tree_count()
                tmp2 = tmp2 * res

            return tmp2 + 1
        else:
            tmp1 = 2
            return tmp1


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


#
#
# 1 构造树
# 2 计算 所有可能的 子树的  数目;   这个 总数 好像 就是 所求的结果
# 3 或者通过穷举， 并 进行判断 是不是 合法的 树
#
#
#

def my_run(data):
    n = data[0]
    tree_list = list(range(0, n + 1))
    tree_list[1] = Tree(n)
    dic = {}
    tree_dic = {}
    for i in range(1, n + 1):
        dic[i] = []
        tree_dic[i] = Tree(i, [], 0)

    my_print("dic init={0}".format(dic))

    for i in range(1, n):
        index = data[i]
        my_print("index={0}".format(index))
        dic[index].append(i)
    my_print(dic)

    # 构造树
    # 如何进行循环？

    for k, v in dic.items():
        my_print(tree_dic[n])
        for sub in v:
            tree_dic[k].add_subtree(tree_dic[sub])
    my_print(tree_dic[n])
    my_print(tree_dic[n - 1])
    my_print(tree_dic[1])

    for k, v in tree_dic.items():
        my_print("i={0}, count={1}".format(k, v.sub_tree_count()))

    res = tree_dic[n].sub_tree_count()
    my_print(res)
    return res - 1

def my_input():
    n = int(input())
    data = [n]
    for i in range(1, n):
        data.append(int(input()))
    return data


def my_main():
    data = my_input()
    res = my_run(data)
    print(res)



my_unit_test()

my_main()
