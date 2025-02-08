class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)

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
                    
    def traverse(self, value):
        current_node = self.root
        while current_node != None:
            print(current_node.value)
            if current_node.value > value:
                    current_node = current_node.left
            else:
                current_node = current_node.right
            
    def lookup(self, value):
        current_node = self.root
        while current_node != None:
            if current_node.value == value:
                return True
            elif current_node.value > value:
                current_node = current_node.left
            elif current_node.value < value:
                current_node = current_node.right
    #Come back to this:
    # def remove(self, value):
    #     current_node = self.root
    #     parent_node = None
    #     # case1 - one node has no child
    #     # case2 - node has child on left side only
    #     # case3 - node has child on right side only
    #     # case4 - node has child on both sides
    #     # case5 - node is root 
    #     # case6 - node is on 3+ level
    #     while current_node != None:
    #         if current_node.value == value:
    #             if current_node.left == None and current_node.right == None:
    #                 current_node = None
    #             elif current_node.left != None and current_node.right == None:
    #                 current_node = current_node.left
    #             elif current_node.left == None and current_node.right != None:
    #                 current_node = current_node.right
    #             elif current_node.left != None and current_node.right != None:
    #                 # find the smallest value on the right side
    #                 # replace the current node with the smallest value
    #                 # remove the smallest value node
    #                 if parent_node.left == current_node:
    #                     parent_node.left = current_node.right
    #                     parent_node.left.left = current_node.left
    #                     current_node = None
    #                 elif parent_node.right == current_node:
    #                     parent_node.right = current_node.right
    #                     parent_node.right.left = current_node.left
    #                     current_node = None                    
    #                 pass
    #         elif current_node.value > value:
    #             parent_node = current_node
    #             current_node = current_node.left
    #         elif current_node.value < value:
    #             parent_node = current_node
    #             current_node = current_node.right
    
tree = BinarySearchTree(30)
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(100)

tree.traverse(170)
print(tree.lookup(4))
print(tree.lookup(170))

#Tree where each node has at most 2 children, and the left child is less than the parent, and the right child is greater than the parent
# Pros:
# Most operations are better than O(n) time
# ordered
# flexible size
# Cons:
# no O(1) operation

#Note: AVL trees and Red-Black trees balance the tree automatically to ensure a O(logN) time complexity