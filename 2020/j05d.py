import sys
input = sys.stdin.readline

# 从 MN  -> 1,1
# 从  1,1 -> MN
# 从二个方向 进行， 当  MN -> 1,1  新节点的量达到 5000 就暂停，从 另一个方向进行搜索
# 到 另一个方向 扩展得到的节点在    已经在  set_e2s 中， 则  搜索结束， 存在路径， 否则继续
#
m = int(input())
n = int(input())

data = [[]]
for i in range(m):
    d = [int(x) for x in input().split()]
    data.append([0] + d)

mem = dict()

node_set_e2s = set()
node_set_s2e = set()

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


def next_layer_e2s(x, y, layer):
    op = x * y
    layer = layer + 1
    if op in data_dict:
        op_list = data_dict.get(op)
    else:
        return list()
    next_op = []
    for op in op_list:
        if (op[0], op[1]) not in node_set_e2s:
            node_set_e2s.add((op[0], op[1]))
            next_op.append([op[0], op[1], op, layer])
    return next_op


def run_e2s(x, y, layer):
    if x == 1 and y == 1:
        return "yes", []
    next_nodes = next_layer_e2s(x, y, layer)
    for op in next_nodes:
        if op[0] == 1 and op[1] == 1:
            return "yes", []
    return "continue", next_nodes


def next_layer_s2e(x, y, layer):
    next_op = []
    op = data[x][y]

    for i in range(m):
        x = i + 1
        if op % x == 0:
            y = op // x
        if y > n:
            continue
        else:
            if (x, y) not in node_set_s2e:
                node_set_s2e.add((x, y))
                next_op.append([x, y])
    return next_op


def run_s2e(x, y, layer):
    if x == m and y == n:
        return "yes", []
    next_nodes = next_layer_s2e(x, y, layer)
    for op in next_nodes:
        if op[0] == m and op[1] == n:
            return "yes", []
        if (op[0], op[1]) in node_set_e2s:
            return "yes", []
    return "continue", next_nodes


def main():
    # nodes = dict()
    nodes_e2s = [[m, n, m * n]]
    layer_e2s = 1
    while len(nodes_e2s) > 0:
        tmp_node = []
        for current in nodes_e2s:
            res, next_node = run_e2s(current[0], current[1], layer_e2s)
            if res == "yes":
                return res
            else:
                tmp_node.extend(next_node)

        layer_e2s = layer_e2s + 1
        nodes_e2s = tmp_node
        # print(layer_e2s, len(tmp_node))
        if len(nodes_e2s) > 5000 or layer_e2s > 1000:
            break
    # print("node_set_e2s" , len(node_set_e2s))
    if len(nodes_e2s) == 0:
        return "no"

    # print("s2e")
    nodes_s2e = [[1, 1]]
    layer_s2e = 1
    while len(nodes_s2e) > 0:
        tmp_node = []
        for current in nodes_s2e:
            res, next_node = run_s2e(current[0], current[1], layer_s2e)
            if res == "yes":
                return res
            else:
                tmp_node.extend(next_node)

        layer_s2e = layer_s2e + 1
        nodes_s2e = tmp_node
        # print(layer_s2e, len(tmp_node))
        if len(nodes_s2e) > 5000:
            break

    return "no"


res1 = main()
print(res1)
