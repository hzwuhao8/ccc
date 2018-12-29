#
#1 y1=y2 a = x2 - x1 ; (x1,y1) (x2,y2) => (x1,y1),(x1+a/3, y1) (x1+a/3, y1+a/3), (x1+2a/3, y1+a/3),(x1+2a/3, y1) , (x2,y1)

#2 x1=x2 ; b= y2 - y1 ; (x1,y1) (x1,y1+b/3), (x1 -3/b, y1+b/3) ,(x1-3/b, y1+2b/3) ,(x1, y1+2b/3),(x2,y2)

def myprint(x):
    pass
    #rint(x)

def myinput():
    line1= input()

    [level,length,x] = [int(x) for x in line1.strip().split()]
    return (level, length, x )

#扩张
def extend( seg  ):
    (p1,p2) = seg
    (x1,y1) = p1
    (x2,y2) = p2
    base = 3
    res = []
    if x1 == x2:
        b = y2  - y1
        delta = b // base
        res.append(((x1,y1) ,(x1, y1 + delta)) )
        res.append(((x1, y1+delta), (x1-delta, y1+delta)))
        res.append(((x1-delta, y1+delta), (x1-delta, y1 + 2*delta)))
        res.append(((x1-delta, y1+2*delta), (x1, y1+ 2*delta)))
        res.append(((x1, y1+ 2*delta), (x2, y2)))

    elif y1 == y2:
        a = x2 - x1
        delta = a // base
        res.append(((x1, y1), (x1+delta , y1 )))
        res.append(((x1 + delta , y1  ), (x1 +  delta, y1 + delta)))
        res.append(((x1 + delta, y1 + delta), (x1 +2* delta, y1 +  delta)))
        res.append(((x1 +2 * delta, y1 +   delta), (x1 +2*delta , y1 )))
        res.append(((x1 +2*delta , y1 ), (x2, y2)))


    else:
        myprint(f"ERROR (x1,y1),(x2,y2)={(x1,y1),(x2,y2)}")

    return res


#从 res  提取 满足 要求的数据

def search(data, x):
    res = []
    for pp in data:
        #myprint(pp)
        (p1, p2) = pp
        (x1, y1) = p1
        (x2, y2) = p2
        if x1 == x:
            res.append(y1)
        if x2 == x:
            res.append(y2)
        if x1 > x and x2 < x:
            res.append(y2)
        if x1 <x and x2 > x:
            res.append(y2)
        if x1 == x2 == x:
            if y1 < y2 :
                res = res + list(range(y1,y2))
            else:
                res = res + list(range(y2,y1))


    myprint(res)
    res2 = list(set(res))
    res2.sort()
    return res2


#level
def level_extend( seg0 , level ):

    data=[seg0]
    res=[seg0]
    for i in range(level):
        res = []
        for seg in data:
            #myprint(f"seg={seg}")
            r1 = extend( seg )
            myprint(f"r={i} r1={r1}")
            res = res + r1
        data = res
    return res


def myrun( level, length, x):
    seg=((0,1),(length,1))
    data = level_extend(seg ,level)
    res = search(data,x)
    return res


def main():
    (level, length ,x) = myinput()
    r = myrun(level, length ,x )

    r1 = " ".join( [str(x) for x in r])
    print(r1)

main()
quit()

seg1 = ((0,0),(27,0))
myprint ( extend( seg1 ) )

seg2 = ((9,0),(9,9))
myprint ( extend( seg2 ) )

assert ( extend( seg1 ) ) == [ ((0,0),(9,0)), ((9,0),(9,9)),((9,9),(18,9)),((18,9),(18,0)), ((18,0),(27,0))          ], f"extend(seg1)"

myprint( level_extend( seg1 , 1 ))

myprint( "===="*10)
seg1 = ((0,1),(81,1))
t1 =  level_extend( seg1 , 2 )
myprint( t1 )
myprint( search(t1 , 36))
#myprint( level_extend( seg1 , 3 ))

#r1=myrun(3,27,5)
#myprint(r1)
#r1=myrun(4,81,38)
#myprint(r1)