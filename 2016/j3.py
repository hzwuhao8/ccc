def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run("banana") == 5
    assert my_run("abracadabra") == 3
    assert my_run("abba") == 4


def my_run(my_str):
    for i in range(len(my_str) + 1, 1, -1):
        tmp_list = list(my_str)
        for k in range(len(my_str) - i + 1):
            tmp_list2 = tmp_list[k: k + i]
            tmp_str = "".join(tmp_list2)
            my_print("i={0} k={1} tmp_str={2}".format(i, k, tmp_str))
            if is_palindrome(tmp_str):
                return i
    return 1


def is_palindrome(my_str):
    l0 = list(my_str)
    l0.reverse()
    r = "".join(l0)
    return my_str == r


def my_unit_test():
    assert is_palindrome("a")
    assert is_palindrome("abba")
    assert is_palindrome("aba")
    assert is_palindrome("abccba")
    assert not is_palindrome("bamama")


my_unit_test()
my_func_test()
