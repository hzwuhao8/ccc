#
# 递推关系   f(n) = sum(f(int(n/k)) ; k = 2 -> n
# 为什么 是这个关系？
# f(1) = 1
# f(2) = f(1) = 1
# f(3) = f(3//2) + f(1) = f(1) + f(1)
# f(4) = f(2) + f(4//3) + f(4//4) = f(2) + f(1) + f(1)
# f(5) = f(5//2) + f(5//3) + f(5//4) + f(5//5)
# weight?
# find the number of perfectly balanced trees with weight N
# weight

# tree  具体是什么 ， 难道不重要吗？
# 2+2+2 =6 <= 8 #
# 这个 6 是什么  意思？
# 8//2=4 ； 8//3 = 2 8//4 = 2
#


import time


def my_func_test():
    assert f(1) == 1
    assert f(2) == 1
    assert f(3) == 2
    assert f(4) == 3
    assert f(10) == 13


dic_cache = {}


def f1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        if n in dic_cache:
            return dic_cache[n]
        total = 0
        for k in range(2, n + 1):
            total += f1(n // k)
    dic_cache[n] = total
    return total


def f(n):
    t1 = time.time()

    for k in range(3, n // 2):
        if k % 1000 == 0:
            t2 = time.time()
            print("k={0} ts={1}".format(k, (t2 - t1)))
        f1(k)

    return f1(n)


def my_main():
    n = int(input())
    dic = {}
    t1 = time.time()
    for i in range(2, n):
        if i % 100000 == 0:
            print("i={0} ts={1}".format(i, time.time() - t1))
            print("len(dic)={0}".format(len(dic)))
        k = n // i
        dic[k] = dic.get(k, 0) + 1

    print("len(dic)={0}".format(len(dic)))

    # res = f(n)
    # print(res)


my_func_test()

my_main()
