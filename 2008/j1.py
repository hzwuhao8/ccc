#


def my_print(x, end="\n"):
    # print(x, end=end)
    pass


def my_input():
    weight = float(input())
    height = float(input())
    return weight, height
    pass


def my_run(data):
    w,h = data
    bmi = w/(h*h)
    if bmi > 25:
        return "Overweight"
    elif 18.5 <= bmi <= 25.0:
        return "Normal weight"
    else:
        return "Underweight"
    pass


def my_unit_test():
    pass


def my_func_test():
    assert my_run((69, 1.73)) == "Normal weight"
    assert my_run((84.5, 1.8)) == "Overweight"
    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    my_res = my_run(input_data)
    print(my_res)


my_main_test()

#quit()

my_main()
