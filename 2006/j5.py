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
         (5, 4): "W",
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

dic_choose = {'a': dic_a , 'b': dic_b, "c": dic_c }

# 改变状态， 核心方法
def black_move(dic_current, r, c):

    pass


def white_move(dic_current, r, c):

    pass


def my_run(typ, data):

    dic_current = dic_choose[typ].copy()

    for i in range(len(data)):
        if i % 2 == 0:
            black_move(dic_current, data[i][0], data[i][1])
        else:
            white_move(dic_current, data[i][0], data[i][1])
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
    assert my_run('b', []) == [8, 8] , my_run('b', [])
    assert my_run('a',[(5, 6)]) == [4, 1]

    assert my_run('c',[(1, 7), (2, 2), (2, 1)]) == [22, 13]
    pass


def my_main():
    #my_input()
    my_test()


my_main()
