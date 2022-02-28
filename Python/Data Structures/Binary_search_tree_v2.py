# 이진트리 각노드 n의 key값이 n의 왼쪽 Sub-tree 에 있는 노드들의 키 값 보다 큼 
# 각 노드 n의 key값이 n의 오른쪽 서브트리에 있는 노드들의 키 값보다 작음 
from turtle import right


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
    def set_data(self, data):
        self.data = data

class Binary_search_tree:

    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root

    def search(self, data):
        return self.search_node(self.root, data)

    def search_node(self, node, data):
        if node is None:
            return None

        left = node.get_left()
        right = node.get_right()

        if node.get_data() == data:
            return node
        if node.get_data() > data: # 40 > 8
            return self.search_node(left, data)
        else:
            return self.search_node(right, data)

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node # 첫번째 insert노드가 부모 
        else:
            self.insert_node(self.root, node)

    def insert_node(self, parent, node):
        
        if parent.get_data() == node.get_data():
            print(f"{node.get_data()} value already in tree")
        
        else:
            if parent.get_data() > node.get_data():
                left = parent.get_left()
                if left is None:
                    parent.set_left(node)
                else:
                    self.insert_node(left, node)
            elif parent.get_data() < node.get_data():
                right = parent.get_right()
                if right is None:
                    parent.set_right(node)
                else:
                    self.insert_node(right, node)
    
    def print_tree(self):
        if self.root is not None:
            self.print_node(self.root, 0)
        else:
            pass
        
    
    def print_node(self, node, depth):
        msg = ""

        if node is not None:
            for i in range(0, depth):
                msg += "**"
            
            msg += str(node.get_data())
            print(msg)

            self.print_node(node.get_left(), depth + 1)
            self.print_node(node.get_right(), depth + 1)


    def height(self):
        if self.root is not None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self, node, height):
        if node is None:
            return height
        left_height = self._height(node.get_left(), height+1)
        right_height = self._height(node.get_right(), height+1)

        return max(left_height, right_height)


        
        

            

        
    # case1 자식이 없는 노드 삭제  = 그냥 삭제 
    # case2 자식이 1개인 노드 삭제 = 삭제노드의 자식을 삭제노드의 부모한테 붙임
    # case3 자식이 2개인 노드 삭제 = 삭제노드보다 작은 노드의 자식중 가장 큰노드를 대체 
                               # = 삭제노드보다 큰노드의 자식중 가장 작은 노드로 대체

    def delete(self, data):
        self.delete_node(self.root, data)
    
    def delete_node(self, node, data):

        if node.get_data() == data:
            node.set_data(None)
        else:
            if node.get_data() > data: # 40 > 10
                return self.delete_node(node.get_left(), data)
            else:
                return self.delete_node(node.get_rignt(), data)
            


bst = Binary_search_tree()

bst.insert(40)
bst.insert(15)
bst.insert(69)
bst.insert(8)
bst.insert(25)
bst.insert(54)
bst.insert(86)
bst.insert(5)
bst.insert(10)
bst.insert(20)
bst.insert(30)
bst.insert(50)
bst.insert(66)
bst.insert(83)
bst.insert(90)
bst.insert(35)
bst.insert(40)

result = bst.search(66)

if result is None:
    print("fail")
else:
    print("sueccss")

bst.print_tree()

print("tree height :" + str(bst.height()))
