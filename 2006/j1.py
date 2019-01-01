def my_print(x):
    # print(x)
    pass


def my_input():
    res = [0] * 4
    for i in range(4):
        res[i] = int(input())
    return res


my_dic = {0: [461, 431, 420, 0],
          2: [130, 160, 118, 0],
          1: [100, 57, 70, 0],
          3: [167, 266, 75, 0]
          }


def my_run(data):
    tmp = [0] * 4
    for i in range(4):
        tmp[i] = my_dic[i][data[i] - 1]
    my_print(tmp)
    total = sum(tmp)
    my_print(total)
    return total


def my_test():
    assert my_run([2, 1, 3, 4]) == 649


def main():
    data = my_input()
    my_print(data)
    res = my_run(data)
    print("Your total calorie count is {0}.".format(res))
    my_test()


main()
