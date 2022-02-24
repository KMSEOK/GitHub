# 이진트리 각노드 n의 key값이 n의 왼쪽 Sub-tree 에 있는 노드들의 키 값 보다 큼 
# 각 노드 n의 key값이 n의 오른쪽 서브트리에 있는 노드들의 키 값보다 작음 

from re import search


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_left(self):
        return self.left
    def get_right(self):
        return self.right

    def get_data(self):
        return self.data

class Binary_search_tree:

    def __init__(self):
        self.root = None
    
    def set_root(self, root):
        self.root = root
    
    def get_root(self):
        return self.root

    def search(self, data):
        return self.search_node(self.root, data)

    def search_node(self, node, data):
        if node is None:
            return None

        left = node.get_left()
        right = node.get_right()
        print(node.get_data())
        if node.get_data() == data:
            return node
        if node.get_data() > data: # 40 > 8
            return self.search_node(left, data)
        else:
            return self.search_node(right, data)

        
        



node_40 = Node(40)
node_15 = Node(15)
node_69 = Node(69)
node_8 = Node(8)
node_25 = Node(25)

node_54 = Node(54)
node_86 = Node(86)
node_5 = Node(5)
node_10 = Node(10)
node_20 = Node(20)
node_30 = Node(30)
node_50 = Node(50)
node_66 = Node(66)
node_83 = Node(83)
node_90 = Node(90)

node_40.set_left(node_15)
node_40.set_right(node_69)

node_15.set_left(node_8)
node_15.set_right(node_25)

node_69.set_left(node_54)
node_69.set_right(node_86)

node_8.set_left(node_5)
node_8.set_right(node_10)

node_25.set_left(node_20)
node_25.set_right(node_20)

node_54.set_left(node_50)
node_54.set_right(node_66)

node_86.set_left(node_83)
node_86.set_right(node_90)

bst = Binary_search_tree()

bst.set_root(node_40)

result = bst.search(8)
if result is None:
    print("fail")
else:
    print("success")

result = bst.search(644)
if result is None:
    print("fail")
else:
    print("success")
