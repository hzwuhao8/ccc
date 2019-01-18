#
#
# jerseys  球衣
# 编号  尺寸  和 队员之间的 要求
# 能满足 的 最大数量
#


def my_print(x):
    print(x)
    pass


def my_func_test():
    J = 4
    A = 3
    j_list = ['', 'M', 'S', 'S', 'L']
    a_list = [('L', 3), ('S', 3), ('L', 1)]
    assert my_run(J, A, j_list, a_list) == 1


# 计算 匹配的数量
# 用元组  比较精确
def my_run(J, A, j_list, a_list):
    data = zip(j_list, range(J))
    my_print(data)


my_func_test()
