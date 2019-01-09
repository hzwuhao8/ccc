# 计分问题， 如何赢
import copy


def my_print(x, end="\n"):
    #print(x, end=end)
    pass


TEST_DATA_1 = [[1, 3, 7, 5], [3, 4, 0, 8], [2, 4, 2, 2]]
TEST_DATA_2 = [[1, 3, 5, 7], [3, 4, 8, 0], [2, 4, 2, 2], [1, 2, 5, 5]]

base_score_list = [(3, 0), (1, 1), (0, 3)]


def get_score(sa, sb):
    if sa > sb:
        return 3, 0
    elif sa == sb:
        return 1, 1
    else:
        return 0, 3


# 计算 当前的分数
# 保存在一个 成绩字典中
def over_game_score(data):
    dic = {1: 0, 2: 0, 3: 0, 4: 0}

    for a, b, sa, sb in data:
        av, bv = get_score(sa, sb)
        dic[a] = dic[a] + av
        dic[b] = dic[b] + bv
    return dic


all_contest = set([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])


# 已经完成的 比赛的集合
def over_game(data):
    game_set = set()
    for a, b, sa, sb in data:
        if a < b:
            game_set.add((a, b))
        else:
            game_set.add((b, a))
    return game_set


# 还有未进行的比赛， 计算 所有的可能
# 统计所有 赢的比赛场次
#
def future_game(data):
    over_set = over_game(data)
    future_set = all_contest.difference(over_set)
    return future_set


def is_win(dic, team):
    s_list = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
    return s_list[0][0] == team


def my_unit_test():
    data = copy.deepcopy(TEST_DATA_1)
    dic = over_game_score(data)
    my_print(dic)
    assert dic[4] == 4
    assert dic[3] == 0
    over_set = over_game(data)
    my_print("over_set={0}".format(over_set))
    assert len(over_set) == 3
    assert over_set == set([(1, 3), (3, 4), (2, 4)])
    f_set = future_game(data)
    assert len(f_set) == 3
    assert f_set == set([(1, 2), (1, 4), (2, 3)])

    data = copy.deepcopy(TEST_DATA_2)
    dic = over_game_score(data)
    my_print(dic)
    assert dic[1] == 1
    assert dic[2] == 2
    assert dic[3] == 6
    assert dic[4] == 1
    over_set = over_game(data)
    my_print("over_set={0}".format(over_set))
    assert len(over_set) == 4
    assert over_set == set([(1, 3), (3, 4), (2, 4), (1, 2)])

    assert is_win(dic, 3)
    assert not is_win(dic, 4)


def my_func_test():
    data = copy.deepcopy(TEST_DATA_1)
    assert my_run(3, data) == 0

    data = copy.deepcopy(TEST_DATA_2)
    assert my_run(3, data) == 9


# 全排列
#

def my_run_inner(team, score_dic, f_set, res):
    if len(f_set) == 0:
        res.append(score_dic)
        return res
    else:
        tmp_list = list(f_set)
        (a, b) = tmp_list[0]
        new_f_set = set(tmp_list[1:])
        new_score_dic = copy.deepcopy(score_dic)
        for sa, sb in base_score_list:
            av, bv = get_score(sa, sb)
            new_score_dic[a] = new_score_dic[a] + av
            new_score_dic[b] = new_score_dic[b] + bv
            my_run_inner(team, new_score_dic, new_f_set, res)


def my_run(team, data):
    f_set = future_game(data)
    score_dic = over_game_score(data)
    total = 0
    res = []
    my_run_inner(team, score_dic, f_set, res)
    my_print(len(res))
    for x in res:
        if is_win(x, team):
            total += 1
    return total

    pass


my_unit_test()
my_func_test()


def my_main():
    team = int(input())
    total = int(input())
    data = []
    for i in range(total):
        data.append([int(x) for x in input().split()])
    res = my_run(team, data)
    print(res)


my_main()
