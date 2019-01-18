#
#
# jerseys  球衣
# 编号  尺寸  和 队员之间的 要求
# 能满足 的 最大数量
#


def my_print(x):
    # print(x)
    pass


def my_func_test():
    J = 4
    A = 3
    j_list = ['', 'M', 'S', 'S', 'L']
    a_list = [('L', 3), ('S', 3), ('L', 1)]
    data = list(zip(j_list, range(J)))
    # a_list 中有重复的！
    a_set = set(a_list)
    assert my_run(J, A, data, a_set) == 1


# 计算 匹配的数量
# 用元组  比较精确
# 性能问题
# 大量的  count(); 需要 排序
def my_run(J, A, data, a_list):
    my_print(data)
    total = 0
    for x in a_list:
        if x in data:
            data.remove(x)
            total += 1

    res = total
    return res


# my_func_test()


def my_main():
    J = int(input())
    A = int(input())
    data = []
    for i in range(1, J + 1):
        t = (input(), i)
        data.append(t)
    a_list = []
    for i in range(A):
        a, b = input().split()
        a_list.append((a, int(b)))
    # a_set = set(a_list)
    res = my_run(J, A, data, a_list)
    print(res)


my_main()
