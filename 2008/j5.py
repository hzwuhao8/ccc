# 用了30分钟， 理解题目， 模拟 步骤
# 可以理解为 状态 空间的 变化
# p(i)*r(i) ;  是总的 可能在的 走法；
# 对于p ,  如果能找到 r(i) 不存在 p 胜利
# 对于R ,  如果  p(i+1) 不存在，则 R  胜利

#

# 数据如何表示？ 用列表？ 用集合？
# 用 dict ?
# dict  {a:1,b:2,c:0,d:1};  [1,2,0,1] 这样表示也可以
# 然后找出 所有可能的 走法，
# 然后寻找对P  必胜的  走法， ；如果 找不到， 则 R 必胜？ 按照 题目 似乎可以这样理解

R = "Roland"
P = "Patrick"

TEST_DATA = [
    [0, 2, 0, 2],
    [1, 3, 1, 3],
    [1, 5, 0, 3],
    [3, 3, 3, 3],
    [8, 8, 6, 7],
    [8, 8, 8, 8],
]

TEST_RESULT = [R, P, R, R, R, P]


def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_input():
    t = int(input())
    input_data = []
    for i in range(t):
        input_data = [int(x) for x in input().split()]
    return input_data
    pass


# 所有合法的取法
VALID = ((2, 1, 0, 2),
         (1, 1, 1, 1),
         (0, 0, 2, 1),
         (0, 3, 0, 0),
         (1, 0, 0, 1),
         )


def is_exist(v, data):
    # my_print("v={0} data={1}".format(v, data))
    tmp = [data[i] - v[i] >= 0 for i in range(4)]
    return tmp.count(True) == 4


# 得到 所有可能的 取法
def get_all_method(data):
    # my_print("get_all_method({0})".format(data))
    res = []
    for v in VALID:
        if is_exist(v, data):
            res.append(v)
    return set(res)
    pass


# 如何进行 递归？

def find_best(steps, data, path, layer):
    layer_str = " {0} ".format(layer) * layer
    my_print("{0}{1}".format(layer_str, "====" * 5 * (layer + 1)))
    my_print("{0} data={1}".format(layer_str, data))
    my_print("{0} path={1}".format(layer_str, path))
    new_steps = get_all_method(data)
    my_print("{0} new_steps={1}".format(layer_str, new_steps))
    if len(new_steps) == 0:
        my_print("{0} steps={1}".format(layer_str, steps))
        my_print("{0} data={1}".format(layer_str, data))
        steps.append(path)
        return steps
        pass
    else:
        for step in new_steps:
            next_data = [data[i] - step[i] for i in range(4)]
            tmp_list = list(path)
            tmp_list.append(step)
            next_path = tuple(tmp_list)

            find_best(steps, next_data, next_path, layer + 1)


def my_run(data):
    my_print("my_run data={0}".format(data))
    steps = []
    find_best(steps, data, (), 0)
    for p in steps:
        my_print(p)

    if len(steps) % 2 == 1:
        return R
    else:
        return P
    pass


def my_unit_test():
    for v in VALID:
        assert is_exist(v, v)

    assert get_all_method([0, 0, 0, 0]) == set(), get_all_method([0, 0, 0, 0])
    assert get_all_method(TEST_DATA[0]) == set(), get_all_method(TEST_DATA[0])

    assert get_all_method(TEST_DATA[1]) == set([(1, 1, 1, 1), (1, 0, 0, 1), (0, 3, 0, 0)]), get_all_method(TEST_DATA[1])
    pass


def my_func_test():
    for i in range(len(TEST_DATA)):
        assert my_run(TEST_DATA[i]) == TEST_RESULT[i], my_run(TEST_DATA[i])

    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    my_res = my_run(input_data)
    print(my_res)


my_main_test()

quit()

my_main()
