class Digraph:

    def __init__(self, v_size, from1=False):
        self.dic = {}
        if from1:
            for i in range(1, v_size + 1):
                self.dic[i] = [].copy()
        else:
            for i in range(v_size):
                self.dic[i] = [].copy()

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

    def get_marked(self):
        return self.marked

    def get_dist_to(self):
        return self.dist_to


def my_print(x, end="\n"):
    # print(x, end=end)
    pass
