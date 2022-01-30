# 더블 링크드 리스트 노드 끼리 앞,뒤로 연결

from platform import node
from turtle import listen
from urllib.parse import _NetlocResultMixinStr


class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_prev(self, prev):
        self.prev = prev
    
    def get_prev(self):
        return self.prev
    
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next

class Doubly_linked_list:

    def __init__(self):
        self.header =None
        self.tail = None
        self.size = 0

    def print_list(self):
        node = self.header
        if node is not None:
            for i in range(0,self.size):
                print(node.get_data())
                node = node.get_next()
            print('>>>>>>>>>>>>')
        else:
            return None

    def append(self, data):
        new_node = Node(data)
        self.size += 1
        if self.header is None:
            self.header = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)         
        self.tail = new_node
    
    def get_at(self, index):
        node = self.header
        if node is not None:
            for i in range(0,index):
                node = node.get_next()
            return node
        else:
            return None
    def search(self, data):
        node = self.header
        if node is not None:
            for i in range(0, self.size):
                if node.get_data() == data:
                    return node 
                
                node = node.get_next()
        else:
            return None
    
    def get_near_by(self, data, scope): #('Banana', 2) 
        node = self.header
        list = []
    
        if node is not None:
            for i in range(0, self.size):
                if node.get_data() == data:
                    pvnode = node.get_prev()
                    for i in range(0,scope):
                        if node.get_prev() is None:
                            break
                        else:
                            list.append(pvnode)
                            pvnode = pvnode.get_prev()
                    nxnode = node.get_next()
                    for j in range(0,scope):
                        if node.get_next() is None:
                            break
                        else:
                            list.append(nxnode)
                            nxnode = nxnode.get_next()
                    return list
                node = node.get_next()

        else:
            return None
             



dll = Doubly_linked_list()
dll.append('Apple')
dll.append('Kiwi')
dll.append('Banana')
dll.append('Melon')
dll.append('Orange')
dll.append('Blackberry')

dll.print_list()

node = dll.get_at(1)
if node is not None:
    print(node.get_data())
else:
    print("index error")

node=dll.search('Kiwi')
if node is not None:
    print('we have it')
else:
    print('we dont have it')

print(">>>>>>>>>>>")
list = dll.get_near_by('Banana',2)
for node in list:
    print(node.get_data())

list = dll.get_near_by('Apple',3)
for node in list:
    print(node.get_data())

