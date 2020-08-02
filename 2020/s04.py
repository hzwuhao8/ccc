# 没有思路
# 定位 i,  [i,i+Ca] i确定后， 需要移动的数量已经确定， 取连续出现最多的？  好像 I 在 只有2个AB 的时候，I也不重要
import collections
n = input()

x = collections.Counter(n)
print(x)
y = n.split('B')
print(y)
