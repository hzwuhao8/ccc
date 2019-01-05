# 需要 使用tree


class Node:
    def __int__(self, action, static_value):
        self.action = action
        self.static_value = static_value

    def __repr__(self):
        return "{0}, {1}".format(self.action, self.static_value)


class Tree:
    def __int__(self, node, layer):
        self.node = node
        self.layer = layer
        self.sub_tree = []

    def add_sub_tree(self, tree):
        self.sub_tree.append(tree)
        tree.layer += 1

    def __repr__(self):

