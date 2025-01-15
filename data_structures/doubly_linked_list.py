class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.prepend(data)
            return
        current_node = self.head
        current_position = 0
        while current_node and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        if not current_node:
            raise IndexError("Position out of bounds")
        new_node.next = current_node.next
        new_node.prev = current_node
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next = new_node

    def lookup(self, data):
        current_node = self.head
        position = 0
        while current_node:
            if current_node.data == data:
                return position
            current_node = current_node.next
            position += 1
        raise ValueError(f"{data} not found in the list")

    def delete_with_value(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node == self.head:
                    self.head = current_node.next
                return
            current_node = current_node.next
        raise ValueError(f"{data} not found in the list")

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.insert(1.5, 2)
dll.print_list()  # Output: 0 1 1.5 2 3
print(dll.lookup(1.5))  # Output: 2
print(dll.lookup(3))  # Output: 4
dll.delete_with_value(1.5)
dll.print_list()  # Output: 0 1 2 3

# single or double linked list
# Singly linked lists are slightly faster than doubly linked lists, but has a disadvantage of not being able to traverse backwards. So if you lose the head node, you may lose the list. Doubly linked lists can be traversed backwards so you can get previous nodes or find nodes from the tail.
#A bit more complex and memory intensive then its single counterpart.