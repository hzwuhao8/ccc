data_col = [[], [], []]
data_row = [[], [], []]

for i in range(3):
    row = input().split()
    data_row[i] = row

for i in range(3):
    data_col[i] = [data_row[j][i] for j in range(3)]

# print(data_row)

# print(data_col)

res_data = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]


def my_by_row(my_data):
    # print(my_data)
    # 按照 行 计算
    for i in range(3):
        if my_data[i][0] == 'X':
            if res_data[i][0] == 'Y' and my_data[i][1] != 'X' and my_data[i][2] != 'X':
                x = int(my_data[i][1]) - (int(my_data[i][2]) - int(my_data[i][1]))
                res_data[i][0] = x
                my_data[i][0] = str(x)
                res_data[i][1] = int(my_data[i][1])
                res_data[i][2] = int(my_data[i][2])
        else:
            if res_data[i][0] == 'Y':
                res_data[i][0] = int(my_data[i][0])

        if my_data[i][1] == 'X':
            if res_data[i][1] == 'Y' and my_data[i][0] != 'X' and my_data[i][2] != 'X':
                x = (int(my_data[i][0]) + int(my_data[i][2])) // 2
                res_data[i][0] = int(my_data[i][0])
                res_data[i][1] = x
                my_data[i][1] = str(x)
                res_data[i][2] = int(my_data[i][2])
        else:
            if res_data[i][1] == 'Y':
                res_data[i][1] = int(my_data[i][1])

        if my_data[i][2] == 'X':
            if res_data[i][2] == 'Y' and my_data[i][0] != 'X' and my_data[i][1] != 'X':
                x = int(my_data[i][1]) + (int(my_data[i][1]) - int(my_data[i][0]))
                res_data[i][0] = int(my_data[i][0])
                res_data[i][1] = int(my_data[i][1])
                res_data[i][2] = x
                my_data[i][2] = str(x)
        else:
            if res_data[i][2] == 'Y':
                res_data[i][2] = int(my_data[i][2])

        # 按照 列计算
        # print(res_data)
        for i in range(3):
            if my_data[0][i] == 'X':
                if res_data[0][i] == 'Y' and my_data[1][i] != 'X' and my_data[2][i] != 'X':
                    x = int(my_data[1][i]) - (int(my_data[2][i]) - int(my_data[1][i]))
                    res_data[1][i] = int(my_data[1][i])
                    res_data[2][i] = int(my_data[2][i])
                    res_data[0][i] = x
                    my_data[0][i] = str(x)
            else:
                if res_data[0][i] == 'Y':
                    res_data[0][i] = int(my_data[0][i])


# 计算 X 的数量; 用于计算  循环次数
x_count = 0
for i in range(3):
    for j in range(3):
        if data_row[i][j] == 'X':
            x_count += 1


def count_y():
    my_res = 0
    for j in range(3):
        if data_row[i][j] == 'Y':
            my_res += 1
    return my_res


for i in range(x_count):
    my_by_row(data_row)
    if count_y() == 0:
        # print(res_data)
        break

for row in res_data:
    print(row[0], row[1], row[2])
