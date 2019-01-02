#1 分析问题
#2 写测试
#3 分解问题
#4 写单元测试
#5 组装

DEFAULT_STR =" "

dic_a = {}
dic_a[(4, 4)] = 'W'
dic_a[(4, 5)] = 'B'
dic_a[(5, 4)] = 'B'
dic_a[(5, 5)] = 'W'


dic_b = {}
for kk in range(1, 9):
    dic_b[(kk, kk)] = 'B'
    dic_b[(9 - kk, kk)] = 'W'

dic_c = {}
for kk in range(1, 9):
    dic_c[(kk, 3)] = 'B'
    dic_c[(kk, 4)] = 'B'
    dic_c[(kk, 5)] = 'W'
    dic_c[(kk, 6)] = 'W'

dic_map = {'a': dic_a, 'b': dic_b, 'c': dic_c}


def my_print(x="", end="\n"):
    #print(x, end=end)
    pass


def my_print_dic(dic):
    # return None
    my_print()
    for i in range(1, 9):
        for j in range(1, 9):
            x = dic.get((i, j), "*")
            my_print("  {0} ".format(x), end="")
        my_print()
    my_print()


def my_input():
    my_str = input()
    return my_str
    pass


def my_parse(data):
    my_str_list = data.split()
    typ = my_str_list[0]
    size = int(my_str_list[1])
    step_list = []
    for i in range(2, size * 2 + 2, 2):
        row = int(my_str_list[i])
        col = int(my_str_list[i + 1])
        step_list.append((row, col))
    my_print("step_list={0}".format(step_list))

    return typ, step_list



def my_run(data):
    (typ, move_list) = my_parse(data)
    dic = dic_map[typ].copy()
    color = 'B'
    r_color = 'W'
    m,n=8,8
    my_print_dic(dic)
    for x, y in move_list:
        one_line_list = my_get_list_all(x, y)
        need_replace_list = []

        for line in one_line_list:
            tmp = my_get_replace(dic, line, color, r_color)
            need_replace_list = need_replace_list + tmp

        my_print("need_replace_list={0}".format(need_replace_list))
        dic[(x, y)] = color
        for p in need_replace_list:
            dic[p] = color

        color, r_color = r_color, color

    my_print_dic(dic)
    total_b = 0
    total_w = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            c = dic.get((i,j),DEFAULT_STR)
            if c == 'B':
                total_b += 1
            elif c =='W':
                total_w += 1
            else:
                pass
    return "{0} {1}".format(total_b, total_w)


    pass


def my_func_test():
    assert my_run("a 1 5 6") == "4 1"
    assert my_run("b 0") == "8 8"
    assert my_run("c 3 1 7 2 2 2 1") == "22 13"
    pass


def my_get_list_all(x, y, m=8, n=8):
    one_line_list = []
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            tmp = my_get_list(x,y,dx,dy,m,n)
            one_line_list.append(tmp)
    return one_line_list
    pass




# 取某一个个方向的数据
# MxN 的矩阵
def my_get_list(x, y, dx, dy, m=8, n=8):

    my_print((x, y))
    my_print("dx={dx}, dy={dy}".format(dx=dx, dy=dy))
    res = []
    max_steps = max(m, n)
    step = 0
    while step <= max_steps:
        x1 = x + dx * step
        y1 = y + dy * step
        step += 1
        my_print("({0},{1}) step={2}".format(x1, y1, step))
        if 1 <= x1 <= m and 1 <= y1 <= n:
            res.append((x1, y1))
        else:
            break

    my_print(res)
    return res
    pass


# 得到 需要替换的  坐标
def my_get_replace(dic, data, color, r_color):
    res = []
    if len(data) >= 3:
        for i in range(1, len(data)):
            if dic.get(data[-i], DEFAULT_STR) == color:
                sub_list = data[1:-i]
                color_list = [dic.get(p, DEFAULT_STR) for p in sub_list]
                if color_list == [r_color] * len(sub_list):
                    res = sub_list
    my_print("会被替换的坐标res={0}".format(res))
    return res

    pass



# 8个方向，每个方向的 列表
# 每个方向，的最大替换
# 数据结构设计， 选择？
# dict , 稀疏矩阵
def my_unit_test():
    # （Up,0),(Up,Right),(0,Right),(Down,Right)
    #  (Down,0),(Down,Left),(0,Left),(Up,Left)
    x, y = 1, 1
    assert my_get_list(x, y, -1, +0) == [(1, 1)]
    assert my_get_list(x, y, -1, +1) == [(1, 1)]
    assert my_get_list(x, y, +0, +1) == [(x, y + k) for k in range(8)]
    assert my_get_list(x, y, +1, +1) == [(x + k, y + k) for k in range(8)]
    assert my_get_list(x, y, +1, +0) == [(x + k, y) for k in range(8)]
    assert my_get_list(x, y, +1, -1) == [(1, 1)]
    assert my_get_list(x, y, +0, -1) == [(1, 1)]
    assert my_get_list(x, y, -1, -1) == [(1, 1)]

    assert my_get_list(5, 5, +1, +1) == [(5, 5), (6, 6), (7, 7), (8, 8)]
    assert my_get_list(5, 6, 0,  -1) == [(5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1)]


    assert my_get_replace(dic_a, [(1, 1), (1, 2), (1, 3), (1, 4)], 'B', 'W') == []
    assert my_get_replace(dic_a, [(5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1)], 'B', 'W') == [(5, 5)]


    pass


def my_main():
    my_unit_test()
    my_func_test()
    data = my_input()
    res = my_run(data)
    print(res)

my_main()

