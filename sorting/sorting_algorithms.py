

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False     #flag, if didn't swap that is False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr [j], arr[j + 1] = arr[j +1], arr[j]
                swapped = True
        if not swapped: #this means all are sorted already
            break

    return arr


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr



def merge_sort(arr):
    #stopping condition
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left_half = merge_sort(arr[:mid]) #index 0 to mid -1
    right_half = merge_sort(arr[mid:]) #mid to end

    return merge(left_half, right_half)

def merge(left_half, right_half):
    return



arr = [5, 3, 8, 4, 2]
# # print(bubble_sort(arr))
# print(selection_sort(arr))





