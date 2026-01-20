def bubble_sort(my_list):   #my_list = [5, 1, 10, 3, 17, 8], len(my_list) = 6
    for i in range(len(my_list)-1, 0, -1):  # i goes from 5 to 1, controls how many elements to check in each pass
        for j in range(i):  # i = 5, j = 0,1,2,3,4 // 0,1 1,2 2,3 3,4 4,5 first pass compares 5 times
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

my_list = [5, 1, 10, 3, 17, 8]

print(bubble_sort(my_list))



def bubble_sort_prof(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swap happened in this pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps happened, the list is sorted
        if not swapped:
            break
    return arr

nums = [5, 2, 9, 1, 5]
sorted_nums = bubble_sort_prof(nums)
print(sorted_nums)