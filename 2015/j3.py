def my_unit_test():
    assert my_encode("j") == "jik", my_encode("j")
    assert my_encode("y") == "yuz"
    assert my_encode("h") == "hij"
    assert my_encode("m") == "mon"
    assert my_encode("a") == "a"


def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run("joy") == "jikoyuz"
    assert my_run("ham") == "hijamon"


def my_encode(c):
    vowel_list = ["a", "e", "i", "o", "u"]

    if c in vowel_list:
        return c
    else:
        my_str = c

        dic = {}
        for x in vowel_list:
            dic[x + c] = abs(ord(c) - ord(x))
        my_print(dic)
        a_list = list(dic.items())
        my_print(a_list)
        a_list.sort(key=lambda xx: (xx[1], xx[0]))
        c2 = a_list[0][0][0]
        my_print("c2={0}".format(c2))
        my_str += c2
        my_print(my_str)
        if c == "z":
            c3 = c
        else:
            for i in range(1, 26):
                next_c = chr(ord(c) + i)
                if next_c not in vowel_list:
                    c3 = next_c
                    break
        my_print("c3={0}".format(c3))
        my_str += c3
        my_print(my_str)
        return my_str


def my_run(my_str):
    res = "".join([my_encode(c) for c in my_str])
    return res


def my_main():
    my_str = input()
    res = my_run(my_str)
    print(res)


my_unit_test()

my_func_test()

my_main()
