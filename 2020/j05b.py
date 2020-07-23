# 从 MN  -> 1,1

m = int(input())
n = int(input())

data = [[]]
for i in range(m):
    d = [int(x) for x in input().split()]
    data.append([0] + d)


mem = dict()

node_dict = dict()




def run(x, y, path):
    if x == 1 and y == 1:
        return "yes", path
    else:
        if (x, y) in node_dict:
            if node_dict[(x, y)] == 1:
                return "no", path
            else:
                node_dict[(x, y)] = 1
        op = x * y
        # print(x, y, path)

        next_op = []
        for i in range(m):
            for j in range(n):
                if data[i + 1][j + 1] == op:
                    next_op.append([i + 1, j + 1, op])
        # print(next_op)
        for op in next_op:
            next_path = path[:]
            next_path.append(op)
            if (op[0], op[1]) not in node_dict:
                node_dict[(op[0], op[1])] = 0
            res, path = run(op[0], op[1], next_path)

            if res == "yes":
                return res, path
            else:
                mem[(op[0], op[1])] = "no"
        mem[(x, y)] = "no"
        return "no", path


res1, path1 = run(m, n, [])
print(res1)
