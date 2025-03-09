# Quick sort - A divide and conquer algorithm that selects a 'pivot' element and partitions the list into two sublists. The left sublist contains elements less than the pivot, while the right sublist contains elements greater than the pivot. It then recursively sorts the sublists.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)