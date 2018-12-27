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
     [a,b,c,d] = data
     r1 = [0,0,0,0,0]
     r1[1] = data[0] ; r1[2] = r1[1]+data[1] ; r1[3] = r1[2]+ data[2]; r1[4] = r1[3]+data[3]  
     myprint(r1)
     r2 = [r1[1], 0, 0, 0, 0]
     r2[2] = data[1]; r2[3] = r2[2] + data[2]; r2[4] = r2[3] + data[3]
     myprint(r2)
     r3 = [ r1[2], r2[2], 0 , data[2], data[2]+data[3]] 
     myprint(r3)
     r4 = [ r1[3], r2[3], r3[3],0 , data[3] ]
     myprint(r4)
     r5 = [r1[4], r2[4], r3[4],r4[4],0 ]    
     myprint(r5)
     return [r1,r2,r3,r4,r5]     

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




