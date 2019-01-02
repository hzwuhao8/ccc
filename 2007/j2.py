#
my_dic={}


def my_print(x, end="\n"):
    # print(x, end=end)
    pass


def my_input():
    data = []
    while True:
        my_str = input()
        if "TTYL" == my_str:
            data.append(my_str)
            break
        else:
            data.append(my_str)
    return data
    pass


def init_data():
    dic_str = """CU
    see you
    :-)
    I’m happy
    :-(
    I’m unhappy
    ;-)
    wink
    :-P
    stick out my tongue
    ( ̃. ̃)
    sleepy
    TA
    totally awesome
    CCC
    Canadian Computing Competition
    CUZ
    because
    TY
    thank-you
    YW
    you’re welcome
    TTYL
    talk to you later
    """
    str_list = dic_str.split("\n")
    my_print("str_list.len={0}".format(len(str_list)))
    dic_a = {}
    for i in range(0, len(str_list) - 1, 2):
        dic_a[str_list[i].strip().upper()] = str_list[i + 1].strip()
    my_print(dic_a)
    return dic_a


def my_run(data):
    res = my_dic.get(data.upper(), data)
    return res
    pass


def my_unit_test():
    pass


def my_func_test():
    assert my_run('CCC') == 'Canadian Computing Competition'
    assert my_run('NOT EXIST') == 'NOT EXIST'
    pass


def my_main():
    global my_dic
    my_dic = init_data()
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()
    input_data = my_input()
    for s in input_data:
        res = my_run(s)
        print(res)



my_main()
