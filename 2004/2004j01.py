#
import math
def myinput():
    n = int(input())
    return n

def myfunc(n):
    n1 = math.sqrt(n)
    res = math.floor(n1)
    return res

assert  myfunc(8) == 2 , ""
assert  myfunc(9) == 3 , ""
assert  myfunc(7535) == 86 , ""

data = myinput()
res = myfunc(data)
print(f"The largest square has side length {res}.")
