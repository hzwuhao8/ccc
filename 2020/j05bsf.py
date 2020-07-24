from collections import deque

m = int(input())
n = int(input())

data = [[]]
for i in range(m):
    d = [int(x) for x in input().split()]
    data.append([0] + d)

mem = dict()

node_dict = dict()
node_set = set()

data_dict = dict()

for i in range(m):
    for j in range(n):
        op = data[i + 1][j + 1]
        if op in data_dict:
            tmp = data_dict[op]
            tmp.append([i + 1, j + 1, op])
            data_dict[op] = tmp
        else:
            tmp = list()
            tmp.append([i + 1, j + 1, op])
            data_dict[op] = tmp

starting_node = (m, n)
unsearched = deque([starting_node])


def gen_moves(node):
    op = node[0] * node[1]
    if op in data_dict:
        op_list = data_dict.get(op)
    else:
        return list()
    next_op = []
    for op in op_list:
        if (op[0], op[1]) not in node_set:
            node_set.add((op[0], op[1]))
            next_op.append((op[0], op[1]))
    return next_op


def is_goal(m):
    return m[0] == 1 and m[1] == 1



def breadth_first_search(unsearched):
    while len(unsearched) > 0:
        node = unsearched.popleft()
        for m in gen_moves(node):
            if is_goal(m):
                return "yes"
            unsearched.append(m)
    return "no"



def main():
    res = breadth_first_search(unsearched)
    print(res)


main()
