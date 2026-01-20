class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.first = self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.size += 1
        return self

    def pop(self):
        if self.size == 0:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.size -= 1
        if self.size == 0:
            self.last = None
        return temp.value

    def peek(self):  # MJ
        if self.size == 0:
            return None
        return self.first.value


    def to_string(self):
        current = self.first
        result = ''

        while current is not None:
            result = current.value + result
            current = current.next
        return result

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.size -= 1
        if self.size == 0:
            self.last = None
        return temp.value

    def print_queue(self):
        current = self.first
        while current:
            print(current.value, end=' ')
            current = current.next
        print()


# Exercise 1 - Valid Parentheses (Stack)
# Given a string of brackets ()[]{}, determine if it’s valid: every opener must have a matching closer
# in the correct order.
# Steps:
# 1. Use a stack; push openers.
# 2. On a closer, check the top matches; otherwise invalid.
# 3. Valid if stack is empty at the end.
# Examples:
# ● s="()[]{}" → True
# ● s="(]" → False
# ● s="([{}])" → True

def is_valid(s):
    stack = Stack()

    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.push(char)
        elif char == ')':
            if stack.peek() != '(':
                return False
            stack.pop()
        elif char == ']':
            if stack.peek() != '[':
                return False
            stack.pop()
        elif char == '}':
            if stack.peek() != '{':
                return False
            stack.pop()
        else:
            return False
    return stack.size == 0
    # if stack.size == 0:
    #     return True
    # else:
    #     return False

print("Exercise 1")
print(is_valid("()[]"))
print(is_valid("(]"))
print(is_valid("([{}])"))
print(is_valid("((("))





# Exercise 2 - Undo Typing (Backspace String)
# Given a string where # means “backspace,” return the final text.
# Steps:
# 1. Scan characters left→right.
# 2. If normal char → push. If # → pop if possible.
# 3. Build the final string from stack contents (LIFO → reverse).
# Examples:
# ● "ab#c" → "ac"
# ● "a##" → ""
# ● "abc###" → ""
# ● "xy#z" → "xz"
print("\nExercise 2")
def undo_typing(s):
    stack = Stack()

    for char in s:
        if char == '#':
            stack.pop()
        else:
            stack.push(char)
    return stack.to_string()

print(undo_typing("ab#c"))
print(undo_typing("xy#z"))

# Exercise 3 - Reverse a Queue (using one Stack)
# Reverse all elements of a Queue using a single Stack.
# Steps:
# 1. Dequeue everything, push onto stack.
# 2. Pop everything, enqueue back.
# 3. Queue is reversed.
# Examples:
# ● Queue front→back: 1,2,3,4 → after reverse: 4,3,2,1
print("\nExercise 3")

def reversing_queue(my_queue):
    my_stack = Stack()
    while my_queue.size != 0:
        my_stack.push(my_queue.dequeue())
    while my_stack.size != 0:
        my_queue.enqueue(my_stack.pop())

# Exercise 4 - Rotate Queue by k
# Rotate a queue left by k (move front to back, k times). Handle k ≥ size by modulo.
# Steps:
# 1. If empty → do nothing.
# 2. Repeat k % size times: enqueue(dequeue()).
# Examples:
# ● Queue 1,2,3,4,5, k=2 → 3,4,5,1,2
# ● Queue 10,20,30, k=5 → 30,10,20 (since 5 % 3 = 2)
print("\nExercise 4")

def rotate_queue(queue, k):
    if queue.size == 0:
        return

    k = k % queue.size

    for _ in range(k):
        queue.enqueue(queue.dequeue())


def rotate_queue_2(queue, k):
    if queue.size == 0:
        return

    if k < queue.size:
        for _ in range(k):
            queue.enqueue(queue.dequeue())
    else:
        for _ in range(k % queue.size):
            queue.enqueue(queue.dequeue())


# Exercise 5 - Implement Queue Using Two Stacks
# Implement a FIFO Queue with two LIFO stacks. Support enqueue, dequeue, peek, and empty.
# Steps:
# 1. in_stack for incoming items; out_stack for outgoing.
# 2. On dequeue/peek, if out_stack empty, pour all from in_stack to out_stack.
# 3. Then pop/peek from out_stack.
# Examples:
# ● Ops: enqueue(1), enqueue(2), peek() → 1, dequeue() → 1, empty() → False
print("\nExercise 5")
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        if not self.out_stack:  # if out_stack is empty
            while self.in_stack:    # while in_stack has items, loop through
                self.out_stack.append(self.in_stack.pop())

    def enqueue(self, value):
        self.in_stack.append(value)

    def dequeue(self):
        self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            raise IndexError("Queue is empty")

    def empty(self):    # check if BOTH stacks are empty
        return not self.in_stack and not self.out_stack


q = MyQueue()
q.enqueue(1)
print(q.in_stack, q.out_stack)
q.enqueue(2)
print(q.in_stack, q.out_stack)
print(q.empty())
q.peek()
print(q.in_stack, q.out_stack)
q.dequeue()
print(q.in_stack, q.out_stack)
q.dequeue()
print(q.in_stack, q.out_stack)
print(q.empty())


# my_queue = Queue()
# my_queue.enqueue(10)
# my_queue.enqueue(20)
# my_queue.enqueue(30)
# my_queue.enqueue(40)
# my_queue.enqueue(50)
#
# my_queue.print_queue()
# rotate_queue(my_queue, 3)
# print("after")
# my_queue.print_queue()

# print("\nAfter")
# reversing_queue(my_queue)
# my_queue.print_queue()