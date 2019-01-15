# j5
#
#  最小， 最小的 和 最小的 对 ； 尽量兌 大的 包括 小的  min  sum ( max(ai,bj))
#  最大， 最大的 和最小的对；   尽量兌 小的，保留 大的  max  sum (max(ai,bj))
#
#
#
#


def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run(1, "5 1 4", "6 2 4") == 12
    assert my_run(2, "5 1 4", "6 2 4") == 15
    assert my_run(2, "202 177 189 589 102", "17 78 1 496 540") == 2016


def my_run(typ, str1, str2):
    data1 = [int(x) for x in str1.split()]
    data2 = [int(x) for x in str2.split()]
    if typ == 1:
        return my_min(data1, data2)
    elif typ == 2:
        return my_max(data1, data2)


def my_min(data1, data2):
    data1.sort()
    data2.sort()
    total = 0
    for x, y in zip(data1, data2):
        total += max(x, y)
    return total


def my_max(data1, data2):
    data1.sort()
    data2.sort()
    data2.reverse()
    total = 0
    for x, y in zip(data1, data2):
        total += max(x, y)
    return total


my_func_test()


def my_main():
    typ = int(input())
    n = int(input())
    str1 = input()
    str2 = input()
    res = my_run(typ, str1, str2)
    print(res)


my_main()
