#
# 第一种考虑， 用 穷举 法
# 计算  m =  n % k
# 对 n  进行分割 ， m ,k ,k .... ;  m 对位置 变换
# 有问题， 不那么简单， 可以分成 m+1， k-1， k-1， 这中 只要  m+2  <= k  就可以了！
# 这个问题就有点 麻烦了
# 如何分割  取到最大值？
# 第一确定能分为 几组
# 2K > N   这种情况下， 从 m,k ; -> m+1,k-1;一直到 k , m

n, k = [int(x) for x in input().split()]
data = [int(x) for x in input().split()]

m = n % k
my_sum = 0

if m == 0:
    my_sum = max(data)
else:
    for i in range(m, k + 1):
        d1 = data[0:i]
        d2 = data[i:]
        tmp = max(d1) + max(d2)
        # print(i, tmp)
        if tmp > my_sum:
            my_sum = tmp

print(my_sum)
