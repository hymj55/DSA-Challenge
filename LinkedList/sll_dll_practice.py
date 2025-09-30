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

    def print_list(self):
        current_node = self.head
        if current_node is None:
            print("List is empty")
            return

        while current_node is not None:
            print(current_node.value, end = " -> ")
            current_node = current_node.next
        print("None")

class Node_dll:
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
        new_node = Node_dll(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def print_list(self):
        current_node = self.head
        if current_node is None:
            print("List is empty")
            return

        while current_node is not None:
            print(current_node.value, end = " -> ")
            current_node = current_node.next
        print("None")

# Exercise 1 - Reverse a Singly Linked List
# Write a function reverse_sll(lst: SinglyLinkedList) -> None that reverses the list in place.
# Update head, tail, and all next pointers.
# Steps:
# 1. Walk with three pointers: prev, curr, next_temp.
# 2. Flip curr.next = prev.
# 3. Advance until curr is None.
# 4. Swap head/tail.
# Examples:
# ● Input: 1 → 2 → 3 → 4 → After: 4 → 3 → 2 → 1
# ● Input: [] → After: []
def reverse_sll(lst: SinglyLinkedList) -> None:   #the parameter lst has to be a SinglyLinkedList object
    if lst.length == 0:                             #and the function does not return anything 'type hint'
        return

    prev = None
    curr = lst.head
    lst.tail = lst.head

    while curr is not None:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    lst.head = prev


# Exercise 2 - Reverse a Doubly Linked List
# Write a function reverse_dll(lst: DoublyLinkedList) -> None that reverses the doubly linked list
# in place by swapping each node’s prev/next. Update head and tail.
# Steps:
# 1. Traverse nodes; for each node, swap node.prev and node.next.
# 2. After traversal, swap head and tail.
# Examples:
# ● Input: A ⇄ B ⇄ C ⇄ D → After: D ⇄ C ⇄ B ⇄ A
# ● Input: [] → After: []

def reverse_dll(lst: DoublyLinkedList) -> None:
    if lst.head is None:
        return

    curr = lst.head

    while curr is not None:
        curr.prev, curr.next = curr.next, curr.prev
        curr = curr.prev
    lst.head, lst.tail = lst.tail, lst.head

def remove_kth_from_end(lst: SinglyLinkedList, k: int) -> bool:
    if k <= 0 or k > lst.length:    # check if k is invalid then, return
        return False

    if lst.length == 0:             # check if it is empty list then, return
        return False

    if k == lst.length:             # if k == length of the list,
        if lst.length == 1:         # if there is only one node in the list
            lst.head = None
            lst.tail = None
        else:                       # remove head (same as shift function)
            temp = lst.head
            lst.head = lst.head.next
            temp.next = None
        lst.length -= 1
        return True

    fast = lst.head
    slow = lst.head

    for _ in range(k):  # if k=2, iterate from 0 to 1
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    node_to_remove = slow.next
    slow.next = node_to_remove.next     #same as 'slow.next = slow.next.next'

    if node_to_remove == lst.tail:
        lst.tail = slow

    lst.length -= 1
    return True

# Exercise 4 - “Loop Detective” (Cycle Detection, SLL)
# Write has_cycle(lst: SinglyLinkedList) -> bool using Floyd’s Tortoise & Hare algorithm to
# detect if the list has a cycle.
# Steps:
# 1. Two pointers: slow = slow.next, fast = fast.next.next.
# 2. If they meet → cycle. If fast/fast.next becomes None → no cycle.
# Examples:
# ● 1 → 2 → 3 → 4 → 5 (no cycle) → False
# ● 1 → 2 → 3 → 4 → 5 ↘
# ↖────── (cycle back to 3) → True
def has_cycle(lst: SinglyLinkedList) -> bool:
    if lst.head is None or lst.head.next is None:   #if list is empty or has only one node, no cycle
        return False

    slow = lst.head
    fast = lst.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


# Exercise 5 - “Merge Lanes” (Merge Two Sorted SLLs)
# Given two sorted SinglyLinkedLists a and b, write merge_sorted_sll(a, b) ->
# SinglyLinkedList that merges them in place (relinks existing nodes) into one sorted list. The
# original lists should end up unusable (their nodes are moved).
# Steps:
# 1. Use a dummy head and tail pointer.
# 2. Stitch nodes by comparing a.head.value vs b.head.value.
# 3. Append any remaining nodes.
# 4. Compute new length, set head/tail.
# Examples:
# ● a: 1 → 3 → 7, b: 2 → 2 → 9 → merged: 1 → 2 → 2 → 3 → 7 → 9
# ● a: [], b: 5 → 6 → merged: 5 → 6
def merge_sorted_sll(a:SinglyLinkedList,b:SinglyLinkedList)->SinglyLinkedList:
    if a.length == 0 and b.length == 0:
        return a

    if b.length == 0:
        return a

    if a.length == 0:
        a.head = b.head
        a.tail = b.tail
        a.length = b.length
        b.head = b.tail = None
        b.length = 0
        return a

    dummy = Node(None)
    tail = dummy

    curr_a = a.head
    curr_b = b.head

    while curr_a is not None and curr_b is not None:
        if curr_a.value <= curr_b.value:
            tail.next = curr_a
            curr_a = curr_a.next
        else:
            tail.next = curr_b
            curr_b = curr_b.next
        tail = tail.next

    if curr_a is not None:
        tail.next = curr_a
    elif curr_b is not None:
        tail.next = curr_b

    a.head = dummy.next

    current = a.head
    length = 0
    while current is not None:
        length += 1
        if current.next is None:
            a.tail = current
        current = current.next
    a.length = length

    b.head = b.tail = None
    b.length = 0

    return a



print("Exercise 1")
my_sll = SinglyLinkedList()
my_sll.push(1)
my_sll.push(2)
my_sll.push(3)
my_sll.push(4)
my_sll.print_list()

reverse_sll(my_sll)
my_sll.print_list()



print("\nExercise 2")
my_dll = DoublyLinkedList()
my_dll.push("A")
my_dll.push("B")
my_dll.push("C")
my_dll.push("D")
my_dll.print_list()

reverse_dll(my_dll)
my_dll.print_list()



print("\nExercise 3")
kth_test = SinglyLinkedList()
kth_test.push(10)
kth_test.push(20)
kth_test.push(30)
kth_test.push(40)
kth_test.push(50)
kth_test.print_list()
remove_kth_from_end(kth_test, 2)
kth_test.print_list()



print("\nExercise 4")
cycle_test_sll = SinglyLinkedList()
cycle_test_sll.push(1)
cycle_test_sll.push(2)
cycle_test_sll.push(3)
cycle_test_sll.push(4)
cycle_test_sll.push(5)
cycle_test_sll.print_list()
print(f"before adding cycle, Has cycle: {has_cycle(cycle_test_sll)}")

cycle_test_sll.tail.next = cycle_test_sll.head.next.next
print(f"after adding cycle, Has cycle: {has_cycle(cycle_test_sll)}")


print("\nExercise 5")
a = SinglyLinkedList()
a.push(1)
a.push(3)
a.push(7)
a.print_list()
b = SinglyLinkedList()
b.push(2)
b.push(2)
b.push(9)
b.print_list()

merged = merge_sorted_sll(a,b)
merged.print_list()

print("\nExercise 5_ emptylist test")
a = SinglyLinkedList()
a.print_list()
b = SinglyLinkedList()
b.push(2)
b.push(2)
b.push(9)
b.print_list()

merged = merge_sorted_sll(a,b)
print("\nafter merged")
merged.print_list()





