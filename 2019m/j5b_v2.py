#
#
# 先计算 k  有多少种 取法；  每种对应的取法种  某一类鱼  又有多少种取法
#
#
#
#
import random


def my_print(x):
    # print(x)
    pass


def fac(x):
    mul = 1
    for i in range(1, x + 1):
        mul *= i
    return mul


def c(n, k):
    if k == 0:
        return 1
    if n - k < k:
        k = n - k
        # my_print("n={0},k={1}".format(n, k))
    p1 = 1
    for i in range(k):
        p1 *= (n - i)
    p2 = fac(k)
    # my_print("p1={0},p2={1}".format(p1, p2))
    return p1 // p2


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
    if k == 0:
        return 0
    # 组合 在计数
    # 先找到 k1 k2 k3 ;  然后是  n(k1) * n(k2) *n(k3) ;   然后 再所有的 相加
    # 递归处理吗？

    #
    my_print("dic={0}".format(dic))
    sa = [x for x in dic.items() if x[1] == 1]
    sb = [x for x in dic.items() if x[1] > 1]
    my_print("sa={0}".format(sa))
    my_print("sb={0}".format(sb))
    n_sa = len(sa)
    n_sb = len(sb)
    if n_sb == 0:
        return c(n_sa, k)

    my_print("n_sa={0} n_sb={1} ".format(n_sa, n_sb))
    res = 0
    sb_dic = dict(sb)
    sb_keys = list(sb_dic.keys())

    for i in range(k, -1, -1):
        if i > n_sa:
            continue
        if k - i > n_sb:
            continue
        p = 0

        p2 = my_r(k - i, sb_keys, sb_dic, 0)
        p1 = c(n_sa, i)
        p = p1 * p2

        print("k1={0} k2={1} p={2} p1={3} p2={4} n_sa={5} n_sb={6}".format(i, k - i, p, p1, p2, n_sa, n_sb))
        res += p
    my_print(res)
    return res
    pass


def my_r(k, keys, dic, layer):
    my_print("  " * layer + "k={0},keys={1}".format(k, keys))
    n = len(keys)
    base_data = [1] * k + [0] * (n - k)
    # my_print(base_data)

    res = 0
    cc = 0
    my_max = c(n, k)
    while True:
        cc += 1
        if cc % 10000 == 0:
            # print(cc)
            # print(base_data)
            pass
        if cc > my_max:
            pass
            # print("ERROR")
            # print("n={0} k={1}".format(n, k))
            # break

        my_print(base_data)
        mul = 1
        for index, i in enumerate(base_data):
            if i == 1:
                mul *= dic[keys[index]]

        res += mul
        # my_print("base_data[n-k:]=".format(base_data[n - k:]))
        if base_data[n - k:].count(1) == k:
            break
        else:

            for i in range(n - 1):
                if base_data[i] == 1 and base_data[i + 1] == 0:
                    base_data[i] = 0
                    base_data[i + 1] = 1

                    for j in range(i):
                        if base_data[j] == 0:
                            if 1 in base_data[j:i]:
                                index = base_data.index(1, j, i)
                                base_data[j] = 1
                                base_data[index] = 0
                            else:
                                break
                    break

    my_print("res={0}".format(res))
    return res


# my_func_test()


def my_main():
    n, k = [int(x) for x in input().split()]
    data = [int(x) for x in input().split()]
    res = my_run(n, k, data)
    res = res % 998244353
    print(res)


my_main()


def my_cnk_test():
    assert c(10, 0) == 1
    assert c(10, 1) == 10
    assert c(10, 10) == 1


# my_cnk_test()



def my_unit_test():
    my_max = 100
    for i in range(100):
        n = random.randint(1, my_max)
        k = random.randint(1, min(3, n))
        dic = dict(enumerate([1] * n))
        print("n={0} k={1}".format(n, k))
        res = my_r(k, list(range(n)), dic, 0)

        assert res == c(n, k), "n={0} k={1}".format(n, k)

# my_unit_test()
