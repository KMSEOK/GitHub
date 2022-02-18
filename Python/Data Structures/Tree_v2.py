# 기존 Tree에서 left child, right child 활용

from turtle import right


class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left_child
    def get_right(self):
        return self.right_child
    def set_left_child(self, left):
        self.left_child = left
    def set_right_child(self, right):
        self.right_child = right

class Tree:

    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root
    
    def set_root(self, root):
        self.root = root

    def print_tree(self):
        self.print_node(self.root, 0)
    def print_node(self, node, depth):
        msg = ""
        if node is not None:
            for i in range(0, depth):
                msg += " "
            
            msg += node.get_data()
            print(msg)

            self.print_node(node.get_left(), depth + 1)
            self.print_node(node.get_right(), depth)


        





tree = Tree()

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g= Node("G")
node_h = Node("H")
node_i = Node("I")
node_j = Node("J")
node_k = Node("K")
node_l = Node("L")
node_m = Node("M")
node_n = Node("N")
node_o = Node("O")
node_p = Node("P")

tree.set_root(node_a)

node_a.set_left_child(node_b)

node_b.set_left_child(node_e)
node_b.set_right_child(node_c)

node_e.set_left_child(node_k)
node_e.set_right_child(node_f)

node_k.set_right_child(node_l)

node_f.set_right_child(node_g)

node_g.set_left_child(node_m)

node_c.set_left_child(node_h)
node_c.set_right_child(node_d)

node_h.set_left_child(node_n)
node_h.set_right_child(node_i)

node_d.set_left_child(node_j)

node_j.set_left_child(node_o)

node_o.set_right_child(node_p)

tree.print_tree()
