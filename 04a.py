#冒泡排序， 这个是最少吗？

def mysort(mylist):
    size = len(mylist)
    count=0
    for i in range(size-1):
        #print(i)
        index = size - i-1 
        #print(f'index={index}')
        a=mylist[index]
        b=mylist[index-1]
        if b < a:
            mylist[index]=b
            mylist[index-1]=a
            count= count+1

    return (mylist,count)

def mysort2(mylist):
    total = 0
    for x in range(100):
        (l2 ,  count)= mysort(mylist)
        mylist = l2
        print(l2)
        total=total+count
        if count ==0:
            break
    return (mylist,total)

def mytest1():
    print(mysort2( [1,2,3,4,5,6,7,9,10,11]))
    print(mysort2([2,1,3]))
    print(mysort2([3,2,1]))
    print(mysort2([1, 2, 3]))
    print(mysort2([15,14,13,1,10,9,8,12]))

def myinput():
    N = int(input())
    str = input()
    mylist = [int(x) for x in str.strip().split(" ")]
    return (N, mylist)

def mymain():
    (N,mylist) = myinput()
    (res, total) = mysort2( mylist)
    #print(res)
    return total

mytest1()
#print( mymain() )
