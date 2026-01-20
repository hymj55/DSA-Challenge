class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):      #Add a node at the end
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self


    def pop(self):      #Remove the last node
        if self.length == 0:    #check if it is empty
            return None
        temp = self.head
        pre = temp
        while temp.next:    # temp.next is not None (looping through until temp.next is None)
            pre = temp
            temp = temp.next
        self.tail = pre     # pre is the second to last node, make it tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:    # When the list has only one node, removing it should reset both head and tail to None
            self.head = None
            self.tail = None
        return temp.value

    def unshift(self, value):   #Add a node at the beginning
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def shift(self):  #Remove the first node
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next #if the list had only one node, this sets self.head to None
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None    #That's why we just need to reset tail to None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        node = self.get(index)
        if node:                # if node is not None
            node.value = value
            return True
        return False    # when index is invalid or out of range (node is None)


    def insert(self, index, value):
        if index < 0 or index > self.length: #index can be equal to length (to append at the end)
            return False
        if index == 0:
            return self.unshift(value)
        if index == self.length:
            return self.push(value)
        new_node = Node(value)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length: #For remove, index == length is invalid//because there is no node at that position to remove
            return None
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        removed = prev.next     # We could also do 'removed = self.get(index)', but that would require another O(n) traversal, which is inefficient
        prev.next = removed.next
        removed.next = None
        self.length -= 1
        return removed.value

