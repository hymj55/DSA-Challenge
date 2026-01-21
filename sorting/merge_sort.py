# Merge Sort (split into halves and merge sorted parts)
# TIME: O(n log n) | SPACE: O(n)
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    # find the middleIdx
    middle = n // 2
    # if middleIdx is 0, return passed arr (0 or 1 element)
    if middle == 0:     # 대신 if n <= 1: 이 조건으로 해도 직관적(배열길이가 1또는 그 이하는 빈배열이니까)
        return arr[:]   # shallow copy, 원본에 영향을 주지않기위해. sort의 경우 리스트안에 int만 있으므로 immutable
    # recursively sort halves
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    # call merge helper to merge two sub-arrays
    return merge(left, right)


def merge(arr1: List[int], arr2: List[int]) -> List[int]:
    # create two pointers for each array
    i, j = 0, 0
    # create arr to be returned
    out: List[int] = []
    # use 3 loops to merge two sorted arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            out.append(arr1[i]); i += 1
        else:
            out.append(arr2[j]); j += 1
    while i < len(arr1):            # i=3, len(arr1)=3 → False, 아무 것도 실행 안 됨
        out.append(arr1[i]); i += 1
    while j < len(arr2):            # j=3, len(arr2)=4 → True, out에 8 추가
        out.append(arr2[j]); j += 1
    # return arr
    return out


# print(merge_sort([4,8,10,3,2,60]))