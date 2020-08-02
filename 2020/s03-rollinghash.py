import itertools
import collections
# import hashlib
from hashlib import md5

# 不使用用 md5 . 有 rolling hash  计算 hash ,  md5 超时
# rolling hash 是一个  增量过程可以 从 前一个  计算出 下一个
# 这里 其实 不是严格的。  rolling hash 的参数，  特别是 m  会 有影响，  存在    hash 冲突。   a = b => hash(a) = hash(b) ;
# 但是 hash(a) = hash(b) => 不能推出 ， 实际上当 m=2^32 时，  实际是否 冲突存在的， 会导致  结果 偏少，  当 m=2^48 时， 结果时准确的 a = b

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

p = 37
m = 2 ** 64

# p_list = [p ** x % m for x in range(n_size)]
p_list = [1]

for i in range(1, n_size):
    p_list.append((p_list[i - 1] * p) % m)

# print(ya)
t0 = collections.Counter(ya)
hash0 = 0
for i in range(len(ya)):
    hash0 = hash0 + ord(ya[i]) * p_list[n_size - i - 1]
hash0 = hash0 % m

# print(n)
# print(h)

# print(ya, hash0)
# print(t0)
if t0 == x:
    str_set.add(hash0)

for i in range(1, h_size - n_size + 1):
    if h[i - 1] != h[i + n_size - 1]:
        t0.subtract(h[i - 1])
        if t0[h[i - 1]] == 0:
            del t0[h[i - 1]]
        t0.update(h[i + n_size - 1])
    hash0 = hash0 * p - (ord((h[i - 1])) * p_list[n_size - 1] * p % m) + ord(h[i + n_size - 1])
    hash0 = hash0 % m
    # ya = h[i:i + n_size]
    # print(ya, hash0)
    # print(t0)
    if t0 == x:
        # print("=====", ya, hash0)
        str_set.add(hash0)
        count = count + 1

print(len(str_set))
