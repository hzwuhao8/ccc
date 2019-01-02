#
import copy

base_motels = [0, 990, 1010, 1970, 2030, 2940,
               3060, 3930, 4060, 4970, 5030,
               5990, 6010, 7000]


def my_print(x, end="\n"):
    # print(x, end=end)
    pass


def my_input():
    a = int(input())
    b = int(input())
    t = int(input())
    m_list = []
    for i in range(t):
        m_list.append(int(input()))
    return a, b, m_list
    pass


def my_run(a, b, add_motels):
    global real_res
    real_res = []
    motels = base_motels + add_motels
    motels = sorted(motels)
    my_print("motels={0}".format(motels))
    d_list = []
    for i in range(len(motels) - 1):
        d_list.append(motels[i + 1] - motels[i])

    my_print("d_list = {0}".format(d_list))
    if max(d_list) > b:
        return 0
    else:
        my_run_2(a, b, d_list, [], 1)
        res = len(real_res)
        res_1 = [x for x in real_res if is_right(a, b, x)]

        return len(res_1)


# 递归的方式处理
# 增加节点？ 对原有的结果 会有影响吗？
def my_run_1(a, b, d_list):
    size = len(d_list)
    index = 0
    tmp_list = [[]]
    while 0 <= index < size:
        my_print(tmp_list)
        next_p = d_list[index]
        maybe_dist = next_p + sum(tmp_list[-1])
        if a > maybe_dist:
            tmp_list[-1].append(next_p)
        elif b > maybe_dist:
            tmp_list[-1].append(next_p)
        else:
            if sum(tmp_list[-1]) < a:
                index = index - 1
                back_p = tmp_list[-1].pop()

            else:
                tmp_list.append([next_p])

        index += 1


def is_right(a, b, res):
    res_sum = [sum(x) for x in res]
    right_list = [x for x in res_sum if a <= x <= b]
    return len(right_list) == len(res_sum)  # 所有的 都符合要求


# 根据 剩余的节点遍历， 如果能 成功 则返回 后续的 组合方式， 如果 失败 则标记为失败
real_res = []


def my_run_2(a, b, d_list, tmp_res_ref, index):
    global real_res
    tmp_res = copy.deepcopy(tmp_res_ref)
    my_print(" " * index + "index={0}\td_list={2}\ttmp_res={1}".format(index, tmp_res, d_list))
    if not d_list:
        return real_res.append(tmp_res)
        pass
    if len(d_list) == 1:
        t1 = copy.deepcopy(tmp_res)
        t1.append(d_list)
        if t1 not in real_res:
            real_res.append(t1)
            my_print(" " * index + 't1={0}'.format(t1))

        t2 = copy.deepcopy(tmp_res)

        if len(t2) > 0 and t2[-1]:
            if sum(t2[-1]) + d_list[0] <= b:
                t2[-1].append(d_list[0])
                my_print(" " * index + 't2={0}'.format(t2))
                if t1 != t2 and t2 not in real_res:
                    #real_res.append(t2)
                    pass
        my_print(" " * index + "\t real_res={0}".format(real_res))
        return
    else:
        for i in range(1, len(d_list) + 1):
            add_list = d_list[:i]
            my_print(" " * index + "add_list={0}".format(add_list))
            if sum(add_list) < a:
                my_print(" " * index + "sum(add_list) < a")
                continue
            if sum(add_list) <= b:
                my_print(" " * index + "sum(add_list) < b\tlen(d_list) > 1")
                next_d_list = d_list[i:]
                x = copy.deepcopy(tmp_res)
                x.append(add_list)
                my_print(" " * index + "tmp_res={0}".format(x))
                my_run_2(a, b, next_d_list, x, index + 1)
                pass
            else:
                my_print(" " * index + "sum(add_list) > b")
                break

            pass


def my_unit_test():
    # my_run_1(1, 500, [990, 20, 960, 60, 910, 120, 870, 130, 910, 60, 960, 20, 990])
    # my_run_1(970, 1040, [990, 20, 960, 60, 910, 120, 870, 130, 910, 60, 960, 20, 990])

    # my_run_2(970, 1040, [990, 20, 960, 60, 910, 120, 870, 130, 910, 60, 960, 20, 990], [[]], 1)
    global real_res
    real_res = []
    my_run_2(1, 7000, [990, 20, 60 ], [], 1)
    my_print("real_res={0}".format("\n".join([str(x) for x in real_res])))
    my_print(len(real_res))
    # assert 1 == 0
    pass


def my_func_test():
    assert my_run(1, 500, []) == 0
    assert my_run(970, 1030, []) == 1
    assert my_run(970, 1040, []) == 4
    assert my_run(970, 1030, [4960]) == 2
    pass


def my_main():
    global real_res
    # my_print("==unit==" * 10)
    # my_unit_test()
    # quit()
    #my_print("==func==" * 10)
    #my_func_test()
    #quit()
    a, b, add = my_input()
    real_res = []
    my_run(a, b, add)
    print(len(real_res))


my_main()
