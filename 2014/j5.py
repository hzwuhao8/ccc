def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run(4, "Ada Alan Grace John", "John Grace Alan Ada") == "good"
    assert my_run(7, "Rich Graeme Michelle Sandy Vlado Ron Jacob",
                  "Ron Vlado Sandy Michelle Rich Graeme Jacob") == "bad"


def my_run(total, str_a, str_b):
    list_a = str_a.split()
    list_b = str_b.split()
    if len(list_a) == total and len(list_b) == total:
        zip_list = list(zip(list_a, list_b))
        my_print(zip_list)
        for a, b in zip_list:
            if a == b or (b, a) not in zip_list:
                return "bad"
        return "good"
    else:
        return "bad"

    pass


def my_main():
    n = int(input())
    str_a = input()
    str_b = input()
    res = my_run(n, str_a, str_b)
    print(res)


my_func_test()

my_main()
