m = int(input())
n = int(input())

data = [[]]
for i in range(m):
    d = [int(x) for x in input().split()]
    data.append([0] + d)

mem = dict()


# for d in data:
#     print(d)


def run(x, y, path):
    # print(x, y, path)
    if x == m and y == n:
        return "yes", path
    else:
        if (x, y) in mem:
            return "no", path

        op = data[x][y]
        # print(op, path)
        next_op = []
        for index in range(op):
            x1 = index + 1
            if op % x1 == 0:
                y1 = int(op / x1)
                if x1 == m and y1 == n:
                    path.append([x1, y1, op])
                    return "yes", path
                else:
                    if x1 > m or y1 > n:
                        continue
                    else:
                        next_op.append([x1, y1, op])
            else:
                continue

        # print(next_op)
        for op in next_op:
            next_path = path[:]
            next_path.append(op)
            next_res, pp = run(op[0], op[1], next_path)
            if next_res == "yes":
                return next_res, pp
            else:
                mem[(op[0], op[1])] = "no"
        return "no", path


res, res_path = run(1, 1, []);
print(res)
