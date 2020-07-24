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

starting_node = (1, 1)
unsearched = deque([starting_node])


def gen_moves(node):
    next_op = []
    op = data[node[0]][node[1]]

    for i in range(m):
        x = i + 1
        if op % x == 0:
            y = op // x
        if y > n:
            continue
        else:
            if (x, y) not in node_set:
                node_set.add((x, y))
                next_op.append((x, y))
    return next_op


def is_goal(node):
    return node[0] == m and node[1] == n




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
