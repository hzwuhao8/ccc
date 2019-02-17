from Digraph import *


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
