class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def push(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.length += 1

        print(self.top.data)

        return self
    
    def pop(self):
        if self.top is None:
            return
        self.top = self.top.next
        self.length -= 1

        return self
    
    def peek(self):
        return self.top

class ArrayStack:
    def __init__(self):
        self.array = []
        
    def push(self,value):
        self.array.append(value)
        print(self.array)
        return self.array
    
    def pop(self):
        self.array.pop()
        print(self.array)
        return self.array
    
    def peek(self):
        print(self.array[-1])
        return self.array[-1]
    

stack = ArrayStack()
stack.push("1")
stack.push("2")
stack.push("3")
stack.peek()
stack.pop()
stack.peek()

#Stacks
#lookup O(n)
#pop O(1)
#push O(1)
#peek O(1)

#fast peek, ordered, fast push and pop.
#it improves pefromance by restricting certain operations.


#figure out
#how are stack nodes stored inside a stack class? 