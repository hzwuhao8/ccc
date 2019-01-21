#
#
# 寻找一个 特殊的  矩阵  旋转 90 度  ，就可以满足 要求
# 根据 题目， 这个 矩阵总是 存在的。
#
# 而且 每一个 位置上的 数值 也是 固定的。  如果 和 要求的 不一致 ， 这个 就必须是 旋转的
# 找出  某一行 或 某一列的 最大的不同 ， 估计可以 解决这个问题
# 如果是  奇数 需要转， 那肯定有一个一点的位置是准确的

# 只需要 计算 某二行， 就可以 求出 n  或者 计算 有多少位置错误的也是可以的

n = int(input())
data = []
for i in range(n):
    d = [int(x) for x in input().split()]
    data.append(d)

total = 0
break_row_count = 0
for i in range(n):

    flag = True
    for j in range(n):
        # print("d[{0},{1}]={2}".format(i, j, data[i][j]))
        if data[i][j] != i * n + (j + 1):
            # print("ERROR d[{0},{1}]={2}".format(i, j, data[i][j]))
            total += 1
            if flag:
                break_row_count += 1
                flag = False


# print(total)
print(break_row_count)
