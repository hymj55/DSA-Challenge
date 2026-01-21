# Quick Sort (place pivot, then recursively sort both sides)
# TIME: O(n^2) worst, O(n log n) average | SPACE: O(1) extra (O(log n) recursion)
from typing import List

def quick_sort(arr: List[int], start: int = 0, end: int = None) -> List[int]:
    if end is None:
        end = len(arr) - 1
    # create start and end pointers (parameters)
    if start < end:
        # call placePivot helper
        pivot_idx = place_pivot(arr, start, end)
        # recursively call quickSort on both sides of the pivot
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)
    # return modified arr with sorted values
    return arr


def place_pivot(arr: List[int], start: int = 0, end: int = None) -> int:
    if end is None:
        end = len(arr) - 1
    # create pivotIdx = start
    pivot_idx = start
    pivot_val = arr[start]
    # loop from start+1 to end inclusively
    for i in range(start + 1, end + 1):
        # if element's value is less than pivot value:
        if arr[i] < pivot_val:
            pivot_idx += 1
            # swap elements under current i and pivot_idx
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
    # swap elements under start and pivotIdx to put pivot in place
    arr[start], arr[pivot_idx] = arr[pivot_idx], arr[start]
    # return pivotIdx
    return pivot_idx
