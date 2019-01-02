#
# 二维棋盘
#1  b, w
#2  a b c 三种 初始状态
#3  move , n  求当前的状态

#4 增加的 子， 不会引起连锁反应， 只会改变当前的 影响的  行列 对角线

#


def my_print(x):
    print(x)
    pass


def my_print_dic(dic):
    # return None
    print()
    for i in range(1, 9):
        for j in range(1, 9):
            x = dic.get((i, j), "*")
            print("  {0} ".format(x), end="")
        print()
    print()

def my_input():
    my_str = input()
    my_str_list = my_str.split()
    typ = my_str_list[0]
    size = int(my_str_list[1])
    step_list = []
    for i in range(2, size * 2 + 2, 2):
        row = int(my_str_list[i])
        col = int(my_str_list[i+1])
        step_list.append((row, col))
    my_print("step_list={0}".format(step_list))

    return typ, step_list
    pass


dic_a = {(4, 4): "W",
         (4, 5): "B",
         (5, 4): "B",
         (5, 5): "W",
         }


dic_b = {}
for i in range(1, 9):
    dic_b[(i, i)] = 'B'
    dic_b[(9-i, i)] = 'W'

dic_c = {}
for i in range(1, 9):
    dic_c[(i, 3)] = 'B'
    dic_c[(i, 4)] = 'B'
    dic_c[(i, 5)] = 'W'
    dic_c[(i, 6)] = 'W'


def tt():
    my_print("==="*20)
    my_print_dic(dic_a)
    my_print("==="*20)
    my_print_dic(dic_b)
    my_print("==="*20)
    my_print_dic(dic_c)

    my_print("==="*20)


dic_choose = {'a': dic_a, 'b': dic_b, "c": dic_c}


# 最大程度的改变 水平方向的

def reverse_color(c):
    if c == 'B':
        return 'W'
    elif c == 'W':
        return 'B'
    else:
        my_print("ERROR COLOR")


def hor(dic, r, c, color, r_color):

    for i in range(1, 9):
        current_color = dic.get((r, i), "")
        #my_print("current_color={0} ({1}, {2})".format(current_color,r,i))
        if current_color == color:
            tmp_l = [dic.get((r, j), "") for j in range(i + 1, c)]
            if set(tmp_l) == set([r_color]):
                my_print("find {0} - {1}".format(i + 1, c - 1))
                for k in range(i + 1, c):
                    dic[(r, k)] = color
            tmp_r = [dic.get((r, j), "") for j in range(c + 1, i)]
            if set(tmp_r) == set([r_color]):
                my_print("find {0} - {1}".format(c + 1, i))
                for k in range(c + 1, i):
                    dic[(r, k)] = color
    dic[(r, c)] = color


def ver(dic, r, c, color, r_color):
    #up
    k = 8
    while k > 0:
        x = r - k
        if x < 0:
            k = k - 1
            continue
        else:

            if dic.get((x, c), "") == color:
                tmp_list = [dic.get((x + t, c), "") for t in range(1, k)]
                if set(tmp_list) == set([r_color]):
                    for t in range(1, k):
                        dic[(x + t, c)] = color
            k = k - 1

    k = 8
    while k > 0:
        x = r + k
        if x > 8:
            k = k - 1
            continue
        else:
            if dic.get((x, c), "") == color:
                tmp_list = [dic.get((x - t, c), "") for t in range(1, k)]
                if set(tmp_list) == set([r_color]):
                    for t in range(1, k):
                        dic[(x - t, c)] = color
            k = k - 1
    dic[(r, c)] = color


def dia(dic, r, c, color, r_color):
    # up left
    k = 8
    while k > 0:
        x = r - k
        y = c - k
        if x < 0 or y < 0:
            k = k - 1
            continue
        else:

            if dic.get((x, y), "") == color:
                tmp_list = [dic.get((x - t, y - t), "") for t in range(1, k)]
                if set(tmp_list) == set([r_color]):
                    for t in range(1, k):
                        dic[(x - t, y - t)] = color
            k = k - 1


    # up right
    k = 8
    while k > 0:
        x = r - k
        y = c + k
        if x < 0 or y > 8:
            k = k - 1
            continue
        else:

            if dic.get((x, y), "") == color:
                tmp_list = [dic.get((x - t, y + t), "") for t in range(1, k)]
                if set(tmp_list) == set([r_color]):
                    for t in range(1, k):
                        dic[(x - t, y + t)] = color
            k = k - 1


    # down left
    k = 8
    while k > 0:
        x = r + k
        y = c - k
        if x > 8 or y < 0:
            k = k - 1
            continue
        else:

            if dic.get((x, y), "") == color:
                tmp_list = [dic.get((x + t, y - t), "") for t in range(1, k)]
                if set(tmp_list) == set([r_color]):
                    for t in range(1, k):
                        dic[(x + t, y - t)] = color
            k = k - 1
    # down right
    k = 8
    while k > 0:
        x = r + k
        y = c + k
        if x > 8 or y > 8:
            k = k - 1
            continue
        else:

            if dic.get((x, y), "") == color:
                tmp_list = [dic.get((x + t, y + t), "") for t in range(1, k)]
                if set(tmp_list) == set([r_color]):
                    for t in range(1, k):
                        dic[(x + t, y + t)] = color
            k = k - 1

    dic[(r, c)] = color



# 改变状态， 核心方法
def black_move(dic_current, r, c):
    hor(dic_current, r, c, 'B', 'W')
    ver(dic_current, r, c, 'B', 'W')
    dia(dic_current, r, c, 'B', 'W')
    pass


def white_move(dic_current, r, c):
    hor(dic_current, r, c, 'W', 'B')
    ver(dic_current, r, c, 'W', 'B')
    dia(dic_current, r, c, 'W', 'B')
    pass


def my_run(typ, data):

    dic_current = dic_choose[typ].copy()

    for i in range(len(data)):
        my_print_dic(dic_current)


        if i % 2 == 0:
            dic_current[(data[i][0], data[i][1])] = 'b'
            my_print("==" * 20)
            my_print_dic(dic_current)

            black_move(dic_current, data[i][0], data[i][1])


        else:
            dic_current[(data[i][0], data[i][1])] = 'w'
            my_print("==" * 20)
            my_print_dic(dic_current)

            white_move(dic_current, data[i][0], data[i][1])


    my_print_dic(dic_current)
    total_b = 0
    total_w = 0
    for k, v in dic_current.items():
        if v == 'W':
            total_w += 1
        elif v == 'B':
            total_b += 1
        else:
            pass
    return [total_b, total_w]
    pass


def my_test():
    assert my_run('b', []) == [8, 8], my_run('b', [])
    assert my_run('a', [(5, 6)]) == [4, 1]

    assert my_run('c', [(1, 7), (2, 2), (2, 1)]) == [22, 13], my_run('c', [(1, 7), (2, 2), (2, 1)])

    pass


def my_main():
    #my_test()

    typ, step_list = my_input()
    res = my_run(typ, step_list)
    print(" ".join([str(x) for x in res]))

my_main()
