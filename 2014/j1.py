def my_func_test():
    assert my_run([60, 70, 50]) == "Scalene", my_run([60, 70, 50])
    assert my_run([60, 60, 60]) == "Equilateral"
    assert my_run([80, 50, 50]) == "Isosceles", my_run([80, 50, 50])
    assert my_run([60, 75, 55]) == "Error"


def my_run(data):
    if sum(data) != 180:
        return "Error"
    else:
        data = sorted(data)
        # print(data)
        if data[0] == data[1] and data[1] == data[2]:
            return "Equilateral"
        elif data[0] == data[1] or data[1] == data[2]:
            return "Isosceles"
        else:
            return "Scalene"


def my_main():
    data = []
    for i in range(3):
        data.append(int(input()))
    res = my_run(data)
    print(res)


my_func_test()
my_main()
