def my_func_test():
    d1 = """16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1"""
    assert my_run(d1) == "magic"

    d2 = """5 10 1 3 
    10 4 2 3 
    1 2 8 5
    3 3 5 0"""

    assert my_run(d2) == "not magic"


def my_run(data):
    rows = data.split("\n")
    dd = []
    for r in rows:
        t = [int(x) for x in r.split()]
        dd.append(t)

    # print(dd)
    my_set = set()
    for row in dd:
        k = sum(row)
        my_set.add(k)
    # print(dic)
    t1, t2, t3, t4 = 0, 0, 0, 0
    for c1, c2, c3, c4 in dd:
        t1 += c1
        t2 += c2
        t3 += c3
        t4 += c4

    my_set2 = my_set.union(set([t1, t2, t3, t4]))
    # print(my_set2)
    if len(my_set2) == 1:
        return "magic"
    else:
        return "not magic"


my_func_test()


def my_main():
    data_str_List = []
    for i in range(4):
        data_str_List.append(input())
    my_str = "\n".join(data_str_List)
    # print(my_str)
    res = my_run(my_str)
    print(res)


my_main()
