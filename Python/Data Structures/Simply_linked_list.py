

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
        self.size = 0

    def append(self, fruit):
        new_node =Node(fruit)
        self.size += 1
        if self.header is None:
            self.header = new_node
        
        else:
            node = self.header    
            while node.get_next() is not None:
                node = node.get_next()
            node.set_next(new_node)
    
    def print_list(self):

        node = self.header

        while node is not None:
            print(node.get_fruit())
            node = node.get_next()

        print(">>>>>>>>>>>>>")

sll = Simply_linked_list()
sll.append("Apple")
sll.append("Banana")
sll.append("Kiwi")
sll.print_list()
