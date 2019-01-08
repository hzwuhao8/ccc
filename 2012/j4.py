def my_print(x):
    print(x)
    pass


def encode(c, s):
    t = (ord(c) + s)
    if t > ord('Z'):
        t = t - 26
    return chr(t)


def decode(e, s):
    t = (ord(e) - s)
    if t < ord('A'):
        t = t + 26
    return chr(t)


def my_run(k, e_str):
    res = []
    for i in range(len(e_str)):
        e = e_str[i]
        s = 3 * (i + 1) + k
        c = decode(e, s)
        res.append(c)
    return "".join(res)


def my_unit_test():
    assert decode('F', 6) == 'Z'
    assert decode('X', 9) == 'O'
    s = 10
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        e = encode(c, s)
        c1 = decode(e, s)
        assert c == c1


def my_func_test():
    assert my_run(3, "FXAB") == "ZOOM"
    assert my_run(5, "JTUSUKG") == "BIGBANG"


my_unit_test()

my_func_test()


def my_main():
    k = int(input())
    enc_str = input()
    res = my_run(k, enc_str)
    print(res)


my_main()
