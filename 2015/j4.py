##
# 没有想象的简单

###

def my_print(x):
    # print(x)
    pass


def my_func_test():
    assert my_run(["R 2", "R 3", "W 5", "S 2", "S 3"]) == [[2, 6], [3, 6]]
    assert my_run(["R 12", "W 2", "R 23", "W 3", "R 45", "S 45", "R 45", "S 23", "R 23", "W 2", "S 23", "R 34", "S 12",
                   "S 34"]) == [[12, 13], [23, 8], [34, 2], [45, -1]]


def my_run(cmd_list):
    current_time = 0
    dic = {}
    dic_time = {}
    is_first = True
    for i in range(len(cmd_list)):
        cmd = cmd_list[i]
        c, x0 = cmd.split()
        x = int(x0)
        if c == "W":
            current_time += x
        elif c == "R":
            my_round = dic.get(x, 0)
            dic[x] = my_round + 1
            if x not in dic_time:
                dic_time[x] = ([current_time], 0)
            else:
                t1 = dic_time[x]
                my_print("t1={0}".format(t1))
                t1[0].append(current_time)

            if i < len(cmd_list) - 1:
                if cmd_list[i + 1].startswith("W"):
                    pass
                else:
                    current_time += 1

        elif c == "S":
            my_round = dic.get(x, 0)
            dic[x] = my_round - 1
            if x not in dic_time:
                print("ERROR")
            else:
                t1 = dic_time[x]
                s1 = t1[0].pop()
                total = t1[1] + (current_time - s1)
                dic_time[x] = (t1[0], total)
            if i < len(cmd_list) - 1:
                if cmd_list[i + 1].startswith("W"):
                    pass
                else:
                    current_time += 1
        else:
            print("ERROR")

        my_print("cmd={0} dic={1} dic_time={2} current_time={3}".format(cmd, dic, dic_time, current_time))

    res = []
    for k, v in dic.items():
        if v != 0:
            res.append([k, -1])
        else:
            t1 = dic_time[k]
            t2 = t1[1]
            res.append([k, t2])
    res.sort()
    my_print("res={0}".format(res))
    return res
    pass


def my_main():
    total = int(input())
    cmd_str = []
    for i in range(total):
        cmd_str.append(input())
    my_print(cmd_str)
    res = my_run(cmd_str)
    for x in res:
        print("{0} {1}".format(x[0],x[1]))


my_func_test()

my_main()
