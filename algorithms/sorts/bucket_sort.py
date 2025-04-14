def bucket_sort(arr):
    """
    Bucket Sort Algorithm
    - Divides the input array into buckets, sorts each bucket, and then combines them.
    """
    if len(arr) == 0:
        return arr  # Return if the array is empty

    # Step 1: Create buckets
    # Find the maximum and minimum values in the array to determine the range
    min_value = min(arr)
    max_value = max(arr)
    bucket_count = len(arr)  # Number of buckets (can be adjusted)
    bucket_range = (max_value - min_value) / bucket_count  # Range of each bucket

    # Initialize empty buckets
    buckets = [[] for _ in range(bucket_count)]

    # Step 2: Distribute elements into buckets
    for num in arr:
        # Calculate the appropriate bucket index for each element
        bucket_index = int((num - min_value) / bucket_range)
        if bucket_index == bucket_count:  # Handle edge case for max_value
            bucket_index -= 1
        buckets[bucket_index].append(num)

    # Step 3: Sort each bucket
    for i in range(bucket_count):
        buckets[i].sort()  # Use any sorting algorithm (e.g., insertion sort)

    # Step 4: Concatenate all buckets into a single sorted array
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


# Example usage
array = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_array = bucket_sort(array)
print("Original array:", array)
print("Sorted array:", sorted_array)