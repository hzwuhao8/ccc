def myprint(x):
    pass
    print(x)


def myinput():
    pass

#加密  模 26
# 'A' -> 1 'B' -> 2

char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
int_list = list(range(1,27))

char_int_dict = dict( zip( char_list, int_list ))
int_char_dict = dict( zip( int_list, char_list  ))

def encode(x, c):
    x2 = char_int_dict[c]
    x3 = (x + x2) % 26
    if x3 == 0:
        x3 = 26
    c3 = int_char_dict[x3]
    return c3

#行加密
def encode2(passwd, mystr):
    maxsize = min(len(passwd), len(mystr))
    res=[]
    for i in range(maxsize):
        x = char_int_dict[ passwd[i]] - 1
        c = mystr[i]
        c2 = encode(x,c)
        res.append(c2)
    return "".join(res)

def myfunc(password,msg):
    msg1 = filter(lambda x: x >= 'A' and x <='Z' , msg)
    msg2 = list(msg1)
    pagesize = len(password)

    page = len(msg2)//pagesize + 1
    msg3 = []
    if len(msg2) % pagesize == 0 :
        page = page - 1
    index =0
    for i in range(page):
        msg3.append( msg2[index:index+pagesize])
        index = index + pagesize

    myprint(msg3)
    res = []
    for s1 in msg3:
        s2 = encode2(password, s1)
        res.append(s2)
    #加密
    return "".join(res)

    #pass


assert encode(5,'B')=='G',f"encode(5,'B')={encode(5,'B')}"
assert encode(5,'T')=='Y',f"encode(5,'T')={encode(5,'Y')}"
assert encode(5,'V')=='A',f"encode(5,'V')={encode(5,'A')}"
assert encode2("ACT","BAN") == "BCG", f'encode2("ACT","BAN")={encode2("ACT","BAN")}'

assert myfunc("ACT","BANANA & PEEL") == "BCGAPTPGXL" , myfunc("ACT","BANANA & PEEL")
assert myfunc("TRICKY","I LOVE PROGRAMMING!") == "BCWXONKFOTKKFZVI" , myfunc("TRICKY","I LOVE PROGRAMMING!")


