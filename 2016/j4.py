def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run("04:00") == "06:00"
    assert my_run("05:00") == "07:00"
    assert my_run("05:20") == "07:40"
    assert my_run("23:20") == "01:20"
    assert my_run("07:00") == "10:30"


def my_run(my_time):
    h, m = [int(x) for x in my_time.split(":")]
    my_print("h={0},m={1}".format(h, m))
    res = ""
    if False and not is_rush(h, m) and not is_rush_end((h + 2) % 24, m):
        res = "{0:02}:{1:02}".format((h + 2) % 24, m)
    else:
        # 需要延迟的时间 20min 为间隔
        # 最多 240 分钟 设 距离为 240 ;   v=2 ; v =1
        s = 240
        for i in range(1, 240):
            h1, m1 = add_min(h, m, i)
            if is_rush(h1, m1):
                v = 1
            else:
                v = 2
            s = s - v
            my_print("s={0},v={1}, i={2}, hm1={3:02}:{4:02}".format(s, v, i, h1, m1))
            if s == 0:
                h2, m2 = add_min(h, m, i)
                res = "{0:02}:{1:02}".format(h2, m2)
                break
            if s <= 0:
                h2, m2 = add_min(h, m, i)
                res = "{0:02}:{1:02}".format(h2, m2)
                break
    my_print("res={0}".format(res))
    return res


def is_rush(h, m):
    rush_hour = [8, 9, 16, 17, 18, ]
    rush_hour_2 = [7, 15]
    rush_hour_3 = [10, 19]
    if h in rush_hour:
        return True
    elif h in rush_hour_2 and m > 0:
        return True
    elif h in rush_hour_3 and m > 0:
        return False
    else:
        return False


# 时间 增加, 数值的变化
def add_min(h, m, delta_m):
    m1 = m + delta_m
    delta_h = 0
    if m1 >= 60:
        delta_h = m1 // 60
        m1 = m1 % 60
    h1 = (h + delta_h) % 24
    return h1, m1


def my_unit_test():
    assert is_rush(8, 30)
    assert is_rush(9, 30)
    assert is_rush(15, 30)
    assert not is_rush(7, 00)
    assert is_rush(7, 1)
    assert is_rush(9, 59)
    assert not is_rush(10, 0)
    assert not is_rush(10, 00)
    assert not is_rush(12, 20)

    assert add_min(0, 10, 50) == (1, 0)
    assert add_min(23, 20, 120) == (1, 20)


my_unit_test()

my_func_test()
