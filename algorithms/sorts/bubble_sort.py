# Bubble sort - Comparing the first two elements of the list and swapping them if they are in the wrong order. You loop unti the list is sorted.

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

array = [37, 45, 29, 8, 12, 88, -3]
bubble_sort(array)
print(array) # [-3, 8, 12, 29, 37, 45, 88]

#This is o(n^2) time complexity on average. If the list is already sorted, it will be O(n) time complexity.