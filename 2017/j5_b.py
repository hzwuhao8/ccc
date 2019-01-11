#
import sys

#input = sys.stdin.readline


def my_print(x):
    print(x)
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
    # 统计出现次数最多的2个数字
    #
    dic_count = {}
    n = len(data)
    # dic_cache[(i, j)] = k
    for k in data:
        if k in dic_count:
            dic_count[k] = dic_count[k] + 1
        else:
            dic_count[k] = 1

    my_print(dic_count)
    my_print(len(dic_count))
    pass


# my_func_test()


def my_main():
    n = int(input())
    data = [int(x) for x in input().split()]
    res = my_run(data)
    # print(" ".join([str(x) for x in res]))


my_main()
