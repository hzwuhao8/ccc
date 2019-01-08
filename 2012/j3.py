base_data = ["*x*", " xx", "* *"]


def my_func_test():
    res = my_run(base_data, 3)

    assert len(res) == 9
    assert len(res[0]) == 9
    assert res[1] == "***xxx***"


def my_run(base, k):
    res = []
    for line in base:
        my_str = [c * k for c in line]
        for i in range(k):
            res.append("".join(my_str))
    return res


my_func_test()

