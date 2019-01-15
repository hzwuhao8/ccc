#
#
#  按字母 统计，  是否相符
#  1 长度 相等 2 不矛盾
#
#


def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run("abba", "baaa") == 'N'
    assert my_run("cccrocks", "socc*rk*") == 'A'


def my_run(my_str1, my_str2):
    dic1 = {}
    dic2 = {'*': 0}

    for x in my_str1:
        dic1.setdefault(x, 0)
        dic1[x] = dic1[x] + 1

    for x in my_str2:
        dic2.setdefault(x, 0)
        dic2[x] = dic2[x] + 1

    my_print(dic1)
    my_print(dic2)
    for k, v in dic1.items():
        dic2.setdefault(k, 0)
        dic2[k] = dic2[k] - dic1[k]
    my_print(dic2)
    # 统计 是否 和 * 的数量一致
    total = 0

    for k, v in dic2.items():
        if k == '*':
            pass
        else:
            if dic2['*'] >= abs(v):
                dic2[k] = 0
                dic2['*'] = dic2['*'] - abs(v)
    # 移除 v =0  的 项
    my_print("after  merge dic2={0}".format(dic2))
    a_list = [k for k in dic2.items() if k[1] != 0]
    my_print("a_list={0}".format(a_list))
    if len(a_list) == 0:
        return 'A'
    else:
        return 'N'


my_func_test()


def my_main():
    str1 = input()
    str2 = input()
    res = my_run(str1, str2)
    print(res)


my_main()
