#J2
import logging

FORMAT='%(funcName)s:%(lineno)d:%(levelname)s %(message)s'
logging.basicConfig(level='ERROR',format=FORMAT)
log = logging.getLogger("J2")

def myinput():
    total = int(input())
    line1 = input()
    line2 = input()
    return (total,line1,line2)

def check(total,line1,line2):
    mycount = 0 ;
    for i in range(total):
        c1 = line1[i]
        c2 = line2[i]
        if c1 == 'C' and c1 == c2 :
            mycount = mycount + 1

    return mycount

assert check(5 , "CC..C", ".CC..") == 1
assert check(7 , "CCCCCCC", "C.C.C.C") == 4

(t,l1,l2) = myinput()
res = check(t,l1,l2)
print(res)

