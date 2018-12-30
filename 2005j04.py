#
# 1 二维数组 ， 1 可以过， 0 不能过； -1 ；已经去过
# 2 在不同的象限  移动顺序 是不同，  4个 象限
# 3 根据 当前位置， 1 根据在哪个象限， 生成 移动序列， 4个可能， 在 选择第一个可以的移动， 继续下一步，    如果 无处可去  ，就不动

def myprint(x):
    #print(x)
    pass


def mprint(m):
    h=["'{:>4}'".format(str(x)) for x in range(len(m[0]))]
    myprint(f"    [{', '.join(h)}]")
    myprint("")
    for i in range(len(m)):
        tmp=[]
        for j in range(len(m[i])):
            x = m[i][j]
            if x <= -100:
                mystr = (f"{x}")
            elif x <= -10:
                mystr = (f" {x}")
            elif x < 0:
                mystr=(f"  {x}")
            else:
                mystr=(f"   {x}")
            tmp.append(mystr)
        index_str="{:>4}".format(str(i))
        myprint(f"{index_str}{tmp}")

def is_move_able(x,y,martix):
    rows = len(martix)
    cols = len(martix[0])
    if x < 0 or y <0  or x >= rows or y>=cols:
        return False
    else:
        if x==17 and y==8 :
            myprint(martix[x][y])
        if martix[x][y] == 1:
            return True
        else:
            return False


def move(x,y, martix ,step):
    x1 = -1
    y1 = -1

    next_seq = moveseq(x,y,martix)
    myprint(f"next_seq={next_seq}")
    flag = False
    for p in next_seq:
        (x1, y1) = p
        #myprint(f"is_move_able({x1},{y1} martix)={is_move_able(x1,y1, martix)}")
        if is_move_able(x1,y1, martix):
            flag = True
            break;

    if not flag :
        return (x,y)
    else:
        myprint(f"move to {x1},{y1}")
        martix[x1][y1] = -step
        mprint(martix)
        return (x1,y1)

def moveseq(x,y,martix):
    rows = len(martix)
    cols = len(martix[0])
    #myprint(f"rows={rows} cols={cols}")
    res = []
    if  x <= rows//2  and y < cols//2:
        res = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]

    elif x <= rows//2 and y >= cols//2:
        res = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
    elif x >= rows//2 and y < cols//2:
        res=[(x,y-1),(x-1,y),(x,y+1),(x+1,y)]
    else:
        res=[(x+1,y),(x,y-1),(x-1,y),(x,y+1)]

    return res

M1 = [[0,1,0],[1,1,1],[0,1,0]]

assert  moveseq(0,0,M1) == [(-1,0),(0,1),(1,0),(0,-1)] ,f"moveseq(0,0,M1)={moveseq(0,0,M1)}"

assert  moveseq(0,2,M1) == [(0,3),(1,2),(0,1),(-1,2)] ,f"moveseq(0,2,M1)={moveseq(0,2,M1)}"

assert  moveseq(2,2,M1) == [(3,2),(2,1),(1,2),(2,3)] ,f"moveseq(0,2,M1)={moveseq(2,2,M1)}"

assert  moveseq(2,0,M1) == [(2,-1),(1,0),(2,1),(3,0)] ,f"moveseq(0,2,M1)={moveseq(2,2,M1)}"


def myinput():
    cols = int(input())
    rows = int(input())
    col_cuts = int(input())
    row_cuts = int(input())
    step = int(input())
    row = [1]*cols
    row_cuted = [0]*col_cuts +[1]* (cols - 2*col_cuts) + [0]*col_cuts
    m = []
    for i in range(rows):
        if i <  row_cuts:
            myprint(row_cuted)
            m.append(row_cuted.copy())
        elif i + row_cuts >= rows :
            myprint(row_cuted)
            m.append(row_cuted.copy())
        else:
            myprint(row)
            m.append(row.copy())
    start_point=(0,col_cuts)
    m[0][col_cuts] = -1
    return (m, step,start_point)
    #myprint(m)


def main():
    (m,step, start_point) = myinput()
    (x,y) = start_point
    for i in range(step):
        myprint(f"step {i} ({x},{y})")
        (x1,y1) = move(x,y,m,i+2)
        x = x1
        y = y1
    #print((x1,y1))
    #print((y1+1,x1+1))
    print( y1+1)
    print( x1+1)

main()





