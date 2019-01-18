def my_func_test():
    assert my_run(2, 2, 2) == 'YES'
    assert my_run(3, 4, 5) == 'NO'


# 组合
#  0 - > maxa ; 0 -> maxb  n
def my_run(a, b, n):
    max_a = n // a
    for i in range(max_a, -1, -1):
        fee_a = a * i
        fee_b = n - fee_a
        if fee_b >= 0 and fee_b % b == 0:
            return 'YES'
    return 'NO'
    pass


my_func_test()


def my_main():
    total = int(input())
    res_list = []
    for i in range(total):
        a, b, n = [int(x) for x in input().split()]
        res = my_run(a, b, n)
        res_list.append(res)
    print("\n".join(res_list))


my_main()

