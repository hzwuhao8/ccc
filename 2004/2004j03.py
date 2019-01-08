
def myprint(x):
    pass
    #print(x)

def myinput():
    a_num = int(input())
    n_num = int(input())
    a_list = []
    n_list = []
    for i in range(a_num):
        str = input()
        a_list.append(str.strip())
    for i in range(n_num):
        str = input()
        n_list.append(str.strip())
    return (a_list,n_list)



def myfunc(adj_list, nouns_list):
    res=[]
    for a in adj_list:
        for n in nouns_list:
            res.append(f"{a} as {n}")
    return res


assert myfunc([1,2],['a']) ==["1 as a","2 as a"], f"myfunc([1,2],['a'])={myfunc([1,2],['a'])}"
assert myfunc(['A'],['z']) ==["A as z"], f"myfunc(['A'],['z'])={myfunc(['A'],['z'])}"

(adj_list,nouns_list) = myinput()

myprint((adj_list,nouns_list))
res = myfunc(adj_list,nouns_list)
for x in res:
    print(f"{x}")