class Digraph:

    def __init__(self, v_size):
        self.dic = {}
        for i in range(v_size):
            self.dic[i] = [].copy()
        pass

    def __str__(self):
        tmp = []
        for k, v in self.dic.items():
            s = "{0} -> {1}".format(k, v)
            tmp.append(s)
        return "\n".join(tmp)

    def add_edge(self, v, w):
        l1 = self.dic.get(v, [].copy())
        l1.append(w)
        self.dic[v] = l1

    def v(self):
        return list(self.dic.keys())

    def v_size(self):
        return len(self.dic)

    def e_size(self):
        return sum([len(x) for x in self.dic.values()])

    def adj(self, v):
        return self.dic.get(v, [])

    def out_degree(self, v):
        return len(self.dic.get(v, []))

    def in_degree(self, v):
        return len([x for x in self.dic.items() if v in x[1]])


def my_print(x, end="\n"):
    print(x, end=end)


def my_unit_test():
    v_size = 13
    g1 = Digraph(v_size)
    g1.add_edge(4, 2)
    g1.add_edge(2, 3)
    g1.add_edge(3, 2)
    g1.add_edge(6, 0)
    g1.add_edge(0, 1)
    g1.add_edge(0, 5)
    g1.add_edge(2, 0)
    g1.add_edge(11, 12)
    g1.add_edge(12, 9)
    g1.add_edge(9, 10)
    g1.add_edge(9, 11)
    g1.add_edge(7, 9)
    g1.add_edge(10, 12)
    g1.add_edge(11, 4)
    g1.add_edge(4, 3)
    g1.add_edge(3, 5)
    g1.add_edge(6, 8)
    g1.add_edge(8, 6)
    g1.add_edge(5, 4)
    g1.add_edge(7, 6)
    g1.add_edge(6, 4)
    g1.add_edge(6, 9)

    my_print(g1)

    assert 13 == g1.v_size()
    assert 22 == g1.e_size()


my_unit_test()
