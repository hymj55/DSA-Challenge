# Exercise 1 - Sum of First N Natural Numbers ###################################################

print("Ex.1-1")
def sum_up(n):
    # Time: O(n)
    # Space: O(1)
    total = 0
    for i in range(1, n+1):
        total += i
    return total

sum_up(10)

print("\nEx.1-2")
def sum_up_math(n):
    # Time: O(1)
    # Space: O(1)
    return n * (n + 1) // 2
    # How to decide, Space Complexity
    # Measure how much extra memory a function uses while running
    # If memory grows with input size n (like arrays, lists, dictionaries), it’s O(n)
    # If it only uses a fixed number of variables or constants, it’s O(1)

sum_up_math(10)

# Exercise 2 - Count Even Numbers ###################################################
print("\nEx.2-1")
def count_even(n):
    # Time: O(n)
    # Space: O(1)
    count = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            count += 1
    return count

count_even(5)

print("\nEx.2-2")
def count_even_formula(n):
    # Time: O(1)
    # Space: O(1)
    return n // 2

count_even_formula(5)

# Exercise 3 - Remove Duplicates from a List ###################################################
print("\nEx.3-1")
def remove_duplicates(arr):
    # Time: O(n^2)
    # Space: O(n)
    new_list = []
    for i in range(len(arr)):
        is_duplicate = False
        for j in range(len(new_list)):
            if arr[i] == new_list[j]:
                is_duplicate = True
                break
        if not is_duplicate:
            new_list.append(arr[i])
    print(new_list)

my_list = [5, 3, 10, 3, 9, 5]
remove_duplicates(my_list)

print("\nEx.3-2")

def remove_duple_set(arr):
    # Time: O(n)
    # Space: O(n)
    new_list = list(set(arr))       # new_list.sort()   if it needs to be sorted before printing
    return new_list
    # For all n elements in the list, each takes O(1) to insert/check in the set → but n repetitions, so, total O(n × 1) = O(n)

result = remove_duple_set(my_list)
print(result)

# Exercise 4 - Search for an Element ###################################################

print("\nEx.4-1")
def linear_search(arr, target):
    # Time: O(n)
    # Space: O(1)   No extra memory required
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Found. Index: {i} value: {arr[i]}")
            return True
    print("Not Found.")
    return False

search_list = [1, 3, 5, 8, 4]
linear_search(search_list, 8)



print("\nEx.4-2")
def binary_search(arr, target):
    # Time: O(log n)
    # Space: O(1)
    arr.sort()
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

result = binary_search(search_list, 99)
print(result)


# Exercise 5 - Find Pair with Given Sum ###################################################

print("\nEx.5-1")
def find_pair(arr, target_sum):
    # Time: O(n^2)
    # Space: O(1)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return True
    return False

arr = [1, 2, 5, 11, 7]
result = find_pair(arr, 99)
print(result)


print("\nEx.5-2")
def find_pair_set(arr, target_sum):
    # Time: O(n)
    # Space: O(n)
    seen = set()
    for value in arr:
        if target_sum - value in seen:  # Since seen is a set, it uses a hash table to look up the value directly → O(1)
            print(value)
            return True
        else:
            seen.add(value)
    return False

result_set = find_pair_set(arr, 12)
print(result_set)

