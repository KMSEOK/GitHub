#Binary_tree는 각 노드의 자식이 2개이하인 노드
# 리스트 활용시 단점은 Tree가 한쪽으로 치우쳐지면 데이터 낭비 list[None, A, B, None, C, None, None, None, D] 리스트의 많은 빈 공간이 생김
# 
# left_child = list[2xi] 
# right_child = list[2xi+1]
# 부모의 위치 = list[i/2]

from unittest.mock import NonCallableMagicMock


class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def get_data(self):
        return self.data
    def get_left_child(self):
        return self.left_child
        
    def get_right_child(self):
        return self.right_child

    def set_left_child(self, left_child):
        self.left_child =left_child
    def set_right_child(self, right_child):
        self.right_child =right_child 

class Binary_tree:

    def __init__(self):
        self.root = None
        

    def set_root(self, root):
        self.root = root
    def get_root(self):
        return self.root

    def pre_order(self, node):
        if node is not None:
            print(node.get_data(), end =" ")
            self.pre_order(node.get_left_child())
            self.pre_order(node.get_right_child())

    def in_order(self, node):
        if node is not None:
            self.in_order(node.get_left_child())
            print(node.get_data(), end = " ")
            self.in_order(node.get_right_child())

    def post_order(self, node):
        if node is not None:
            self.post_order(node.get_left_child())
            self.post_order(node.get_right_child())
            print(node.get_data(), end = " ")

    def level_order(self, node):
        queue = []
        queue.append(node)
        while queue:
            t = queue.pop(0)
            print(t.get_data(), end = " ")

            if t.get_left_child() is not None:
                queue.append(t.get_left_child())
            if t.get_right_child() is not None:
                queue.append(t.get_right_child())


b_tree = Binary_tree()

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")
node_h = Node("H")

b_tree.set_root(node_a)

node_a.set_left_child(node_b)
node_a.set_right_child(node_c)

node_b.set_left_child(node_d)
node_b.set_right_child(node_e)

node_c.set_right_child(node_f)

node_d.set_right_child(node_g)
node_e.set_left_child(node_h)

b_tree.pre_order(b_tree.get_root())
print("")
b_tree.in_order(b_tree.get_root())
print("")
b_tree.post_order(b_tree.get_root())
print('')
b_tree.level_order(b_tree.get_root())
