# Merge sort - A divide and conquer algorithm that divides the list into two halves, sorts each half, and then merges the two halves.
# O(n log n) - Time complexity

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result + left[left_index:] + right[right_index:]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

array = [37, 45, 29, 8, 12, 88, -3]
print(merge_sort(array)) # [-3, 8, 12, 29, 37, 45, 88]