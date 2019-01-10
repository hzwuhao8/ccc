def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_func_test():
    assert my_run_min([5, 1, 4], [6, 2, 4]) == 12
    assert my_run_max([5, 1, 4], [6, 2, 4]) == 15
    assert my_run_max([202, 177, 189, 589, 102], [17, 78, 1, 496, 540]) == 2016


# 排序 然后取， 看看能否取到 大对大
def my_run_min(d1, d2):
    d1a = sorted(d1)
    d2a = sorted(d2)
    d1a.reverse()
    d2a.reverse()

    n = len(d1)
    my_min = 0
    for i in range(n - 1, -1, -1):
        if d2a[i] > d1a[i]:
            my_min += d2a[i]
        else:
            my_min += d1a[i]
    return my_min
    pass


# 要尽量 取到 大的 数
def my_run_max(d1, d2):
    d1a = sorted(d1)
    d2a = sorted(d2)
    d1a.reverse()
    d2a.reverse()
    my_print("d1a={0}".format(d1a))
    my_print("d2a={0}".format(d2a))

    dd = d1a + d2a
    dd.sort()
    dd.reverse()
    my_print("dd={0}".format(dd))
    n = len(d1)
    res = []
    dd1 = dd[:n]
    my_print("dd1={0}".format(dd1))
    sum = 0
    for x in dd1:
        if x in d1a:
            d1a.remove(x)
            for y in d2a:
                if y < dd1[-1]:
                    d2a.remove(y)
                    break
        else:
            d2a.remove(x)
            for y in d1a:
                if y < dd1[-1]:
                    d1a.remove(y)
                    break
        res.append((x, y))
        sum += x
        my_print("d1a={0} d2a={1},(x,y)=({2},{3})".format(d1a, d2a, x, y))
        my_print("res={0}".format(res))
    return sum



my_func_test()
