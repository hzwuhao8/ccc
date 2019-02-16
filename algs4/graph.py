class Graph:

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
        l1 = self.dic.get(v, [])
        l1.append(w)
        self.dic[v] = l1

        l2 = self.dic.get(w, [])
        l2.append(v)
        self.dic[w] = l2

    def v_size(self):
        return len(self.dic)

    def e_size(self):
        return sum([len(x) for x in self.dic.values()]) // 2

    def adj(self, v):
        return self.dic.get(v, [])

    def degree(self, v):
        return len(self.dic.get(v, []))

    def max_degree(self):
        return max([len(x) for x in self.dic.values()])

    def average_degree(self):
        return 2.0 * self.v_size() / self.e_size()

    def number_of_self_loops(self):
        return len([x for x in self.dic.items() if x[0] in x[1]])


def my_print(x, end="\n"):
    print(x, end=end)


def my_unit_test():
    v_size = 13
    g1 = Graph(v_size)
    g1.add_edge(0, 5)
    g1.add_edge(4, 3)
    g1.add_edge(0, 1)
    g1.add_edge(9, 12)
    g1.add_edge(6, 4)
    g1.add_edge(5, 4)
    g1.add_edge(0, 2)
    g1.add_edge(11, 12)
    g1.add_edge(9, 10)
    g1.add_edge(0, 6)
    g1.add_edge(7, 8)
    g1.add_edge(9, 11)
    g1.add_edge(5, 3)
    g1.add_edge(13, 13)

    my_print(g1)
    assert 14 == g1.v_size()
    assert 14 == g1.e_size()
    assert 4 == g1.degree(0)
    assert 4 == g1.max_degree()
    assert 1 == g1.number_of_self_loops()


my_unit_test()
