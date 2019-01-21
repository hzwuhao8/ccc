import random


def my_sort(data):
    n = len(data)
    # print(data)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]

    return data
    pass


def my_func_test():
    assert my_sort([1, 2, 3]) == [1, 2, 3]
    for i in range(100):
        data = list(range(i))
        data1 = data.copy()
        data2 = data.copy()
        random.shuffle(data1)
        assert my_sort(data1) == data2


my_func_test()
