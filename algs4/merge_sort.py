import random


def my_sort(data, layer):
    # print("  " * layer + "{0}".format(data))
    n = len(data)
    mid = n // 2

    d1 = data[:mid]
    d2 = data[mid:]

    # print("  " * layer + "mid={0}, d1={1}, d2={2}".format(mid, d1, d2))
    if mid == 0:
        return data

    if len(d1) > 0:
        d1 = my_sort(d1, layer + 1)
    if len(d2) > 0:
        d2 = my_sort(d2, layer + 1)

    data = merge(d1, d2)
    return data
    pass


def merge(data_a, data_b):
    k, i, j = 0, 0, 0
    data = []
    max_i = len(data_a)
    max_j = len(data_b)
    max_k = max_i + max_j
    for k in range(max_k):
        if i >= max_i:
            data = data + data_b[j:]
            break
        if j >= max_j:
            data = data + data_a[i:]
            break

        if data_a[i] < data_b[j]:
            data.append(data_a[i])
            i = i + 1
        else:
            data.append(data_b[j])
            j = j + 1
    return data


def my_func_test():
    assert merge([3], []) == [3]
    assert merge([2], [3]) == [2, 3]
    assert merge([3], [2]) == [2, 3]

    assert merge([1, 2], [3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge([1, 2, 10, 11], [3, 4, 5, 8, 19]) == [1, 2, 3, 4, 5, 8, 10, 11, 19]
    assert my_sort([1, 2, 3], 0) == [1, 2, 3]
    for i in range(100):
        data = list(range(i))
        data1 = data.copy()
        data2 = data.copy()
        random.shuffle(data1)
        # print(data1)
        # print(my_sort(data1, 0))
        assert my_sort(data1, 0) == data2, "data={0}".format(data)


my_func_test()
