#
# 题目 看不懂
# 大致是 求 平均值， 再 进行比较， 然后决定


base_dic_data = {1: 100,
                 2: 500,
                 3: 1000,
                 4: 5000,
                 5: 10000,
                 6: 25000,
                 7: 50000,
                 8: 100000,
                 9: 500000,
                 10: 1000000,
                 }


def my_print(x, end="\n"):
    # print(x, end=end)
    pass


def my_input():
    t1 = int(input())
    data = [0] * t1
    for i in range(t1):
        data[i] = int(input())
    banker = int(input())
    return data, banker
    pass


def my_run(data, banker):
    keep_list = []
    for i in range(1,11):
        if i in data:
            pass
        else:
            keep_list.append(base_dic_data.get(i))
    my_print(keep_list)
    t = sum(keep_list)
    my_print("sum = {0}".format(t))
    if len(keep_list) == 0:
        res = 'deal'
    else:
        avg = t / (len(keep_list))
        if avg <= banker:
            res = 'deal'
        else:
            res = 'no deal'
    my_print("res={0}".format(res))
    return res
    pass


def my_unit_test():
    pass


def my_func_test():
    assert my_run([3, 8], 198000) == 'no deal'
    assert my_run([10, 9, 8, 7, 6, 5, 4, 3], 400) == 'deal'
    pass


def my_main():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()
    data,banker = my_input()
    res = my_run(data, banker)
    print(res)

my_main()
