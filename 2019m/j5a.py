def my_print(x):
    # print(x)
    pass


def my_main():
    n, k = [int(x) for x in input().split()]
    data = [int(x) for x in input().split()]
    dic = {}
    for x in data:
        dic.setdefault(x, 0)
        dic[x] = dic[x] + 1
    if k > len(data):
        return 0
    else:
        cnk = c(n, k)
        mul = 1
        my_print(dic)
        for k, v in dic.items():
            mul *= fac(v)
        my_print("cnk={0} mul={1}".format(cnk, mul))
        return cnk // mul


def fac(x):
    mul = 1
    for i in range(1, x + 1):
        mul *= i
    return mul


def c(n, k):
    my_print("n={0},k={1}".format(n, k))
    p1 = 1
    for i in range(k):
        p1 *= (n - i)
    p2 = fac(k)
    my_print("p1={0},p2={1}".format(p1, p2))
    return p1 // p2




print(my_main())
