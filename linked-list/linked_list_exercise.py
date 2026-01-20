"""
Exercise 4: Sorted Singly Linked List
Add a new python file: sorted_linked_list.py.
Create a sorted linked list class that will be able to sort the inserted integer node automatically.
"""

class Node:
    def __init__(self, value:int):
        self.value = value      # Integer value stored in the node
        self.next = None        # Pointer to the next node


# Sorted Linked List (ascending order)
class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, value:int):
        """
        Insert a new node in sorted order (ascending)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        new_node = Node(value)

        #Case 1. If list is empty, new node becomes head and tail
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        #Case 2. If new value is smaller than head, insert at beginning
        elif value < self.head.value:
            new_node.next = self.head
            self.head = new_node

        #Case 3. If new value is bigger than or equal to tail, insert at the end
        elif value >= self.tail.value:
            self.tail.next = new_node
            self.tail = new_node

        #Case 4. insert in the middle/ find correct position
        else:
            current = self.head
            # Move until the next node's value is bigger than the new value
            while current.next is not None and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.length += 1

    def delete(self, value):
        """
        Delete a node with the given value
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Case 1: Empty list
        if self.length == 0:
            return False

        # Case 2: Deleting the head node
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            # If list becomes empty, update tail too
            if self.length == 0:
                self.tail = None
            return True

        # Case 3: Deleting tail
        if self.tail.value == value:
            current = self.head
            # Move until the node before tail
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
            self.length -= 1
            return True

        # Case 4: Delete a node in the middle
        current = self.head
        # Find the node before the one to delete
        while current.next and current.next.value != value:
            current = current.next

        if current.next and current.next.value == value:
            # Skip the node to remove it
            current.next = current.next.next
            self.length -= 1
            return True
        # Value not found
        return False

    def search(self, value:int):
        """
        Search if the value exists in the list
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        # Go through the list until value is found
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        """
        Print all values in the list in sorted order
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        values = []
        current = self.head
        # Collect all values in a list
        while current is not None:
            values.append(current.value)
            current = current.next
        print("Sorted List:", values)


sll = SortedLinkedList()
sll.insert(10)
sll.insert(5)
sll.insert(15)
sll.insert(7)
sll.display() # Output: Sorted List: [5, 7, 10, 15]
#


print(sll.search(10))  # True
print(sll.search(100)) # False


sll.delete(7)
sll.display()

sll.delete(5)  # head
sll.display()

sll.delete(15) # tail
sll.display()  # Output: Sorted List: [10]

sll.delete(100) #
sll.display()   # Output: Sorted List: [10]





