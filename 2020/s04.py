# 没有思路
# 定位 i,  [i,i+Ca] i确定后， 需要移动的数量已经确定， 取连续出现最多的？  好像 I 在 只有2个AB 的时候，I也不重要
# 取聚集？ 取在一定范围内， A 出现最多的 地方， 然后以这个 为基础， 进行后续的操作
# 1 统计 有多少个A ，  然后 以这个为 字符串的长度，    一个一个 字符移动， 得到 A 最多的 字符串，
# 2 这里需要考虑  时一个 圆环  这个 事实，  需要将 字符串  演长一倍
import collections

n = input()

x = collections.Counter(n)
# print(x)

max_dict = {}

str_a = n + n[0:-1]
str_len = len(str_a)


def counter_chr(ch):
    start = x[ch]
    ya = str_a[0:start]
    # print(ya)
    a_counter = collections.Counter(ya)
    max_dict[ch] = (0, a_counter[ch])
    # print(max_dict)
    for i in range(str_len - start - 1):
        del_chr = str_a[i]
        add_chr = str_a[start + i]
        a_counter.subtract(del_chr)
        a_counter.update(add_chr)
        if a_counter[ch] > max_dict[ch][1]:
            max_dict[ch] = (i, a_counter[ch])
            # print(max_dict)
            # print(str_a[i + 1:start + i + 1])


counter_chr('A')
counter_chr('B')
counter_chr('C')

# print(max_dict)
res = x['A'] - (max_dict['A'][1])
print(res)

