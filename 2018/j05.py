# 1  图， 是否联通
# 2  求从第一页 到 最后 一页的 最短路径

# 采用二维矩阵 表示 图； 如有有链接； a(i)(j) = 1 ; 否则 a(i)(j) =0
# 10000 ; 递归方法， 不知道 是否可以？
# 联通；    1个节点 ； 2个节点
# 强联通的   边集 数量 大于等于 顶点的数量
# 边集； 用 List 表示；
# (0,0)
# (1,1)
# V node =  range(n)
# E  (n1,n2) ; 表述 有 n1 -> n2 的 链接
# 可以考虑 E 作为一个  Dict？   便于搜索？

#2019 -01-11  ; 10天前 写的 代码 看不懂了


def myprint(x):
    pass
    # print(x)


def searchOne(E, lista):
    myprint(f"before extend lista={lista}")
    tmpa = []
    for n in lista:
        tmp2 = E.get(n, [])
        tmpa = tmpa + tmp2
    if tmpa == []:
        myprint(f"没有新增加节点")
    return tmpa


def reachable(E, V):
    totalNodeList = [1]
    realadd = [1]
    for x in range(100):
        tmpresult = searchOne(E, realadd)
        realadd = []
        for x in tmpresult:
            if x in totalNodeList:
                pass
            else:
                realadd.append(x)
                totalNodeList.append(x)
        if realadd == []:
            break
    myprint(f"totalNodeList={totalNodeList}")

    if len(totalNodeList) == len(V):
        return 'Y'
    else:
        return 'N'


# 从1 出发的 最短路径； 如果不可达； 返回 -1
# 求出 所有路径
# 找到 所有从 到 n 的 节点
# 找到 到 这些 节点的  节点，  如果出现  1 这知道了 最短路径需要 链接表； 就 比较简单了
# 或者 建立一个 反向的 链接表
# 求出 最短路径

# 求能够到达该节点的 节点集合
def path_one_step1(E, n, revE):
    res = revE.get(n, [])

    myprint(f"节点={n} 找到的节点 res={res}")
    return res


def path_one_step(E, nList, revE):
    res = []
    for n in nList:
        t1 = path_one_step1(E, n, revE)
        for x in t1:
            if x in res or x in nList:
                pass
            else:
                res.append(x)
    myprint(f"nList={nList} 找到的节点 res={res}")
    return res


def short1(E, n, revE):
    beginList = [n]
    if 1 in beginList:
        return 1

    extends = []

    for i in range(100):
        myprint(f"*************第{i}次扩张")
        extends = path_one_step(E, beginList, revE)
        if extends == []:
            return -1

        if 1 in extends:
            return i + 2
        else:
            beginList = extends

    return -1


# 找到端点 节点
# 找到 1 -> 该节点的最短路径
# 找到  所有  端节点 中的  最短路径的  最短路径

def short(E, V, revE):
    myprint("===" * 20)
    tn = []
    for n in V:
        if E.get(n, []) == []:
            tn.append(n)
    myprint(f"端点集合={tn}")
    if 1 in tn:
        res = 1
    else:
        tn2 = [short1(E, n, revE) for n in tn]
        tn3 = list(filter(lambda x: x >= 1, tn2))
        res = min(tn3)
        myprint(f"最短={res}")
    return res


def mytest():
    V = [1, 2, 3]
    E1 = {1: [2, 3]}
    revE1 = {2: [1], 3: [1]}
    E2 = {1: [3], 3: [1]}
    revE2 = {3: [1], 1: [3]}
    res = reachable(E1, V)
    myprint(res)
    res = reachable(E2, V)
    myprint(res)
    path_one_step1(E1, 2, revE1)
    path_one_step(E1, [2, 3], revE1)
    short(E1, V, revE1)
    myprint(f"E= 空集")
    res = short({}, V, {})
    myprint(f"res={res}")


mytest()


def myinput():
    n = int(input())
    V = range(1, n + 1)
    # 到达点 出
    E = {}
    # 进入点 进
    revE = {}

    for i in range(1, n + 1):
        line = input()
        ll = [int(x) for x in line.split(" ")]

        if ll[0] == 0:
            pass
        else:
            E[i] = ll[1:]
            for x in ll[1:]:
                tmp = revE.get(x, [])
                tmp.append(i)
                revE[x] = tmp

    return (E, V, revE)


(E, V, revE) = myinput()
myprint(f"input V={V}")
myprint(f"input E={E}")
myprint(f"input revE={revE}")

res1 = reachable(E, V)
res2 = short(E, V, revE)
print(res1)
print(res2)
