def median(x,y,z):
    step1 = [x,y,z]
    step1.sort()
    result = step1[1]
    return result

def mymain():
    assert 1 == median(1, 1, 1)
    assert 2 == median(1, 2, 3)
    assert 1 == median(1, 1, 3)
    assert 2 == median(3, 2, 2)

def myinput():
    str1 = input()
    str2 = input()
    [N,X] = [int(x) for x in  str1.strip().split(" ")]
    #print(N)
    #print(X)
    mylist = [int(x) for x in str2.strip().split(" ")]
    #print(mylist)
    return (N,X,mylist)

def search(mylist,X):
    result = 0
    i=0
    j=0
    k=0
    for ai in mylist:
        j=i+1
        i=i+1
        for aj in mylist[j:]:
            k=j+1
            j=j+1
            for ak in mylist[k:]:
                if median(ai,aj,ak) == X:
                    #print([ai,aj,ak])
                    result = result + 1

    return result

#mymain()
(N,X,mylist) = myinput()
print( search(mylist , X ))