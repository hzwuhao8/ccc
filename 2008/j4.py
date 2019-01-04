#


class Tree():
    def __init__(self, op="", left="", right=""):
        self.op = op
        self.left = left
        self.right = right

    def add_left(self, op, left, right):
        sub_tree = Tree(op, left, right)
        self.left = sub_tree

    def add_right(self, op, left, right):
        sub_tree = Tree(op, left, right)
        self.right = sub_tree

    def __str__(self):
        return prefix_str(self)


def prefix_str(tree):
    if tree.op == "":
        return tree.left
    elif type(tree.left) == type("s") and tree.left.isdigit() and type(tree.right) == type(
            "s") and tree.right.isdigit():
        return tree.op + " " + tree.left + " " + tree.right
    elif type(tree.left) == type("s") and tree.left.isdigit():
        return tree.op + " " + tree.left + " " + prefix_str(tree.right)
    elif type(tree.right) == type("s") and tree.right.isdigit():
        return tree.op + " " + prefix_str(tree.left) + " " + tree.right
    else:
        return tree.op + " " + prefix_str(tree.left) + " " + prefix_str(tree.right)


def postfix_str(tree):
    if tree.op == "":
        return tree.left
    elif isinstance(tree.left, type("s")) and isinstance(tree.right, type("s")):
        return tree.left + " " + tree.right + " " + tree.op
    elif isinstance(tree.left, type("s")):
        return tree.left + " " + postfix_str(tree.right) + " " + tree.op
    elif isinstance(tree.right, type("s")):
        return postfix_str(tree.left) + " " + tree.right + " " + tree.op
    else:
        return postfix_str(tree.left) + " " + postfix_str(tree.right) + " " + tree.op


def my_print(x, end="\n"):
    print(x, end=end)
    pass


def my_input():
    input_data = []
    while True:
        s = input().strip()
        if "0" == s:
            break
        else:
            input_data.append(s)
    return input_data
    pass


def to_tree(data, layer=0):
    tree = None
    my_print("    " * layer + "data={0}".format(data))
    if len(data) == 0:

        pass
    elif len(data) == 1:
        tree = Tree("", data[0], "")
    elif len(data) == 3:
        tree = Tree(data[0], data[1], data[2])
    else:
        index = 0
        for i in range(1, len(data)):
            c = data[i]
            if c.isdigit():
                index = i
                break
            else:
                continue
        my_print("    " * layer + "index={0}".format(index))
        if index == 0:
            print("    " * layer + "ERROR data_str={0}".format(data))
        op = data[0]
        left_str = data[1:index + 1]
        right_str = data[index + 1:]
        tree = Tree(op, to_tree(left_str, layer=layer + 1), to_tree(right_str, layer=layer + 1))
        pass
    return tree


def to_tree_stack(data):
    stack_a = []
    my_print(data)
    for c in data:
        my_print(stack_a)
        if c.isdigit() and len(stack_a) >= 2:
            c1 = stack_a[-1]
            c2 = stack_a[-2]
            my_print("c={2} c1 ={0} c2 ={1}".format(c1, c2, c))
            if isinstance(c1, Tree) or c1.isdigit():
                if c2 == "+" or c2 == "-":
                    c1 = stack_a.pop()
                    c2 = stack_a.pop()
                    my_print("c={2} c1 ={0} c2 ={1}".format(c1, c2, c))
                    t1 = Tree(c2, c1, c)
                    my_print("t1={0}".format(t1))
                    if len(stack_a) >= 2:
                        c1 = stack_a[-1]
                        c2 = stack_a[-2]
                        if isinstance(c1, Tree) or c1.isdigit():
                            c1 = stack_a.pop()
                            c2 = stack_a.pop()
                            t2 = Tree(c2, c1, t1)
                            stack_a.append(t2)
                        else:
                            stack_a.append(t1)
                    else:
                        stack_a.append(t1)
                else:
                    stack_a.append(c)
            else:
                stack_a.append(c)
        else:
            stack_a.append(c)
    my_print("stack_a={0}".format(stack_a))
    if len(stack_a) == 1:
        if isinstance(stack_a[0], Tree):
            return stack_a[0]
        else:
            return Tree("", stack_a[0], "")
    elif len(stack_a) == 3:
        return Tree(stack_a[0], stack_a[1], stack_a[2],)


def my_run(data_str):
    tree = to_tree_stack(data_str.split())

    res_str = postfix_str(tree)
    return res_str


def my_unit_test():
    t = Tree("+", "1", "2")
    assert prefix_str(Tree("", "1", "")) == "1"
    assert prefix_str(t) == "+ 1 2"
    assert postfix_str(t) == "1 2 +"
    t2 = Tree("-", "4", "3")
    t3 = Tree("+", t, t2)
    assert prefix_str(t3) == "+ + 1 2 - 4 3", prefix_str(t3)
    assert postfix_str(t3) == "1 2 + 4 3 - +", postfix_str(t3)
    pass


def my_func_test():
    assert my_run("1") == "1"
    assert my_run("+ 1 2") == "1 2 +"
    assert my_run("- 2 2") == "2 2 -"
    my_print("=x=x=" * 20)
    assert my_run("+ 2 - 2 1") == "2 2 1 - +"
    my_print("=x=x=" * 20)
    assert my_run("- - 3 + 2 1 9") == "3 2 1 + - 9 -"
    assert my_run("+ + + 9 8 7 6") == "9 8 + 7 + 6 +"
    assert my_run("+ 1 + + 2 3 - 4 5") == "1 2 3 + 4 5 - + +"
    pass


def my_main_test():
    my_print("==unit==" * 10)
    my_unit_test()
    my_print("==func==" * 10)
    my_func_test()


def my_main():
    input_data = my_input()
    for s in input_data:
        my_res = my_run(s)
        print(my_res)


my_main_test()

#quit()

my_main()
