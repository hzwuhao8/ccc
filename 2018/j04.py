#1 矩阵 90 度 旋转
#2 判断 每一行， 每一列符合要求； 行  递增， 列 递增


def myprint(x):
    pass
    #print(x)


def isDes(lx1):
    lx2 = lx1.copy()
    lx3 = lx1.copy()
    lx3.sort()
    return (lx3 == lx2)


def rotate90(n,xx):
    res = []
    for i in range(n):
        res.append([0]*n)

    for i in range(n):
        for j in range(n):
          res[i][j]= xx[n-j-1][i]
    return res

def allisok(n,xxx):
    flag = 1==1
    for i in range(n):
        flag = isDes( xxx[i])
        if not flag:
            myprint( f"i={i}; xxx[i] = {xxx[i]}  f={flag} FLAG={ isDes(xxx[i])}" )
            #break
            return flag
        
    for i in range(n):
        tmp = []
        for j in range(n):
          tmp.append( xxx[j][i])
        flag = isDes( tmp)
        if not flag:
            myprint( f"i={i}; tmp={tmp} f={flag} FLAG={ isDes( tmp )}" )
            break  
    return flag


assert isDes( [1,2,3])
assert not isDes( [4,3,1])
assert isDes( [11, 12, 31])

l1 = [[11,12,13],[21,22,23],[31,32,33]]

def t1(la):
   lb=la.copy()
   for i in range(5):
        myprint("="*20 + str(i) + "="*20)
        myprint(f"lb={lb}")
        l2 = rotate90(3,lb)
        myprint(f"l2={l2}")
        myprint( allisok(3, l2))
        myprint("="*40)
        lb = l2

#t1(l1)


def myinput():
    n = int(input())
    d = []
    for i in range(n):
        line = input()
        l = [int(x) for x in line.split( " ")]
        d.append(l)
    return (n,d)

def run():
    (n,data) = myinput()
    myprint( f"n={n} data={data} ")
    for i in range(5):
       d1 = rotate90(n, data)
       if allisok(n, d1):
           #print(d1)
           break 
       else:
           data = d1 
    return d1

res = run()
for i in range(len(res)):
    print( " ".join( [str(x) for x in res[i]] ))
