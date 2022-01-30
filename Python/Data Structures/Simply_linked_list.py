# 단점: 데이터양이 많아지면 데이터들이 단선의 링크로 연결되어있음 이러면 검색시 노드 하나 하나를 거쳐서 가므로 시간이 많아 걸림


class Node:

    def __init__(self, fruit):
        self.fruit = fruit
        self.next = None
    
    def get_fruit(self):
        return self.fruit
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

class Simply_linked_list:
    
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

        

    def append(self, fruit):
        new_node =Node(fruit)
        self.size += 1
        if self.header is None:
            self.header = new_node
        
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
    
    def get_at(self, index):
        node = self.header
        if self.size < index:
            return None

        if node is not None:
            for i in range(index):
                node = node.get_next()
        else:
            return None
        return node

    def search(self, fruit):
        node = self.header
        if node is not None:
            for i in range(0,self.size):
                if node.get_fruit() == fruit:
                    return node
                node = node.get_next()
        else:
            return None

    def delete_at(self, index):
        
        front = None
        current = self.header
        if current is not None:
            for i in range(0,index):
                front = current
                current = current.get_next()
            if current == self.header:
                self.header = current.get_next()
            else:
                front.set_next(current.get_next())
            if current == self.tail:
                self.tail = front
            self.size -= 1    
    def print_list(self):

        node = self.header

        while node is not None:
            print(node.get_fruit())
            node = node.get_next()

        print(">>>>>>>>>>>>>")

sll = Simply_linked_list()
sll.append("Apple")
sll.append("Kiwi")
sll.append("Banana")
sll.print_list()
print(">>>>>>>>>>>>>>>")

node = sll.get_at(1)
if node is not None:
    print(node.get_fruit())
else:
    print("index error")

node = sll.get_at(2)
if node is not None:
    print(node.get_fruit())
else:
    print("index error")
print(">>>>>>>>>>>>>>>")

node = sll.search("Banana")
if node is not None:
    print("we hava it")
else:
    print("we dont have it")

node = sll.search("Kimminseok")
if node is not None:
    print("we hava it")
else:
    print("we dont have it")

sll.delete_at(1)
sll.print_list()