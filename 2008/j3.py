#


def my_print(x, end="\n"):
    # print(x, end=end)
    pass


def my_input():
    input_data = input()
    return input_data
    pass


base_data = [list('ABCDEF'),
             list('GHIJKL'),
             list('MNOPQR'),
             list('STUVWX'),
             list('YZ -.\n'),
             ]


def get_x_y(c):
    for i in range(5):
        for j in range(6):
            if base_data[i][j] == c:
                return (i, j)
            else:
                continue
    print("c={0} ERROR".format(c))


def my_move(f, to):

    (x1, y1) = get_x_y(f)
    (x2, y2) = get_x_y(to)
    steps = abs(x1 - x2) + abs(y1 - y2)
    return steps


def my_run(data):
    total = 0
    f = 'A'
    data_list = list(data)
    data_list.append("\n")
    for t in data_list:
        steps = my_move(f, t)
        my_print("f={0} t={1} steps={2}".format(f, t, steps))
        f = t
        total += steps
    return total
    pass


def my_unit_test():
    assert len(base_data) == 5
    assert len(base_data[2]) == 6
    assert "".join(sum(base_data, [])) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ -.\n"
    assert base_data[3][2] == 'U'
    assert my_move('A', 'A') == 0
    assert my_move('A', 'G') == 1
    assert my_move('G', 'P') == 4
    assert my_move('P', 'S') == 4
    assert my_move('S', '\n') == 6
    pass


def my_func_test():
    assert my_run("GPS") == 15 , my_run("GPS")
    assert my_run("ECHO ROCK") == 29
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
