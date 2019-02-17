# 使用 digraph 的方法 解决问题

# 读入 数据 构造图
# 从点 1 出发， 用 bfs 进行搜索，
# 如果除 0 外，marked[x] == True ;  图联通，
# dist_to  从 0 ，1，2，  直到 找到 某一层 有 节点是  终点

from Digraph import *





def my_input():
    n = int(input())
    g = Digraph(n, True)
    for page in range(1, n + 1):
        my_str = input()
        page_nums = [int(x) for x in my_str.split()]
        for num in page_nums[1:]:
            g.add_edge(page, num)
    return (n, g)


def my_run(n, g):
    bfs = BreadthFirstSearch(g, 1)
    dic1 = bfs.get_marked()
    if len(dic1) == n:
        res1 = 'Y'
    else:
        res1 = 'N'

    res2 = n
    dic2 = bfs.get_dist_to()
    # 检查所有的节点，找到在 最小层的 终点
    for k, v in dic2.items():
        if not g.adj(k) and v < res2:
            res2 = v
    res2 = res2 + 1  # 因为是从0 开始计数的
    return res1, res2


def my_main():
    n, g = my_input()
    my_print("n={}".format(n))
    my_print("{}".format(g))
    res1, res2 = my_run(n, g)
    print(res1)
    print(res2)


my_main()
