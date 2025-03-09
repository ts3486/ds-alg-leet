# insertion sort - Building the final sorted list one item at a time. You take the first unsorted element and insert it into its proper position in the sorted list.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
    return arr

# effective when datasets are very small or nearly sorted