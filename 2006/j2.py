

def my_print(x):
    print(x)
    pass


def my_input():
    m = int(input())
    n = int(input())
    return [m, n]


def my_run(data):
    [m, n] = data
    # my_print(data)
    total = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i + j == 10:
                # my_print("i={0}, j={1}".format(i, j))
                total = total + 1
    return total
    pass


def my_test():
    assert my_run([6, 8]) == 5, "my_run([6, 8])={0}".format(my_run([6, 8]))
    assert my_run([12, 4]) == 4

    pass


def my_main():
    my_test()
    data = my_input()
    total = my_run(data)
    if total != 1:
        print("There are {0} ways to form the sum 10.".format(total))
    else:
        print("There is {0} way to form the sum 10.".format(total))


my_main()
