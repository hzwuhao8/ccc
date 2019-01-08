def my_print(x):
    print(x)
    pass


def my_func_test():
    assert my_run(40, 39) == 0
    assert my_run(100, 131) == 500
    assert my_run(100, 129) == 270, my_run(100, 129)
    assert my_run(100, 120) == 100, my_run(100, 120)


def my_run(limit, speed):
    res = 0
    delta = speed - limit
    if delta <= 0:
        res = 0
    elif delta <= 20:
        res = 100
    elif delta <= 30:
        res = 270
    else:
        res = 500

    return res


my_func_test()


def my_main():
    print("Enter the speed limit: ", end="")
    limit = int(input())
    print("Enter the recorded speed of the car: ", end="")
    speed = int(input())
    res = my_run(limit, speed)
    if res == 0:
        print("Congratulations, you are within the speed limit")
    else:
        print("You are speeding and your fine is $ {0}".format(res))


my_main()
