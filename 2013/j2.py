def my_func_test():
    assert my_run("SHINS") == "YES"
    assert my_run("NOISE") == "NO"


def my_run(my_str):
    base_set = set("IOSHZXN")
    s1 = set(my_str)
    s2 = s1.difference(base_set)
    # print("base_set={0} s1={1} s2={2}".format(base_set,s1,s2))

    if len(s2) == 0:
        return "YES"
    else:
        return "NO"


my_func_test()


def my_main():
    my_str = input()
    my_res = my_run(my_str)
    print(my_res)

my_main()
