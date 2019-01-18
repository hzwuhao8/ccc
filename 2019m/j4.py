#
# dict ?
# 统计 出现的次数
# 按照 次数排序； 再按照  特定的顺序排序
#
#


def my_print(x):
    # print(x)
    pass


def my_main():
    a1 = "Deluxe Tuna Bitz"
    a2 = "Bonito Bitz"
    a3 = "Sashimi"
    a4 = "Ritzy Bitz"
    key_dic = {a1: 4, a2: 3, a3: 2, a4: 1}
    val_dic = {1: a4, 2: a3, 3: a2, 4: a1}
    dic = {1: 0, 2: 0, 3: 0, 4: 0}
    n = int(input())

    for i in range(n):
        my_str = input()
        key = key_dic[my_str]
        dic[key] = dic[key] + 1

    my_print(dic)
    tmp_list = dic.items()
    tmp2_list = [(x[1], x[0]) for x in tmp_list if x[1] > 0]
    tmp2_list.sort()
    my_print(tmp2_list)
    tmp2_list.reverse()
    my_print(tmp2_list)

    for x in tmp2_list:
        print("{0} {1}".format(val_dic[x[1]], x[0]))


my_main()


