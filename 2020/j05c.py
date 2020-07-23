# 从 MN  -> 1,1

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


def next_layer(x, y, layer):
    op = x * y
    layer = layer + 1
    if op in data_dict:
        op_list = data_dict.get(op)
    else:
        return list()
    next_op = []
    for op in op_list:
        if (op[0], op[1]) not in node_dict:
            node_dict[(op[0], op[1])] = layer
            next_op.append([op[0], op[1], op, layer])
    return next_op


def run(x, y, layer):
    if x == 1 and y == 1:
        return "yes", []
    next_nodes = next_layer(x, y, layer)
    for op in next_nodes:
        if op[0] == 1 and op[1] == 1:
            return "yes", []
    return "continue", next_nodes


def main():
    # nodes = dict()
    nodes = [[m, n, m * n]]
    layer = 1
    while len(nodes) > 0:
        tmp_node = []
        for current in nodes:
            res, next_node = run(current[0], current[1], layer)
            if res == "yes":
                return res
            else:
                tmp_node = tmp_node + next_node
        layer = layer + 1
        nodes = tmp_node
        print(layer, len(tmp_node))
    return "no"


res1 = main()
print(res1)
