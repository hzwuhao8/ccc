#
# j5
#
# 1 统计  各种数字 有多少个
# 2 统计  能组成 哪些 和，并记录 宽度，
# 3 求取 最大 宽度， 并计数 最大宽度的 有 几种 高度


def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run(4, "1 2 3 4") == "2 1"
    assert my_run(5, "1 10 100 1000 2000") == "1 10"


def my_run(n, my_str):
    data = [int(x) for x in my_str.split()]

    # 统计有哪些数字
    num_dic = {}
    for x in data:
        num_dic.setdefault(x, 0)
        num_dic[x] = num_dic[x] + 1
    my_print("num_dic={0}".format(num_dic))
    # 统计  能够组成的 高度  ，并记录宽度
    sum_dic = {}
    sum_dic_list = list(num_dic.items())
    index = -1
    for i, v1 in sum_dic_list:
        index += 1
        for j, v2 in sum_dic_list[index:]:
            key = i + j
            sum_dic.setdefault(key, 0)
            if i == j:
                sum_dic[key] = sum_dic[key] + v1 // 2
            else:
                sum_dic[key] = sum_dic[key] + min(v1, v2)
    my_print("sum_dic={0}".format(sum_dic))

    # 求 最大的 width
    res1, res2 = 0, 0
    for k, v in sum_dic.items():
        if v > res1:
            res1 = v
            res2 = 1
        elif v == res1:
            res2 += 1

    res_str = "{0} {1}".format(res1, res2)
    my_print(res_str)
    return res_str


my_func_test()


def my_main():
    n = int(input())
    my_str = input()
    res = my_run(n, my_str)
    print(res)


my_main()
