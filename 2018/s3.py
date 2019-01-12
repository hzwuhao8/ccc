#1 显示 矩阵
#2 处理被 C  控制的节点
#3 广度优先 搜索， 得到 结果集
#4 数据整理，输出结果
# 4 x 100  估计 递归 可以处理的


def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_func_test():
    data_str = """WWWWW
W.W.W
WWS.W
WWWWW"""
    assert my_run(data_str) == [-1, 2, 1]

    data_str = """WWWWWWW
WD.L.RW
W.WCU.W
WWW.S.W
WWWWWWW"""
    assert my_run(data_str) == [2, 1, 3, -1, -1, 1]


def my_run(data_str):
    pass



