def my_func_test():
    assert my_run([30, 10, 20, 20]) == "No Fish"
    assert my_run([1, 10, 12, 13]) == "Fish Rising"
    assert my_run([10, 9, 8, 7]) == "Fish Diving"


# 思路错误， 还是需要用 比较的方法
def my_run2(data):
    if data.count(data[0]) == 4:
        return "Fish At Constant Depth"
    ll = sorted(data)
    rev = data.copy()
    rev.reverse()
    if ll == data:
        return "Fish Rising"
    elif ll == rev:
        return "Fish Diving"
    else:
        return "No Fish"


def my_run(data):
    delta_list = []
    for i in range(len(data) - 1):
        delta = data[i + 1] - data[i]
        if delta > 0:
            delta_list.append(1)
        elif delta == 0:
            delta_list.append(0)
        else:
            delta_list.append(-1)

    if delta_list == [0, 0, 0]:
        return "Fish At Constant Depth"
    elif delta_list == [1, 1, 1]:
        return "Fish Rising"
    elif delta_list == [-1, -1, -1]:
        return "Fish Diving"
    else:
        return "No Fish"


my_func_test()


def my_main():
    data = [int(input()) for i in range(4)]
    res = my_run(data)
    print("{0}".format(res))


my_main()
