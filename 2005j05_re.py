#use re

import re
def  myprint(x):
    #print(x)
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


def my_check(s):
    myprint(s)
    r0 = re.compile('A')
    r1 = re.compile('ANA')
    r2 = re.compile('A(NA)+')
    r3 = re.compile('BAS')
    s2 = my_reduce(s)
    if r0.fullmatch(s2):
        myprint(f"s2={s2}, r={r0}")
        return True
    elif r1.fullmatch(s2):
        return True
    elif r3.findall(s2):
        return True
    else:
        return False
    pass


def myinput():
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
    res = myinput()
    for s  in res:
        if my_check(s):
          print('YES')
        else:
          print('NO')

main()

quit()

assert my_check('A') , "A is valid"
assert my_check('B') == False
assert my_check('ANA')
assert my_check('ANANA')
assert my_check('BAS')
assert my_check('BANANAS')
