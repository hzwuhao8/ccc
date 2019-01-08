# 用穷举法

def myprint(x):
    pass
    #print(x)



def is_rsa(n):
    res= []
    for i in range(2, n//2+1):
        if n % i == 0:
            res.append(i)
    res = [1] + res + [n]
    myprint(res)
    return  len(res) == 4

def myinput():
    start = int(input())
    stop = int(input())
    return (start , stop )

def main():
    (start , stop ) = myinput()
    total = 0
    for i in range(start , stop +1 ):
        if is_rsa(i):
            total = total + 1
    print(f"The number of RSA numbers between {start} and {stop} is {total}.")

assert is_rsa(10) ,f"is_rsa(10)={is_rsa(10)}"

assert is_rsa(15) ,f"is_rsa(10)={is_rsa(15)}"

assert not is_rsa(12) ,f"is_rsa(10)={is_rsa(12)}"

assert not is_rsa(11) ,f"is_rsa(10)={is_rsa(11)}"


main()
