# https://amorim.ca/pages/viewpage.action?pageId=3276819
# 参考
# 计算 满足 和的  对应的 组合的总数
#  n*(n-1)/2 中组合方式;  取 和数 出现 最多的 组合
#  a1 + an = a2+a(n-1) =....
#  a1 + a2 = x ; a1 + a3 = x ; a1 +a4 =x ;  a2+a3 = x; 如何 避免取的时候 出现 冲突？
#   a1 + a5 = x ; a2 + a5 =x ; ; 先取出  出现次数最多的， 然后在考虑 如何取
import time


def my_print(x):
    print(x)
    pass


def is_validate(data):
    data.sort()
    l = len(data)
    d1 = data[:l // 2]
    d2 = data[l // 2:]
    d2.reverse()
    s = set([x + y for x, y in zip(d1, d2)])
    if len(s) == 1:
        return len(s) == 1, d1[0] + d2[0]
    else:
        return False, 0


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
    ts = time.time()
    data.sort()
    dic_cache = {}
    dic_count = {}
    n = len(data)
    (flag, h) = is_validate(data)
    ts2 = time.time()
    if (ts2 - ts > 60 * 1000):
        print("TIME OUT")
        return [0, 0]

    if flag:
        n = len(data) // 2
        return [n, 1]

    for i in range(n):
        ts2 = time.time()
        if (ts2 - ts > 60 * 1000):
            print("TIME OUT")
            return [0, 0]
        for j in range(i + 1, n):
            if j % 100000 == 0:
                my_print("i={0},j={1} dic_count={2}".format(i, j, dic_count))
                ts2 = time.time()
                if (ts2 - ts > 60 * 1000):
                    print("TIME OUT")
                    return [0, 0]

            if i == j:
                pass
            else:
                k = data[i] + data[j]
                # dic_cache[(i, j)] = k
                if k in dic_count:
                    dic_count[k] = dic_count[k] + 1
                else:
                    dic_count[k] = 1

    my_print("dic_cache={0}".format(dic_cache))
    my_print("dic_count={0}".format(dic_count))
    n_list = sorted(dic_count.items(), key=lambda x: (x[1], x[0]), reverse=True)
    ts2 = time.time()
    if (ts2 - ts > 60 * 1000):
        print("TIME OUT")
        return [0, 0]

    my_print("n_list={0}".format(n_list))
    # 还要看能同时取到 几个，可能不到 n 个，  一个元素只能出现一次
    # 但 n0  < n1 时 ，需要对 n1 进行考虑吗？
    n = n_list[0][1]
    height = n_list[0][0]
    h = 1
    if n == 1:
        h = len(n_list)
    else:
        may_be_list = [x for x in dic_cache.items() if x[1] == height]
        my_print("may_be_list={0}".format(may_be_list))
        index_set = set()
        for x in may_be_list:
            i1, i2 = x[0]
            if i1 not in index_set:
                index_set.add(i1)
            if i2 not in index_set:
                index_set.add(i2)
        n = len(index_set) // 2

    return [n, h]
    pass


my_func_test()


def my_main():
    n = int(input())
    data = [int(x) for x in input().split()]
    res = my_run(data)
    print(" ".join([str(x) for x in res]))


my_main()
