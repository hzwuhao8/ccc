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


class DepthFirstSearch:
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = {}
        self.edge_to = {}
        # self.dfs(g, s)
        self.dfs_stack()
        my_print("marked={}".format(self.marked))
        my_print("edge_to={}".format(self.edge_to))

    def has_path_to(self, v):
        return self.marked.get(v, False)

    def paths(self, v):
        tmp = []
        if self.has_path_to(v):
            current = v
            tmp.append(current)
            while current != self.s:
                current = self.edge_to[current]
                tmp.append(current)

        tmp.reverse()
        return tmp

    def dfs(self, g, v):
        self.marked[v] = True
        for w in g.adj(v):
            if not self.marked.get(w, False):
                self.dfs(g, w)
                self.edge_to[w] = v

    def dfs_stack(self):
        stack = list()
        stack.append(self.s)
        self.marked[self.s] = True
        while stack:
            v = stack.pop()
            for w in self.g.adj(v):
                if not self.marked.get(w, False):
                    stack.append(w)
                    self.marked[w] = True
                    self.edge_to[w] = v


class BreadthFirstSearch:
    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = {}
        self.edge_to = {}
        self.dist_to = {}
        self.bfs(g, s)
        my_print("marked={}".format(self.marked))
        my_print("edge_to={}".format(self.edge_to))
        my_print("dist_to={}".format(self.dist_to))

    def has_path_to(self, v):
        return self.marked.get(v, False)

    def paths(self, v):
        tmp = []
        if self.has_path_to(v):
            current = v
            tmp.append(current)
            while current != self.s:
                current = self.edge_to[current]
                tmp.append(current)
        tmp.reverse()
        return tmp

    def bfs(self, g, s):
        q = list()
        q.append(s)
        self.dist_to[s] = 0
        while q:
            v = q.pop(0)
            self.marked[v] = True
            for w in g.adj(v):
                if not self.marked.get(w, False):
                    q.append(w)
                    self.marked[w] = True
                    self.edge_to[w] = v
                    self.dist_to[w] = self.dist_to[v] + 1


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

    dfs = DepthFirstSearch(g1, 0)
    assert dfs.has_path_to(2)
    assert not dfs.has_path_to(12)
    path = dfs.paths(2)
    my_print(path)
    assert [0, 5, 4, 2] == path, "{0}".format(path)
    assert [] == dfs.paths(6)

    bfs = BreadthFirstSearch(g1, 0)
    assert bfs.has_path_to(2)
    assert not bfs.has_path_to(12)
    path = bfs.paths(2)
    my_print(path)
    assert [0, 5, 4, 2] == path, "{0}".format(path)
    assert [] == bfs.paths(6)

    g2 = Digraph(5)
    g2.add_edge(5, 0)
    g2.add_edge(2, 4)
    g2.add_edge(3, 2)
    g2.add_edge(1, 2)
    g2.add_edge(0, 1)
    g2.add_edge(4, 3)
    g2.add_edge(3, 5)
    g2.add_edge(0, 2)
    my_print(g2)

    assert 6 == g2.v_size()
    assert 8 == g2.e_size()

    bfs = BreadthFirstSearch(g2, 0)
    assert bfs.has_path_to(2)
    assert not bfs.has_path_to(12)
    path = bfs.paths(2)
    my_print(path)


my_unit_test()
