class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
    
    def get_data(self):
        return self.data
    
    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

class Queue:

    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        self.size += 1
        if self.front is None:
            self.front = new_node
        else:
            self.rear.set_prev(new_node)
        self.rear = new_node

    def print_queue(self):
        node = self.front
        while node is not None:
            print(node.get_data())
            node =node.get_prev()

    def dequeue(self):
        node = self.front
        if node is not None:
            self.front = node.get_prev()
            self.size -= 1
        return node



queue = Queue()
queue.enqueue("Apple")
queue.enqueue("Kiwi")
queue.enqueue("Banana")
queue.print_queue()

node = queue.dequeue()
print("Dequeue: " + node.get_data())

node = queue.dequeue()
print("Dequeue: " + node.get_data())

queue.print_queue()