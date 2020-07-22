def h(data):
    t = data[0]
    data[0] = data[1]
    data[1] = t


def v(data):
    t = data[0][0]
    data[0][0] = data[0][1]
    data[0][1] = t
    t = data[1][0]
    data[1][0] = data[1][1]
    data[1][1] = t


def main():
    data = [[1, 2], [3, 4]]
    lines = input()
    count_v = 0
    count_h = 0
    for x in lines:
        if x == "V":
            count_v += 1
        else:
            count_h += 1
    if count_v % 2 == 1:
        v(data)
    if count_h % 2 == 1:
        h(data)

    # for x in lines:
    #     if "V" == x:
    #         v(data)
    #     else:
    #         h(data)
    for x in range(2):
        print(data[x][0], data[x][1])


main()
