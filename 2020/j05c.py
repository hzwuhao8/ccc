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


def next_layer(x, y, layer):
    op = x * y
    layer = layer + 1
    next_op = []
    for i in range(m):
        for j in range(n):
            if data[i + 1][j + 1] == op:
                if (i + 1, j + 1) not in node_dict:
                    node_dict[(i + 1, j + 1)] = layer
                    next_op.append([i + 1, j + 1, op, layer])
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
    nodes = [[m, n, m * n]]
    while len(nodes) > 0:
        tmp = nodes[:]
        for current in tmp:
            nodes.remove(current)
            res, next_node = run(current[0], current[1], 1)
            if res == "yes":
                return res
            else:
                nodes = nodes + next_node
    return "no"

res1 = main()
print(res1)
