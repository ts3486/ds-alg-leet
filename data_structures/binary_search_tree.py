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

        current_node = self.root
        new_node = Node(value)
        while True:
            if current_node.value > value:
                if current_node.left == None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left
            elif current_node.value < value:
                if current_node.right == None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
                    
    def traverse(self):
        current_node = self.root
        while current_node != None:
            print(current_node.value)
            if current_node.left != None:
                current_node = current_node.left
            elif current_node.right != None:
                current_node = current_node.right
            else:
                break
            
    def lookup(self, value):
        current_node = self.root
        while current_node != None:
            if current_node.value == value:
                return True
            elif current_node.value > value:
                current_node = current_node.left
            elif current_node.value < value:
                current_node = current_node.right
        
    def remove(self, value):
        current_node = self.root
        parent_node = None
        while current_node != None:
            if current_node.value == value:
                if current_node.left == None and current_node.right == None:
                    if parent_node.left == current_node:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                elif current_node.left == None:
                    if parent_node.left == current_node:
                        parent_node.left = current_node.right
                    else:
                        parent_node.right = current_node.right
                elif current_node.right == None:
                    if parent_node.left == current_node:
                        parent_node.left = current_node.left
                    else:
                        parent_node.right = current_node.left
                else:
                    #find the smallest value in right subtree
                    smallest = current_node.right
                    while smallest.left != None:
                        smallest = smallest.left
                    current_node.value = smallest.value
                    #remove the smallest value in right subtree
                    self.remove(smallest.value)
            elif current_node.value > value:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.value < value:
                parent_node = current_node
                current_node = current_node.right
