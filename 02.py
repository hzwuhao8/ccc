def myf(list):
    #print(list)
    maxresult = 10
    a = dict()
    for x in list:
        if x in a:
            a[x] = a[x] + 1
        else:
            a[x] = 1
    result = maxresult
    mymax = 0

    # print(a)
    for k, v in a.items():
        # print(k,v)
        if v > mymax or (v==mymax and k <= result):
            result = k
            mymax = v

    return result

def mymain():
    mysize = int(input())

    mystr =input()
    # print(mystr)
    mylist = mystr.strip().split(" ")
    #print(mylist)

    mylist2 = [int(x) for x in mylist]
    # print(mylist2)

    print(myf(mylist2[0:mysize]))
mymain()
