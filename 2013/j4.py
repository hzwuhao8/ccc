def my_func_test():
    assert my_run(6, [3, 6, 3]) == 2
    assert my_run(6, [5, 4, 3, 2, 1]) == 3


# 从小 加到大
def my_run(limit, task_list):
    task_list.sort()
    total = 0
    for i in range(len(task_list)):
        # print("i={0} total={1}".format(i,total))
        total += task_list[i]
        if total >= limit:
            return i + 1
        else:
            pass

    return len(task_list)

    pass


my_func_test()


def my_main():
    limit = int(input())
    size = int(input())
    task_list = []
    for i in range(size):
        task_list.append(int(input()))
    res = my_run(limit, task_list)
    print(res)


my_main()
