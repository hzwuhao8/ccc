def my_func_test():
    assert my_run(6, 'ABBABB') == 'B'
    assert my_run(6, 'ABBABA') == 'Tie'


def my_run(all, data):
    ta = data.count('A')
    tb = data.count('B')
    if ta > tb:
        return 'A'
    elif ta == tb:
        return "Tie"
    else:
        return 'B'


def my_main():
    all = int(input())
    data = input()
    res = my_run(data)
    print(res)


my_func_test()

my_main()

