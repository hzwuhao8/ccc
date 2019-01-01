#use re

import re


def my_print(x):
    # print(x)
    pass


def my_reduce(s):
    r2 = re.compile('A(NA)+')
    r3 = re.compile('BAS')
    while True:
        s1 = r2.sub('A', s)
        s2 = r3.sub('A', s1)
        if s == s2:
            break
        s = s2
    return s


def my_check_re(s):
    my_print(s)
    s2 = my_reduce(s)
    return s2 == 'A'


def my_input():
    flag = True
    res = []
    while flag:
        s = input()
        if 'X' == s:
            break
        else:
            res.append(s)

    return res


def main():
    res = my_input()
    for s in res:
        if my_check_re(s):
            print('YES')
        else:
            print('NO')


main()

quit()

assert my_check_re('A'), "A is valid"
assert not my_check_re('B')
assert my_check_re('ANA')
assert my_check_re('ANANA')
assert my_check_re('BAS')
assert my_check_re('BANANAS')
