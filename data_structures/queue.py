class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def enqueue(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last = new_node

        self.length += 1

        print(self)

        return self
    
    def dequeue(self):
        if self.first is None:
            raise ValueError("No node to dequeue")
        self.first = self.first.next
        self.length -= 1

        return self
    
    def peek(self):
        print(self.first)
        return self.first

stack = Queue()
stack.enqueue("1")
stack.enqueue("2")
stack.enqueue("3")
stack.peek()
stack.dequeue()
stack.peek()

#Queues
# lookup O(n)
# enqueue O(1)
# dequeue O(1)
# peek O(1)