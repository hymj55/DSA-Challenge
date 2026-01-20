from locale import currency


def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr


def fib_iterative2(n):
    if n <= 1:
        return 1        #fib(0)=1, 이렇게 시작하는 경우

    prev, curr = 0, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr


print(fib_recursive(5))
print(fib_iterative(5))
print(fib_iterative2(5))

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

def fact_iter(n):
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

print(fact(5))
print(fact_iter(5))

#Sorting Algorithm
def bubble_sort_p(arr):
    # TIME: O(n^2) | SPACE: O(1) 이 방식은 선택정렬의 아이디어에 가까움 swap 적음
    n = len(arr)
    for end in range(n-1, 0, -1):
        max_idx = 0
        for j in range(1, end + 1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[end], arr[max_idx] = arr[max_idx], arr[end]
    return arr

print(bubble_sort_p([4,1,9,3,8,2]))

def selection_sort_p(arr):
    # TIME: O(n^2) | SPACE: O(1)
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort_p([4,1,9,3,8,2]))


def insertion_sort_p(arr):
    # TIME: O(n^2) | SPACE: O(1)
    n = len(arr)
    for i in range(1, n):   #starting from index 1 인덱스 0은 이미 "정렬된 부분"이라고 가정하기 때문
        key = arr[i]        #현재 정렬된 부분에 끼워넣고 싶은 값
        j = i - 1           #key의 왼쪽에서부터 비교를 시작할 위치 i -1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort_p([4,1,9,3,8,2]))


def bubble_sort(arr):
    # All cases (Best/average/worst) O(n^2)
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):   #i는 정렬안된 구간의 길이 라고 생각할것
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([4,1,9,3,8,2]))

def bubble_sort_opt(arr):
    # Only Best case(already sorted list) o(n)
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):   #i는 정렬안된 구간의 길이 라고 생각할것
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# def swap_with_variable(arr, index1, index2):
#     temp = arr[index1]
#     arr[index1] = arr[index2]
#     arr[index2] = temp
#
# def swap_with_tuple(arr, index1, index2):
#     arr[index1], arr[index2] = arr[index2], arr[index1]



def selection_sort(arr):
    # Time: o(n^2)
    # Space: o(1)
    n = len(arr)            #n = 5
    for i in range(n-1):    #i = 0,1,2,3
        min_idx = i             #if i = 0
        for j in range(i + 1, n): #j = 1, 2, 3, 4
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr



def quick_sort(arr, start=0, end=None):
    # TIME: O(n^2) worst, O(n log n) average | SPACE: O(1) extra (O(log n) recursion)
    if end is None:
        end = len(arr) - 1      #assgin last index of the array
    if start < end:             #base case = breaking condition
        pivot_idx = place_pivot(arr, start, end)
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)
    return arr

def place_pivot(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    pivot_idx = start
    pivot_val = arr[start]

    for i in range(start + 1, end + 1):
        if arr[i] < pivot_val:
            pivot_idx += 1
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
    arr[start], arr[pivot_idx] = arr[pivot_idx], arr[start]
    return pivot_idx

arr = [4,2,7,11,8,19,3]
print(quick_sort(arr))


