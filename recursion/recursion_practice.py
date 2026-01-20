# Problem1:
# Write a recursive function that takes a positive integer n and prints numbers from n down to 1.
# Example:
# Input: 5
# Output: 5 4 3 2 1
print("\ncountDown")
def countDown(n):
    print(n)
    if n == 1:
        return 1
    countDown(n-1)

countDown(5)


# Problem2:
# Write a recursive function that takes a positive integer n and returns the sum of all numbers from 1 to n.
# Example:
# Input: 5
# Output: 15  # 1+2+3+4+5
print("\nsumOfNum")
def sumOfNum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + sumOfNum(n-1)

print(sumOfNum(0))

# Problem3:
# Write a recursive function to calculate the factorial of a given number n.
# Example:
# Input: 4
# Output: 24  # 4*3*2*1
print("\nfactorial")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))

# Problem4:
# Write a recursive function that returns the nth Fibonacci number.
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, …
# Example:
# Input: 6
# Output: 8
print("\nfibonacci")
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

# Problem5:
# Write a recursive function that takes a string and returns the string in reverse order.
# Example:
# Input: "hello"
# Output: "olleh"
print("\nreverseStr")
def reverseStr(str):
    n = len(str)
    if n <= 1:
        return str
    return str[-1] + reverseStr(str[:-1])   # last char + all chars except last
    # str[-1] -> get the last character of the string
    # str[:-1] -> get all characters from the start (index 0) up to but not including the last character
    # slicing syntax: sequence[start(inclusive):stop(exclusive)]
    # if start is omitted, it starts from index 0

# Slicing can be applied to sequence types such as strings, lists, and tuples.
# A sequence is a data type where items are in order and you can access them one by one.
# s = "hello"
# print(s[1:4])  # "ell"

# lst = [10, 20, 30, 40, 50]
# print(lst[1:4])  # [20, 30, 40]

# t = (1, 2, 3, 4, 5)
# print(t[:3])  # (1, 2, 3)

print(reverseStr("hello"))



# Problem6:
# Write a recursive function that counts the number of even numbers in a list of integers.
# Example:
# Input: [1,2,3,4,5,6]
# Output: 3
print("\ncountEvenNums")
def countEvenNums(lst):
    if len(lst) < 1:                # if not lst:   Same result
        return 0
    if lst[-1] % 2 == 0:
        return 1 + countEvenNums(lst[:-1])
    else:
        return countEvenNums(lst[:-1])

# lst = [10, 20, 30, 40, 50]
# print(lst[1:])  # [20, 30, 40, 50]

# lst = [10, 20, 30, 40, 50]
# print(lst[1:-1])  # [20, 30, 40]

print(countEvenNums([1,2,3,4,5,6]))


print("\ncountEvenNums_v2")
def countEvenNums_v2(lst):
    if not lst:    # check if list is empty
        return 0
    if lst[0] % 2 == 0:
        return 1 + countEvenNums_v2(lst[1:])
    else:
        return countEvenNums_v2(lst[1:])

print(countEvenNums_v2([1,2,3,4,5,6]))
