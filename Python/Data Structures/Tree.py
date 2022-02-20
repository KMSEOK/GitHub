
# fix commit

class Node:

    def __init__(self, data):
        self.data = data
        self.children = []
#       self.size = 0

    def get_data(self):
        return self.data
    def get_children(self):
        return self.children
    def add_children(self, child):
        self.children.append(child)


class Tree:

    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root
    
    def set_root(self, root):
        self.root = root


    def print_tree(self):
        self.print_node(self.root,0)
    
    def print_node(self, node,depth):
        msg = ""
        if node is not None:
            for i in range(0,depth):
                msg += " "
            msg += node.get_data()
            print(msg)

            children = node.get_children()
            for i in range(0,len(children)):
                self.print_node(children[i], depth+1)


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

node_a.add_children(node_b)
node_a.add_children(node_c)
node_a.add_children(node_d)

node_b.add_children(node_e)
node_b.add_children(node_f)
node_b.add_children(node_g)

node_c.add_children(node_h)
node_c.add_children(node_i)

node_d.add_children(node_j)

node_e.add_children(node_k)
node_e.add_children(node_l)

node_g.add_children(node_m)

node_h.add_children(node_n)

node_j.add_children(node_o)
node_j.add_children(node_p)

tree.print_tree()

