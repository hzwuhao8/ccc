#J1
import logging

FORMAT='%(funcName)s:%(lineno)d:%(levelname)s %(message)s'
logging.basicConfig(level='ERROR',format=FORMAT)
log = logging.getLogger("J1")


def myinput():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    return ((a,b,c,d))

def check(a,b,c,d):
    t1 = a == 8 or a == 9
    t2 = d == 8 or d == 9
    t3 = b == c
    if t1 and t2 and t3 :
        return 'ignore'
    else:
        return 'answer'


#assert check(9,6,6,8) == "ignore"
#assert check(5,6,6,8) == "answer"

((a,b,c,d)) = myinput()
log.debug((a,b,c,d))

res = check(a,b,c,d)
log.debug(res)
print(res)
