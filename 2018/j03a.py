def  myprint(x):
     pass
     #print(x)

def  myout(L):
     return  " ".join(str(x) for x in L) 

def  myinput():
     line1=input()
     data = [ int(x) for x in line1.strip().split(" ") ]
     return data


def  myfunc(data):
     res = []
     size = len(data)
     size2 = size + 1 
     for k in range( size2 ):
       r = []
       for i in range(k):
         r.append(0)
       t = 0
       for i in range(size-k):
         r.append(t)
         t = t + data[i+k]
       r.append(t)
       myprint(r)
       res.append(r)
     
     for k in range(size2):
       for i in range(k):
          res[k][i] = res[i][ k ] 
     return res


d = myinput()
myprint(d)
res = myfunc(d)
myprint(res)
myprint("=====1=======")
myprint(myout(res[0]))
myprint(f"{myout(res[0])}xxx")
myprint("=====1=======")


for r in res:
    print(f"{myout(r)} ")




