#
# 题目看不懂
# 估计是 ， 不考虑  空格，  list 里面的 字母是一样的，不考虑顺序
#

S_T = 'Is an anagram.'
S_F = 'Is not an anagram.'


def my_print(x, end="\n"):
    # print(x, end=end)
    pass


def my_input():
    str_1 = input()
    str_2 = input()
    return str_1, str_2
    pass


def my_run(str_1, str_2):
    s_1 = [x for x in list(str_1) if x != ' ']
    s_2 = [x for x in list(str_2) if x != ' ']

    if sorted(s_1) == sorted(s_2):
        res = S_T
    else:
        res = S_F
    return res
    pass


def my_unit_test():
    pass


def my_func_test():
    assert my_run('ITEM', 'TIME') == S_T
    assert my_run('CS AT WATERLOO', 'COOL AS WET ART') == S_T
    pass


def my_main():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()
    str_1, str_2 = my_input()
    res = my_run(str_1, str_2)
    print(res)


my_main()
