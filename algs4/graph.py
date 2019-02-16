class Graph:

    def __init__(self, v_size):
        self.dic = {}
        for i in range(v_size):
            self.dic[i] = [].copy()
        pass

    def add_edge(self, v, w):
        l1 = self.dic.get(v, [])
        l1.append(w)
        self.dic[v] = l1

        l2 = self.dic.get(w, [])
        l2.append(v)
        self.dic[w] = l2
        pass

    def v_size(self):
        return len(self.dic)

    def e_size(self):
        return sum([len(x) for x in self.dic.values()]) // 2

    def adj(self, v):
        return self.dic.get(v, [])

    def __str__(self):
        tmp = []
        for k, v in self.dic.items():
            s = "{0} -> {1}".format(k, v)
            tmp.append(s)
        return "\n".join(tmp)


def my_print(x, end="\n"):
    print(x, end=end)


def my_unit_test():
    v_size = 4
    g1 = Graph(v_size)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    my_print(g1)
    assert v_size == g1.v_size()
    assert 2 == g1.e_size()


my_unit_test()
