def main():
    (f1, t1) = input().split()
    (f2, t2) = input().split()
    (f3, t3) = input().split()
    (steps_str, f, t) = input().split()
    steps = int(steps_str)
    op_list = []
    rules = [[f1, t1], [f2, t2], [f3, t3]]
    run(f, rules, 0, t, steps, op_list)


#
# 输入 当前字符串， 对 所有位置 进行规则运用
# 返回一个列表
#


def one_step(ff, rule):
    result = []
    s = str(ff)
    f1 = str(rule[0])
    t1 = str(rule[1])
    index = s.find(f1)
    while index >= 0:
        next_index = index + len(f1)
        s1 = s[0:index]
        s2 = s[next_index:]
        tmp_s = s1 + t1 + s2
        result.append([index + 1, tmp_s])
        index = s.find(f1, next_index)

    return result


is_over = False


def run(ff, rules, layer, want, max_steps, op_list):
    # print(ff, layer, op_list)
    if layer == max_steps and ff == want:
        # print("ok")
        for op in op_list:
            print(op[0], op[1], op[2])

        return True
    if layer >= max_steps:
        # print("NOT FOUND")
        return False

    # 进行深度优先 搜索
    layer = layer + 1
    res = False
    for rule_index in range(len(rules)):
        rule = rules[rule_index]
        may_op = one_step(ff, rule)
        for op in may_op:
            op = [rule_index + 1] + op
            next_op_list = op_list[:]
            next_op_list.append(op)
            res = run(op[2], rules, layer, want, max_steps, next_op_list)
            if res:
                break
        if res:
            break
    return res


# print(one_step("AB", ["AA", "AB"]))
# print(one_step("ABAB", ["AB", "BB"]))
# print(one_step("AB", ["B", "AA"]))

rules_a = [["AA", "AB"], ["AB", "BB"], ["B", "AA"]]
ff_a = "AB"
want_a = "AAAB"
max_steps_a = 4
op_list_a = []
# run(ff_a, rules_a, 0, want_a, max_steps_a, op_list_a)

main()
