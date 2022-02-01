#노트북 작성 
# First in First out
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        self.size += 1
        if self.top is None:
            self.top = new_node

        else:
            new_node.set_next(self.top)
        self.top = new_node

    def pop(self):
        node = self.top
        if node is not None:
            prev = node.get_next()
            self.top = prev
            self.size -= 1
        return node
            
    def get_size(self):
        return self.size

    def print_stack(self):
        node = self.top
        while node is not None:
            print(node.get_data())
            node = node.get_next()



stack = Stack()
stack.push("Apple")
stack.push("Kiwi")
stack.push("Banana")
stack.print_stack()

while True:
    node = stack.pop()
    if node is None:
        break
    else:
        print(f'pop: {node.get_data()}')
stack.print_stack()

print(stack.get_size())