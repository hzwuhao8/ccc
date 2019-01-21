import random


# 3x+1


def my_sort(data):
    n = len(data)
    # print(data)
    x = (n - 1) // 3 // 2

    for k in range(x, -1, -1):
        print("k={0},delta={1} , data={2} ".format(k, (3 * k + 1), data))
        delta = 3 * k + 1
        for i in range(1 * delta, n, 3 * k + 1):
            for j in range(i, 0, -(3 * k + 1)):
                if data[j] < data[j - delta]:
                    data[j], data[j - delta] = data[j - delta], data[j]
    print(data)
    return data
    pass


def my_func_test():
    assert my_sort([1, 2, 3]) == [1, 2, 3]
    for i in range(10):
        data = list(range(i * 3))
        data1 = data.copy()
        data2 = data.copy()
        random.shuffle(data1)
        assert my_sort(data1) == data2


my_func_test()
