import itertools
import collections
# import hashlib
from hashlib import md5

n = input().strip()
h = input().strip()

# print(len(n))
# print(len(h))

n_size = len(n)
h_size = len(h)
#  1 生成搜索序列，  搜索序列 如何生成？  生成的 时候，如果  子列   不是 h 的 子列， 那么 这个排序 就不是 h的 子列
#  用这种方法，可以 过滤 很大一部分  如何用程序表达 描述？
#  n -> dict {"a" : 2 , "b": 1 } , 然后进行排列？  如何生成排列？ 如何 得到 子排列， 如何 过滤？和  树 有关系吗？
#  a -> a -> b ;  如果 aa 不存在， 则 aa 下面的 分支 都不用处理了。
#  将 h  按照 n 的 长度 进行分割，
#  换一个思路，这里还需要考虑 重复的情况， 哪种情况下 有重复？
#
count = 0
x = collections.Counter(n)
# print(x)
y = collections.Counter(h)
str_set = set()
ya = h[0:n_size]
m = md5()
# print(ya)
t0 = collections.Counter(ya)
# print(t0)
if t0 == x:
    tt = m.copy()
    tt.update(ya.encode())
    str_set.add(tt.hexdigest())

for i in range(1, h_size - n_size + 1):
    if h[i - 1] != h[i + n_size - 1]:
        t0.subtract(h[i - 1])
        if t0[h[i - 1]] == 0:
            del t0[h[i - 1]]
        t0.update(h[i + n_size - 1])
    # print(t0)
    if t0 == x:
        ya = h[i:i + n_size]
        tt = m.copy()
        tt.update(ya.encode())
        str_set.add(tt.hexdigest())
        count = count + 1

print(len(str_set))
