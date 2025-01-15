class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_position = 0
        while current_node and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        if not current_node:
            raise IndexError("Position out of bounds")
        new_node.next = current_node.next
        current_node.next = new_node

        #[1,2,3,4]
        #insert(data, 3)
        #nn=data
        #cp = 0, cn=head (1)
        #cp = 1, cn=head.next (2)
        #cp = 2, cn=head.next.next (3)
        #nn.next=4
        #cn.next=data
        #[1,2,3,data,4]

        #[1,2,3,4]
        #insert(data, 5)
        #nn=data
        #cp = 0, cn=head (1)
        #cp = 1, cn=head.next (2)
        #cp = 2, cn=head.next.next (3)
        #cp = 3, cn=head.next.next.next (4)
        #cp = 4, cn=head.next.next.next.next (None)
        #cp = %, cn=head.next.next.next.next.next (None) loop ends here. 
        #cn = None so raises error.

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
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.print_list()  # Output: 0 1 2 3
ll.delete_with_value(2)
ll.print_list()  # Output: 0 1 3

#linked lists
# access - O(n)
# lookup - O(n)
# insertion - O(1)
# deletion - O(1)

# - fast inserts and deletions
# - the advantage of linked lists over arrays is its ordered data + low cost operations and size flexibility.
# - insertion and deletion from the head is very low cost of O(n)
# - however insertion/deletion from the tail because it is costly tp find the second to last node.
