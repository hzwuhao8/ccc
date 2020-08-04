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
    t1 = max(data)
    i = data.index(t1)
    if i < m:
        t2 = max(data[m + 1:])
    elif i == m:
        t2 = max(max(data[0:m]), max(data[m + 1:]))
    elif i < k:
        t2 = max(data[i + 1:])
    elif i == k:
        t2 = max(max(data[0:k]), max(data[k + 1:]))
    else:
        t2 = max(data[0:k])
    my_sum = t1 + t2

print(my_sum)
