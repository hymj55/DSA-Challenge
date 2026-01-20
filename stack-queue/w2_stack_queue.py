from collections import deque #덱 class

cart = []

# cart.append(1)
# cart.append(2)
# cart.append(3)
#
# print(cart)

# List of dictionaries
cart.append({"id":101, "name":"T-shirt", "qty":100})    #key:value pairs    {}: Dictionary, append dictionary to cart list
cart.append({"id":102, "name":"Sneakers", "qty":200})



print(cart[0])
print(cart[1])

# Print the name key of the dictionary at index 1 (the second dictionary)
print(cart[0]["name"])
# print(cart["name"]) 이건 불가능

if cart[0]["name"]== "T-shirt":
    print("true")


for item in cart:
    print(item)


# stack=[]    # LIFO
# stack.append(1)
# stack.append(2)
# print(stack)
# stack.pop() # 2 is out, the latest one
# print(stack)
#

#Queue -   #FIFO

fifo_queue = deque() #  instantiation

print("Add items to it")
fifo_queue.append("Alice")
fifo_queue.append("Bob")
fifo_queue.append("Charlie")

# print(fifo_queue)   #output: deque(['Alice', 'Bob', 'Charlie'])
# fifo_queue = deque()
# print(fifo_queue)   #output: deque([])
#

# fifo_queue.enqueue(10)
# fifo_queue.enqueue(20)
# print(fifo_queue)

fifo_queue.pop()
print(fifo_queue)

fifo_queue.popleft()
print(fifo_queue)


a = [1,2,3]
b=a
b.append(4)
print(a)
print(b)
#output : [1, 2, 3, 4] [1, 2, 3, 4]


# but want to print a = [1,2,3] b = [1,2,3,4]
print("using list()")
a = [1,2,3]
b=list(a)
b.append(4)
print(a)
print(b)



print(".copy")
a = [1,2,3]
b=a.copy()
b.append(4)
print(a)
print(b)





total = 2
new_total = total
total = 5
print(total)
print(new_total)
#output: 5 2

total = 2
new_total = total
new_total = 5
print(total)
print(new_total)
#output: 2 5

#shallow copy vs deep copy


queue = []
queue.append("Alice")   # enqueue
queue.append("Bob")
print(queue)            # ['Alice', 'Bob']

queue.pop(0)            # dequeue (맨 앞 원소 제거)
print(queue)            # ['Bob']



print("use collections and import deque class")
queue = deque()      # create empty queue

queue.append("Alice")    # enqueue
queue.append("Bob")
queue.append("Charlie")

print(queue)  # deque(['Alice', 'Bob', 'Charlie'])

queue.popleft()   # dequeue -> remove 'Alice'
print(queue)      # deque(['Bob', 'Charlie'])

