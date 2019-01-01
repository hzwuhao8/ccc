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


# use  stack
def my_check_stack(my_str):
    my_print("="*40)
    my_print(my_str)
    stack_a= []
    stack_b = []
    for s in my_str:
        my_print("{0} push {1}".format(stack_a,s))
        # my_print(stack_b)
        if 'A' == s:
            if len(stack_a) == 0 :
                stack_a.append(s)
            elif len(stack_a) == 1 :
                stack_a.append(s)
            else:
                c1 = stack_a.pop()
                c2 = stack_a.pop()
                if 'A' == c2 and 'N' == c1:
                    stack_a.append(s)
                else:
                    stack_a.append(c2)
                    stack_a.append(c1)
                    stack_a.append(s)
        if 'N' == s:
            stack_a.append(s)
        if 'B' == s:
            stack_a.append(s)
        if 'S' == s:
            if len(stack_a) >= 2:
                c1 = stack_a.pop()
                c2 = stack_a.pop()
                if 'B' == c2 and 'A' == c1:

                    # 需要继续处理
                    if len(stack_a) >= 2:
                        x1 = stack_a.pop()
                        x2 = stack_a.pop()
                        if 'A' == x2 and 'N' == x1:
                            stack_a.append('A')
                        else:
                            stack_a.append(x2)
                            stack_a.append(x1)
                            stack_a.append('A')
                    else:
                        stack_a.append('A')
                else:
                    stack_a.append(c2)
                    stack_a.append(c1)

            else:
                stack_a.append(s)

    my_print(stack_a)
    # my_print(stack_b)
    return stack_a == ['A']
    # pass




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
        if my_check_stack(s):
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


my_check_stack('A')

my_check_stack('ANA')

my_check_stack('BANANANBANBASNASS')

