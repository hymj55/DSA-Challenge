def countdown (n):
    if n == 0:
        print ("Done")
    else:
        countdown(n - 1)
        print(n)

# countdown(5)

def sum_number (n):
    if n == 0:
        return 0

    return n + sum_number(n - 1)

print("sum_num",sum_number(5))


#Implement a factorial function using Recurision eg 5! = 120
#0! =1
#1! = 1

def factorial (n):
    if n == 1 or n == 0:
        return 1

    return n * factorial (n - 1)

print("fact",factorial(3))



#Fibonanci series:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

# F(n) = F(n-1) + F(n-2)

# N == 9 INPUT then above should be output
# Sum = 88;

def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print("fib",fibonacci(9))


def fib_sum(n):
    #Time: O(2^n)
    if n < 0:
        return 0
    total = 0
    for i in range(n+1):
        total = total + fibonacci(i)
    return total

print("fib_sum", fib_sum(9))

def fib_sum(n):
    # Time: O(n)
    if n < 0:
        return 0
    total = 0
    a, b = 0, 1
    for _ in range(n+1):
        total += a
        a, b = b, a + b
    return total


total =0
for i in range(10):
    print(fibonacci(i), end=" ")
    total = total + fibonacci(i)

print ("sum of numbers is:,", total)