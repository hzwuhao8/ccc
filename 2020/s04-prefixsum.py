#
#
#

import collections

chr_to_num = {'A': 0, 'B': 1, 'C': 0}
n = input()
x = collections.Counter(n)

# print(x)

n_len = len(n)
n_ring = n + n[0:-1]
n_ring_len = len(n_ring)

prefix_sum_list = [0 for x in range(n_ring_len)]
prefix_sum_list[0] = chr_to_num[n_ring[0]]

for i in range(1, n_ring_len):
    # prefix_sum_list.append(prefix_sum_list[i - 1] + chr_to_num[n_ring[i]])
    prefix_sum_list[i] = (prefix_sum_list[i - 1] + chr_to_num[n_ring[i]])

# print(prefix_sum_list)

b_counter = x['B']
max_b = 0
for i in range(0, n_ring_len - b_counter):
    tmp = prefix_sum_list[i + b_counter] - prefix_sum_list[i]
    if tmp > max_b:
        max_b = tmp

# print(max_b)

res = x['B'] - max_b

print(res)
