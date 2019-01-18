#
#
# stack ,
# 0 -> pop
# others  -> append
#
#

def my_func_test():
    my_str = """1
3
5
4
0
0
7
0
0
6"""
    data = [int(x.strip()) for x in my_str.split("\n")]
    assert my_run(10, data) == 7


def my_run(n, data):
    my_stack = []
    for x in data:
        if x == 0:
            if my_stack:
                my_stack.pop()
        else:
            my_stack.append(x)
    return sum(my_stack)


my_func_test()


def my_main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(int(input()))
    res = my_run(n, data)
    print(res)


my_main()
