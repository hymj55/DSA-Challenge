# Problem:
# Calculate the sum of the first n natural numbers. Implement both approaches and analyze time/space complexity for each solution.
# 1. First approach: a. Use a loop to add numbers from 1 to n.
# 2. Second approach (optimized): a. Use the mathematical formula n * (n + 1) // 2.

def sum_up_1(n):
    """
    Time complexity: Big O of n,  1 + 1 + n + 2n + 2n + 1 = O(5n + 3) = O(n)
    Space complexity: Big O of 1
    """
    total = 0       # 1 assignment
    i = 1           # 1 assignment
    while i <= n:   # n comparisons
        total += i  # n additions + n assignments = 2n
        i += 1      # n additions + n assignments = 2n
    print(total)    # 1 print operation

sum_up_1(5)

def sum_up_2(n):
    """
    Time complexity: Big O of 1,   O(1)
    Space complexity: Big O of 1     O(1)  THINK OF 1. how many times we store / 2. Do we ever use an array or not
    """
    return n * (n + 1) // 2  # 3 operations      / is float division(always returns float!!), // is floor division(returns int!!)

result2= sum_up_2(5)
print(result2)


# Exercise 2 - Count Even Numbers
# Problem:
# Count how many numbers from 1 to n are even. Implement both approaches and analyze time/space complexity for each solution.
# 1. First approach: a. Loop through every number from 1 to n, check i % 2 == 0, and increment a counter.
# 2. Second approach (optimized): a. Use math directly: half the numbers from 1 to n are even → n // 2.

def count_even_num_1(n):
    """
    Time complexity: Big O of n,    1 + n + 2n + 1 = 3n + 2 = O(n)
    Space complexity: Big O of 1
    """
    count = 0                   # 1 assignment
    for i in range(1, n+1):     # n iterations
        if i % 2 == 0:
            count += 1          # n additions + n assignments = 2n
    print(f"The number of even numbers: {count}")   # 1 print operation

count_even_num_1(10)

print("The number of even numbers with formula:")
def count_even_num_2(n):
    """
    Time complexity: Big O of 1,  1 = O(1)
    Space complexity: Big O of 1
    """
    return n // 2   # 1 division operation

count_even_num_2(10)


# Exercise 3 - Remove Duplicates from a List
# Problem:
# Remove all duplicate values from a list, preserving only unique elements.
# Implement both approaches and analyze time/space complexity for each solution.
# ● First approach: Use a nested loop: For each element, check if it already exists in a result list before appending.
# ● Second approach (optimized): Use a set to collect unique values.

def remove_duplicates():
    """
    Time complexity: Big O of n,    1 + 1 + n + n + 1 = O(2n + 3) = O(n)
    Space complexity: Big O of n
    """
    num_list = [10, 5, 8, 5, 11, 10, 9]    # 1 assignment,  n = len(num_lists)
    unique_list = []                       # 1 assignment
    for value in num_list:                 # n iterations
        if value not in unique_list:       # n comparisons
            unique_list.append(value)
    print(unique_list)                     # 1 print operation

remove_duplicates()


def remove_duplicates_nested():
    """
    Time complexity: Big O of n squared,    1 + 1 + ( n * n ) + 7 + 1 = O(n^2)
    Space complexity: Big O of n
    """
    num_list = [10, 5, 8, 5, 11, 10, 9]    # 1 assignment, n = len(num_lists)
    unique_list = []                       # 1 assignment
    for i in range(len(num_list)):         # n iterations
        is_duplicate = False

        for j in range(len(unique_list)):  # n iterations
            if num_list[i] == unique_list[j]: # n comparisons
                is_duplicate = True
                break

        if not is_duplicate:                # 7 iterations
            unique_list.append(num_list[i])
    print(unique_list)                     # 1 print operation

remove_duplicates_nested()

def remove_duplicates_set():
    """
    Time complexity: Big O of 1,     O(1)?? O(n)
    Space complexity: Big O of n
    """
    num_list = [10, 5, 8, 5, 11, 10, 9]    # 1 assignment, n = len(num_lists)
    unique_set = set()                      # 1 assignment
    for value in num_list:                 # n iterations
        unique_set.add(value)               # a set automatically does not allow duplicates/If it is already present, it ignores it.
    print(unique_set)

    unique_list = list(unique_set)
    print(unique_list)

remove_duplicates_set()

# Exercise 4 - Search for an Element
# Problem: Check if a given number exists in a list.
# Implement both approaches and analyze time/space complexity for each solution.
# ● First approach: Use a linear search (scan the list one by one).
# ● Second approach (optimized): If the list is sorted, use binary search to reduce the number of checks.

def linear_search(number_list, target):
    """
    Time complexity: Big O of n
    Space complexity: Big O of 1    we only use variables. i and target
    """
    for i in range(len(number_list)):               # n iterations and "check elements one by one!!" O(n)
        if number_list[i] == target:                # n comparisons
            print(f"Found. Index of the list: {i}")
            return
    print("Not found.")

print("Linear Search")
number_list = [2, 5, 12, 35, 49, 22, 56]
linear_search(number_list, 12)


def binary_search(number_list, target):
    """
    Time complexity: Big O of log n,    1 + 1 + log n  = O(log n + 2) = O(log n)
    Space complexity: Big O of 1
    """
    number_list.sort()
    left = 0                                # 1 assignment
    right = len(number_list)-1              # 1 assignment

    while left <= right:                    # n iterations but when we see mid and "cut the problem in half each step!!"  O(log n)!!
        mid = (left + right) // 2
        if number_list[mid] == target:
            return mid
        elif number_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print("Binary Search")
number_list = [2, 5, 12, 35, 49, 22, 56]
print(binary_search(number_list, 12))



# Exercise 5 - Find Pair with Given Sum
# Problem: Given a list of integers and a target sum, determine if there exists a pair of numbers in the list that adds up to the target.
# Implement both approaches and analyze time/space complexity for each solution.
# ● First approach: Use nested loops to check every possible pair.
# ● Second approach (optimized): Use a set to store numbers as you iterate, checking if target - current is already seen.

def find_pair(int_list, target_sum):
    """
    Time complexity: Big O of n squared,   n * n = O(n^2)
    Space complexity: Big O of 1    only use i , j variables. target_sum is parameter
    """
    for i in range(len(int_list)):                  # n iterations(outer loop)
        for j in range(i+1, len(int_list)):         # n iterations(inner loop)
            if int_list[i] + int_list[j] == target_sum:
                print(f"i:{i}, j:{j}, values: {int_list[i]}, {int_list[j]}, target_sum: {target_sum}")
                return
    print("Find_pair: Not found.")





