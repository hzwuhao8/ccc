#
# 排序问题
# 高低 交替
# 偶数位 的 总数比奇数位的 大
# 高的越来越高  低的 越来越低
# 排序
# 最大最下 。。。。  然后再 reverse
#
#
#

def my_func_test():
    assert my_run(8, "10 50 40 7 3 110 90 2") == "10 40 7 50 3 90 2 110"
    assert my_run(7, "10 50 40 7 3 90 2") == "10 40 7 50 3 90 2"


def my_run(n, my_str):
    data = [int(x) for x in my_str.split()]
    data.sort()
    # print(data)
    res = []
    if n % 2 == 1:
        res.append(data[0])
        data = data[1:]
        n = n - 1
    m = n // 2
    for i in range(m):
        res.append(data[n - 1 - i])
        res.append(data[i])


# print(res)
    res.reverse()
    res_str = " ".join([str(x) for x in res])


    return res_str


my_func_test()


def my_main():
    n = int(input())
    my_str = input()
    res = my_run(n, my_str)
    print(res + " ")


my_main()
