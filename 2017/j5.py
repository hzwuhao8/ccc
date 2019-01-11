# 最长的 等差数列，   子列


def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run([1, 2]) == [1, 1]
    assert my_run([1, 20]) == [1, 1]
    assert my_run([0, 10, 20, 30]) == [2, 1]
    assert my_run([1, 2, 3, 4]) == [2, 1]
    assert my_run([20, 30, 40, 10, 30, 20, 15, 35]) == [4, 1]
    t = my_run([1, 10, 100, 1000, 2000])
    assert t == [1, 10], t


def is_seq(s_seq):
    s_seq.sort()
    d1 = s_seq[:-1]
    d2 = s_seq[1:]
    d_zip = zip(d1, d2)
    d3 = [x[0] - x[1] for x in d_zip]
    d4 = set(d3)

    return len(d4) == 1


# 排序
# 取 子列
# 滑动窗口
# 等差 是肯定 满足 要求的   充分 条件， 不是 必要条件！ 存在 重复的数字  重复数字  本身也是 等差， 并且  中值 正好 相等
#  从最大 n 开始，判断是否满足；


def is_validate(data):
    data.sort()
    l = len(data)
    d1 = data[:l // 2]
    d2 = data[l // 2:]
    d2.reverse()
    s = set([x + y for x, y in zip(d1, d2)])
    if len(s) == 1:
        return len(s) == 1, d1[0] + d2[0]
    else:
        return False, 0


# 保证 len(data) = 2k


def my_run_inner(data, layer=0, dic_cache={}):
    if layer > 10:
        return [[0, 0]]
    if tuple(data) in dic_cache:
        return dic_cache[tuple(data)]

    (flag, h) = is_validate(data)
    n = len(data) // 2
    if flag:
        my_print("  " * layer + "data={0},n={1},h={2}".format(data, n, h))
        dic_cache[tuple(data)] = [[n, h]]
        return [[n, h]]
    else:
        next_data_list = remove_2(data)
        tmp_res = [[n, -1]]
        dic_cache[tuple(data)] = [[n, -1]]
        for x in next_data_list:
            y = my_run_inner(x, layer + 1, dic_cache)
            my_print("  " * layer + "data={0},y={1}".format(data, y))

            tmp_res += y
        my_print("tmp_res={0}".format(tmp_res))
        return tmp_res


def my_run(data):
    dic_cache = {}
    data.sort()
    if len(data) % 2 == 0:
        res = my_run_inner(data, 0, dic_cache)

    else:
        data_list = remove_one(data)
        res = []
        for x in data_list:
            y = my_run_inner(x, 1, dic_cache)
            res = res + y
            my_print("y={0}".format(y))
    my_print("dic={0}".format(dic_cache))
    my_print("res={0}".format(res))

    last_res = [x[1] for x in dic_cache.items() if x[1][0][1] > 0]
    last_res = sum(last_res, [])
    last_res.sort()
    n = last_res[0][0]
    h_list = [x[1] for x in last_res if x[0] == n]
    my_print("h_list={0}".format(h_list))
    h = len(set(h_list))
    my_print("last_res={0}".format(last_res))

    return [n, h]


def remove_one(data):
    size = len(data)
    res = []
    for i in range(size):
        d1 = data.copy()
        del d1[i]
        res.append(d1)
    return res


def remove_2(data):
    res1 = remove_one(data)
    res2 = []
    for x in res1:
        res3 = remove_one(x)
        res2 += res3
    res_last = [x for x in res2 if x]
    return res_last


# bad
def remove_n(data, n):
    if n <= 0:
        return [data]
    if n == 1:
        return remove_one(data)
    else:
        res = []
        for i in range(n):
            res += remove_one(data)


def my_unit_test():
    assert is_validate([1, 2, 3, 4]) == (True, 5)
    assert is_validate([20, 30, 40, 10, 30, 20, 15, 35]) == (True, 50)
    assert is_validate([1, 10, 100, 1000, 2000]) == (False, 0)
    assert remove_one([]) == []
    assert remove_one([1]) == [[]]
    assert remove_one([1, 2]) == [[2], [1]]
    assert remove_2([1, 2]) == [], remove_2([1, 2])


my_unit_test()
my_func_test()
