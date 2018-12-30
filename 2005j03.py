# 序列访问的次序和单词 替换
# 简单的循环
def myprint(x):
    pass
    print(x)


def myinput():
    res = []
    for i in range(100):
        txt = input()
        res.append(txt)
        if "SCHOOL" == txt:
            break
    return res


def myreverse(a_list):
    size = len(a_list)
    assert size % 2 == 0 , f"data error a_list={a_list}"
    ll = list(range(0,size,2))
    ll.reverse()

    res = []
    for i in ll:
        if i == 0:
            name = "into your HOME."
        else:
            name = f"onto {a_list[i - 1]} street."
        action = a_list[i]
        if action == 'R':
            action = "Turn LEFT"
        else:
            action = "Turn RIGHT"
        s = f"{action} {name}"
        res.append(s)

    res_str = "\n".join(res)
    return res_str


def main():
    a_list = myinput()
    res = myreverse( a_list    )
    #myprint(res)
    print(res)


main()

list_a=['R','QUEEN','R','FOURTH','R','SCHOOL']
res_a = """Turn LEFT onto FOURTH street.\nTurn LEFT onto QUEEN street.\nTurn LEFT into your HOME."""
assert myreverse(list_a) == res_a , f"myreverse(list_a)={myreverse(list_a)}"