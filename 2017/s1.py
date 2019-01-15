#
# 对于 数据量 大的 性能 不能满足 要求
#
#
#
#
#


def my_func_test():
    assert my_run(3, "1 3 3", "2 2 6") == 2
    assert my_run(3, "1 2 3", "4 5 6") == 0
    assert my_run(4, "1 2 3 4", "1 3 2 4") == 4


def my_run(n, str1, str2):
    d1 = [int(x) for x in str1.split()]
    d2 = [int(x) for x in str2.split()]
    s1 = sum(d1)
    s2 = sum(d2)
    if s1 == s2:
        return n
    else:
        for i in range(-1, -n, -1):
            s1 = s1 - d1.pop()
            s2 = s2 - d2.pop()
            if s1 == s2:
                return n + i
        return 0


# my_func_test()


def my_main():
    n = int(input())
    str1 = input()
    str2 = input()
    res = my_run(n, str1, str2)
    print(res)


my_main()
