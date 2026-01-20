class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    def unshift(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return self

    def shift(self):
        if self.length == 0:
            return None
        temp = self.head          #Save node before deletion for return even if there's only one node here
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:    #Check if index is in the first half -> search from head, else search from tail.
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:                           #When index is in the last(second) half -> search from tail
            temp = self.tail
            for _ in range(self.length - 1, index, -1): #range(start/inclusive,stop/exclusive,step)
                temp = temp.prev
        return temp

    def set(self, index, value):    #code looks same but get method is differently for DLL,
        node = self.get(index)      #so we have that efficiency.
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.unshift(value)
        if index == self.length:
            return self.push(value)     # index == self.length!!!
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node       #this part is the only difference compared to SLL
        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.shift()
        if index == self.length - 1:    #index == self.length - 1!!!
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = temp.prev = None
        self.length -= 1
        return temp.value

    # prev = self.get(index - 1)
    # removed = prev.next
    # prev.next = removed.next
    # removed.next = None