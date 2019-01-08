#
#
#

def my_print(x, end="\n"):
    print(x, end=end)


def my_run(a, e):
    res = []
    if a >= 3 and e <= 4:
        res.append("TroyMartian")
    if a <= 6 and e >= 2:
        res.append("VladSaturnian")
    if a <= 2 and e <= 3:
        res.append("GraemeMercurian")
    return res


def my_func_test():
    assert my_run(4, 5) == ["VladSaturnian"]
    assert my_run(2, 3) == ["VladSaturnian", "GraemeMercurian"]
    assert my_run(8, 6) == []


def my_main():
    print("How many antennas?")
    a = int(input())
    print("How many eyes?")
    e = int(input())
    res = my_run(a, e)
    if not res:
        pass
    else:
        print("\n".join(res))

    pass


my_main()
# ßmy_func_test()
