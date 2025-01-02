def find_recurring_number(array):
    #input: array with integers. 
    #output: integer that is recurring the most in the array.
    #count how many of the same elemets exists by create a hash table of the elements and their count.

    seen = {}

    for i in array:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1

    # Check if all values in the dictionary are equal
    values = list(seen.values())
    if all(value == values[0] for value in values):
        return None

    # Find the key with the maximum value
    max_key = max(seen, key=seen.get)
    return max_key
    


print(find_recurring_number([2, 5, 1, 2, 3, 5, 1, 2, 4]))