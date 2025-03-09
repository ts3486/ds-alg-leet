# Selection sort - Finding the smallest element in the list then swapping it with the first element. You loop through the list and repeat the process.

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr