class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        #traverse(value) to find node to be link new node 
        if self.root == None:
            self.root = Node(value)
        # else 
        
    def lookup(self):
