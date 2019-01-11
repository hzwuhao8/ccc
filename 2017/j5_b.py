#
import sys
import time


#input = sys.stdin.readline


def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run([1, 2]) == [1, 1]
    assert my_run([1, 20]) == [1, 1]
    assert my_run([0, 10, 20, 30]) == [2, 1]
    assert my_run([1, 2, 3, 4]) == [2, 1]
    t = my_run([20, 30, 40, 10, 30, 20, 15, 35])
    assert t == [4, 1], t
    t = my_run([1, 10, 100, 1000, 2000])
    assert t == [1, 10], t


def my_run(data):
    # my_print("====" * 20)
    # 统计出现次数最多的2个数字
    #
    dic_count = {}
    # n = len(data)
    # dic_cache[(i, j)] = k
    for k in data:
        dic_count[k] = dic_count.get(k, 0) + 1

    # my_print("dic_count={0}".format(dic_count))
    # my_print("len(dic_count)={0}".format(len(dic_count)))

    dic_data2 = {}
    item_list = list(dic_count.items())
    index = 0
    for i, v1 in item_list:
        for j, v2 in item_list[index:]:
            if i == j:
                c = v1 // 2
            else:
                c = min(v1, v2)

            dic_data2[i + j] = dic_data2.get(i + j, 0) + c
        index = index + 1

    # my_print("dic_data2={0}".format(dic_data2))
    ans1 = 0
    ans2 = 0
    for k, v in dic_data2.items():
        if v > ans1:
            ans1 = v
            ans2 = 1
        elif v == ans1:
            ans2 += 1

    return [ans1, ans2]

    pass


# my_func_test()


def my_main():
    n = int(input())

    data = [int(x) for x in input().split()]
    res = my_run(data)
    print(" ".join([str(x) for x in res]))


my_main()
