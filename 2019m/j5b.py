#
#
# 先计算 k  有多少种 取法；  每种对应的取法种  某一类鱼  又有多少种取法
#
#
#
#


def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run(1, 2, [1]) == 0
    assert my_run(1, 1, [1]) == 1

    assert my_run(3, 1, [1, 1, 1]) == 3
    assert my_run(3, 1, [1, 1, 1, 2, 3, 2, 2, 3]) == 3 + 3 + 2
    assert my_run(3, 2, [1, 1, 1]) == 0
    assert my_run(4, 3, [1, 2, 2, 3]) == 2
    assert my_run(4, 1, [1, 2, 2, 3]) == 4  # 有疑问， 1+2+1 = 4 种
    assert my_run(2, 1, [1, 2]) == 2
    my_print("***" * 20)
    assert my_run(3, 2, [1, 2, 3]) == 3
    my_print("***" * 20)
    assert my_run(4, 1, [1, 2, 3, 4]) == 4
    assert my_run(4, 3, [1, 2, 3, 4]) == 4  # C(4,3) = C(4,1)
    assert my_run(4, 2, [1, 2, 3, 4]) == 4 * 3 / 2


def my_run(n, k, a_list):
    dic = {}
    for x in a_list:
        dic.setdefault(x, 0)
        dic[x] = dic[x] + 1
    my_print(dic)
    if k > len(dic):
        return 0

    # 组合 在计数
    # 先找到 k1 k2 k3 ;  然后是  n(k1) * n(k2) *n(k3) ;   然后 再所有的 相加
    # 递归处理吗？

    #
    key_list = list(dic.keys())
    key_list.sort()

    res = my_r(k, key_list, dic, 0)
    return res
    pass


def my_r(k, keys, dic, layer):
    my_print("  " * layer + "k={0},keys={1}".format(k, keys))
    n = len(keys)
    base_data = [1] * k + [0] * (n - k)
    # my_print(base_data)

    res = 0
    cc = 0
    while True:
        cc += 1
        my_print(base_data)
        mul = 1
        for index, i in enumerate(base_data):
            if i == 1:
                mul *= dic[keys[index]]
        res += mul
        # my_print("base_data[n-k:]=".format(base_data[n - k:]))
        if sum(base_data[n - k:]) == k:
            break
        else:
            for i in range(n - 1):
                if base_data[i] == 1 and base_data[i + 1] == 0:
                    base_data[i] = 0
                    base_data[i + 1] = 1
                    # k-1 个1
                    form = 0
                    for j in range(i):
                        k_count = k - 1
                        if base_data[j] == 0:
                            if 1 in base_data[j:i]:
                                index = base_data.index(1, j, i)
                                base_data[j] = 1
                                base_data[index] = 0
                            k_count -= 1
                            if k_count == 0:
                                break

                    break
    my_print("res={0}".format(res))
    return res


# my_func_test()


def my_main():
    n, k = [int(x) for x in input().split()]
    data = [int(x) for x in input().split()]
    res = my_run(n, k, data)

    print(res)

my_main()
