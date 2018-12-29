

def myinput():
    start = int(input())
    stop = int(input())
    return (start,stop)

def myfunc(start,stop):
    step = 3*4*5
    if start == stop:
        return [start]
    else:
        return list(range(start, stop+1, step))

assert (myfunc(2000,2000) == [2000]), f"{myfunc(2000,2000)}"
assert (myfunc(2004,2100) == [2004,2064]), f"{myfunc(2004,2100)}"

(start,stop) = myinput()
res = myfunc(start,stop)
for x in res:
    print(f"All positions would change in year {x}")