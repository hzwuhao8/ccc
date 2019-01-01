#
# 1 原有的规则的基础上， 新增加了规则，
# 2 有可能规则是有矛盾的
#


def my_print(x):
    # print(x)
    pass


def my_input():
    res = []
    while True:
        x1 = int(input())
        x2 = int(input())
        if x1 == 0 and x2 ==0:
            break
        else:
            res.append((x1, x2))
    return res
    pass


def is_right(y, rules, over):
    my_print("y={0}, rules={1}, over={2}".format(y, rules, over))
    res = is_right_1(y, rules, over)
    my_print("res={0}".format(res))
    return res


def is_right_1(y, rules, over):
    prefix = [p[0] for p in rules if p[1] == y]
    if set(over).intersection(set(prefix)) == set(prefix):
        return True
    else:
        return False





base_rules = [(1, 7), (1, 4), (2, 1), (3, 4), (3, 5)]


def my_run(data):
    res = []
    rules = base_rules + data
    my_print(rules)
    not_free_var = [x[1] for x in rules ]
    my_print("not_free_var={0}".format(not_free_var))
    free_var = [i for i in range(1, 8) if i not in not_free_var ]
    my_print("free_var={0}".format(free_var))
    free_var = [i for i in range(1, 8) if is_right(i, rules, [])]
    if free_var == []:
        return []
    else:
        for i in range(7):
            if free_var == []:
                return []
            else:
                step_1 = min(free_var)
                res.append(step_1)
                free_var = free_var + [x[1] for x in rules if x[0] == step_1 and
                                       is_right(x[1], rules, res)]
                free_var.remove(step_1)
                my_print("res={0} free_var={1}".format(res, free_var))

        return res


def my_test():
    assert my_run([(6, 2), (5, 4)]) == [3, 5, 6, 2, 1, 4, 7]
    assert my_run([(7, 2), (4, 5)]) == []
    pass


def my_main():
    my_test()
    rr = my_input()
    res = my_run(rr)
    if not res:
        print("Cannot complete these tasks.  Going to bed.")
    else:
        print(" ".join([str(x) for x in res]))


my_main()
