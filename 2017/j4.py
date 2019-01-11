T = 12 * 60


def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run(34) == 1
    assert my_run(180) == 11


def my_run(t):
    m = t // T
    tt = t % T
    return m * my_run_1(T) + my_run_1(tt)


def my_run_1(t):
    total = 0
    for i in range(1, t + 1):
        my_time = add_min(i)
        if is_seq(my_time):
            total += 1

    return total


def my_unit_test():
    assert is_seq("12:34")
    assert is_seq("2:10")
    assert not is_seq("1:24")

    assert add_min(1) == "12:01"
    assert add_min(34) == "12:34"
    assert add_min(120) == "2:00"
    assert add_min(12 * 60) == "12:00", add_min(12 * 60)
    assert add_min(12 * 60 - 1) == "11:59", add_min(12 * 60 - 1)


def add_min(t):
    t1 = t % T
    h = (t1 // 60) % 12
    m = t1 % 60
    if h == 0:
        h = 12
    my_str = "{0}:{1:02}".format(h, m)
    return my_str
    pass


dic_cache = {}


def is_seq(my_str):
    if my_str in dic_cache:
        return dic_cache[my_str]
    else:
        s1 = my_str.replace(':', '')
        s_seq = [int(x) for x in s1]
        d1 = s_seq[:-1]
        d2 = s_seq[1:]
        d_zip = zip(d1, d2)
        d3 = [x[0] - x[1] for x in d_zip]
        d4 = set(d3)
        dic_cache[my_str] = len(d4) == 1
        return len(d4) == 1


def my_main():
    t = int(input())
    res = my_run(t)
    print(res)


my_unit_test()

my_func_test()

my_main()

