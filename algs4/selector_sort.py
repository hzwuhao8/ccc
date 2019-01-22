# 选择 排序
import random


def s_sort(data):
    for i in range(len(data)):
        my_min = data[i]
        index = i
        for j in range(i + 1, len(data)):
            if data[j] < my_min:
                my_min = data[j]
                index = j
        data[i], data[index] = data[index], data[i]

    return data


def my_func_test():
    assert s_sort([1, 2, 3]) == [1, 2, 3]
    for i in range(100):
        data = list(range(i))
        data1 = data.copy()
        data2 = data.copy()
        random.shuffle(data1)
        assert s_sort(data1) == data2


my_func_test()

