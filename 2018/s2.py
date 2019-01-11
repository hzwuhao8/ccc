# J4?
# 这个题目做过了
# 理解题目的 时间 就不需要了
#
# 1 旋转 90 的  数据变换
# 是不是一个 合法的矩阵 ；  行 升序  列 升序


def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run([[1, 3], [2, 9]]) == [[1, 3], [2, 9]]
    assert my_run([[3, 7, 9], [2, 5, 6], [1, 3, 4]]) == [[1, 2, 3], [3, 5, 7], [4, 6, 9]]


def my_run(data):
    if is_validate(data):
        return data

    for i in range(4):
        next_data = rotate_90(data)
        if is_validate(next_data):
            return next_data

    pass


# 旋转 90度 顺时针
def rotate_90(data):
    n = len(data)
    next_data = [[0] * n] * n
    for i in range(0, n):
        tmp_row = [0] * n
        for j in range(0, n):
            my_print("i={0} j={1} (n - 1) - j={2}".format(i, j, (n - 1) - j))
            tmp_row[j] = data[(n - 1) - j][i]
        next_data[i] = tmp_row
        my_print(next_data)
    return next_data


# 满足 排序要求的矩阵
def is_validate(data):
    for r in data:
        if is_sorted(r):
            pass
        else:
            return False
    for i in range(len(data)):
        tmp = []
        for j in range(len(data)):
            tmp.append(data[j][i])
        if is_sorted(tmp):
            pass
        else:
            return False
    return True


# 升序 序列
def is_sorted(r):
    r1 = r.copy()
    r2 = sorted(r1)
    return r1 == r2


def my_unit_test():
    assert is_sorted([1, 2, 3])
    assert not is_sorted([2, 1, 3])
    assert is_validate([[1, 2, 3], [3, 5, 7], [4, 6, 9]])
    assert rotate_90([[3]]) == [[3]]
    assert rotate_90([[1, 2, 3], [3, 5, 7], [4, 6, 9]]) == [[4, 3, 1], [6, 5, 2], [9, 7, 3]]


my_unit_test()
my_func_test()


def my_main():
    n = int(input())
    data = []
    for i in range(n):
        d1 = [int(x) for x in input().split()]
        data.append(d1)
    res = my_run(data)

    for x in res:
        print(" ".join([str(i) for i in x]))


my_main()

