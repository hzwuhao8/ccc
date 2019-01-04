#用了30分钟， 理解题目， 模拟 步骤
#可以理解为 状态 空间的 变化
# p(i)*r(i) ;  是总的 可能在的 走法；
# 对于p ,  如果能找到 r(i) 不存在 p 胜利
# 对于R ,  如果  p(i+1) 不存在，则 R  胜利

#

#数据如何表示？ 用列表？ 用集合？
#用 dict ?
#dict  {a:1,b:2,c:0,d:1}
#然后找出 所有可能的 走法，
#然后寻找对P  必胜的  走法， ；如果 找不到， 则 R 必胜？ 按照 题目 似乎可以这样理解



def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_input():
    pass


def my_run(data):

    pass


def my_unit_test():
    pass


def my_func_test():

    pass


def my_main_test():
    my_print("==unit=="*10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    my_res = my_run(input_data)
    print(my_res)


my_main_test()

quit()

my_main()

