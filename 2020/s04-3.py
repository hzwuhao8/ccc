#  按照 说明 解法 其实还是  穷举的方法， 只是 他每一次 运算 都很快， 所以能够 在 规定的时间内解决
#  prefix sum  关于A  有一个 数组， 关于 B 有一个数组，  C 是 A，B 排队完成后， 自然 C 也 排好了
#  Na ,  应该是 A的 地方， 不是A 出现的次数   =  counter_a - ( prefix_sum [i+counter_a] -  prefix_sum[i] ) ;  对 I 进行 穷举， 求出 最小值
#  S(A,B)  是 B 在 应该是 A 出现的 地方的 出现次数;  这个 也是一个 prefix_sum  ?
#  S(B,A)  应该是B的 地方， 出现A的 次数，

# 对哪个字符 计算  prefix sum
import collections


#
#  利用 prefix sum array  对 字符出现的 次数 进行计数
#

def prefix_sum(my_str, my_ch):
    res = [0 for x in my_str]
    counter_ch = collections.Counter(my_ch)
    # print(counter_ch)
    res[0] = counter_ch[my_str[0]]
    for i in range(1, len(my_str)):
        res[i] = res[i - 1] + counter_ch[my_str[i]]
    return res


def part_sum(sum_arr, left, right):
    if left == 0:
        return sum_arr[right]
    else:
        return sum_arr[right] - sum_arr[left - 1]


def my_res(ch1, ch2):
    ca = counter[ch1]
    cb = counter[ch2]
    prefix_sum_a = my_prefix_sum[ch1]
    prefix_sum_b = my_prefix_sum[ch2]
    res = len(my_str)
    # print(counter)
    # print(my_str)
    i = 0
    na = ca - (prefix_sum_a[i + ca - 1])
    nb = cb - (prefix_sum_b[i + ca + cb - 1] - prefix_sum_b[i + ca - 1])
    sab = (prefix_sum_b[i + ca - 1])
    sba = (prefix_sum_a[i + ca + cb - 1] - prefix_sum_a[i + ca - 1])
    tmp = na + nb - min(sab, sba)
    res = tmp

    for i in range(1, len(my_str) - ca - cb):
        na = ca - (prefix_sum_a[i + ca - 1] - prefix_sum_a[i - 1])
        nb = cb - (prefix_sum_b[i + ca + cb - 1] - prefix_sum_b[i + ca - 1])
        sab = (prefix_sum_b[i + ca - 1] - prefix_sum_b[i - 1])
        sba = (prefix_sum_a[i + ca + cb - 1] - prefix_sum_a[i + ca - 1])
        tmp = na + nb - min(sab, sba)
        if tmp < res:
            # print(i, na, nb, sab, sba, tmp)
            res = tmp
    return res


n = input()

counter = collections.Counter(n)

my_str = n + n[0:-1]
my_prefix_sum = {
    'A': prefix_sum(my_str, 'A'),
    'B': prefix_sum(my_str, 'B'),
    'C': prefix_sum(my_str, 'C'),
}

# print(prefix_sum_a)
# print(prefix_sum_b)
res = min(my_res('A', 'B'),my_res('A', 'C'))

print(res)
