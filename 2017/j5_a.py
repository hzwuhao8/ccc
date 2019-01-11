#https://amorim.ca/pages/viewpage.action?pageId=3276819
# 参考
# 计算 满足 和的  对应的 组合的总数
#  n*(n-1)/2 中组合方式;  取 和数 出现 最多的 组合
#  a1 + an = a2+a(n-1) =....
#  a1 + a2 = x ; a1 + a3 = x ; a1 +a4 =x ;  a2+a3 = x; 如何 避免取的时候 出现 冲突？
#   a1 + a5 = x ; a2 + a5 =x ; ; 先取出  出现次数最多的， 然后在考虑 如何取



def my_func_test():
    assert my_run([1, 2]) == [1, 1]
    assert my_run([1, 20]) == [1, 1]
    assert my_run([0, 10, 20, 30]) == [2, 1]
    assert my_run([1, 2, 3, 4]) == [2, 1]
    assert my_run([20, 30, 40, 10, 30, 20, 15, 35]) == [4, 1]
    t = my_run([1, 10, 100, 1000, 2000])
    assert t == [1, 10], t


def my_run(data):
    pass


my_func_test()
