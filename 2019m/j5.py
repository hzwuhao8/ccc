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
    changed = False
    if k > len(key_list) / 2 and len(key_list) >= 4:
        k = len(key_list) - k
        changed = True
    all_possible = set()
    res = my_r(k, key_list, dic, 0, [], all_possible)
    my_print("all_possible={0}".format(all_possible))
    # 上面的结果是错误的
    #
    if not changed:
        total = 0
        for x in all_possible:
            mul = 1
            for y in x:
                mul *= dic[y]
            total += mul
        return total
    else:
        total = 0
        tmp = list(dic.keys())
        tmp.sort()
        all_set = set(tmp)
        for x in all_possible:
            mul = 1
            xx = all_set.difference(set(x))
            my_print(xx)
            for y in xx:
                mul *= dic[y]
            total += mul
        return total

    pass


def my_r(k, keys, dic, layer, prefix, a_set):
    my_print("  " * layer + "k={0},keys={1} , prefix={2}".format(k, keys, prefix, a_set))
    my_print("  " * layer + "a_set={0}".format(a_set))
    res = 0
    if k > len(keys):
        res = 0
    elif k == 1:
        total = 0

        for x in keys:
            next_p = prefix.copy()
            next_p.append(x)
            next_p.sort()
            tu = tuple(next_p)
            my_print("  " * layer + "__62__" + str(tu))

            if tu in a_set:
                pass
            else:
                total += dic[x]
                a_set.add(tu)
        res = total
    elif k == len(keys):
        mul = 1
        next_p = prefix.copy()
        next_p = next_p + keys
        next_p.sort()
        my_print("  " * layer + "__76__" + str(next_p))
        tu = tuple(next_p)
        if tu in a_set:
            pass
        else:
            for x in keys:
                mul = mul * dic[x]
                a_set.add(tu)
        res = mul
    else:

        mul = 1
        for y in keys:
            next_keys = keys.copy()
            next_keys.remove(y)
            next_p = prefix.copy()
            next_p.append(y)
            t = my_r(k - 1, next_keys, dic, layer + 1, next_p, a_set)
            if t == 0:
                pass
            else:
                mul = mul * t

        res = 1 + mul
    my_print("  " * layer + "res={0}".format(res))
    return res


# my_func_test()


def my_main():
    n, k = [int(x) for x in input().split()]
    data = [int(x) for x in input().split()]
    res = my_run(n, k, data)
    print(res)


my_main()
