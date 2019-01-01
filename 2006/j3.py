#
#1 每个字母 需要按几次
#2 哪些需要插入 pause   同一个 key 需要加 pause
#


def my_print(x):
    # print(x)
    pass


def my_input():
    data = []
    while True:
        tmp = input()
        if "halt" == tmp:
            break
        data.append(tmp)
    return data
    pass


my_dic = {
    'a': [2, 1],
    'b': [2, 2],
    'c': [2, 3],

    'd': [3, 1],
    'e': [3, 2],
    'f': [3, 3],

    'g': [4, 1],
    'h': [4, 2],
    'i': [4, 3],

    'j': [5, 1],
    'k': [5, 2],
    'l': [5, 3],

    'm': [6, 1],
    'n': [6, 2],
    'o': [6, 3],

    'p': [7, 1],
    'q': [7, 2],
    'r': [7, 3],
    's': [7, 4],

    't': [8, 1],
    'u': [8, 2],
    'v': [8, 3],

    'w': [9, 1],
    'x': [9, 2],
    'y': [9, 3],
    'z': [9, 4],

    }


def my_run(data):
    my_print("")
    my_print(data)
    my_print("="*40)
    stack_a = []
    for c in data:
        my_print(stack_a)
        action = my_dic[c]
        if len(stack_a) == 0:
            stack_a.append([c, action])
        else:
            s1 = stack_a[-1]
            if action[0] == s1[1][0]:
                stack_a.append(['', [0, 2]])

            stack_a.append([c, action])
    my_print(stack_a)
    total = 0
    for x in stack_a:
        total = total + x[1][1]
    return total
    pass


def my_test():
    assert my_run('a') == 1
    assert my_run('dada') == 4
    assert my_run('bob') == 7
    assert my_run('abba') == 12
    assert my_run('cell') == 13
    assert my_run('www') == 7

    pass


def my_main():
    my_test()
    data = my_input()
    for s in data:
        total = my_run(s)
        print(total)


my_main()
