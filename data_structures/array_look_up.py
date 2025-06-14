# The purpose of this funciton is to find the an elment within an array. 

class ArrayLinearSearchExample:
    def __init__(self, data):
        self.data = data 
        
    def search(self, value):
        # 1. Identify input size: n = number of elements
        n = len(self.data) # constant time operation: 1 = c. 

        # 2. Count work units: one comparison per element
        # 3. Formula: up to n comparisons
        
        # for i in [0,1,2,3,4] 
        for i in range(n):     
            # constant time operation: 1 = c
            if self.data[i] == value:      # one comparison per loop
                return i    
            
            # n * 1 = n comparisons
        
        # 4. Simplify: f(n) = n · 1 → O(n)
        # 5. Result: Time O(n), Space O(1)
        return -1   # constant time operation: 1 = c
    
    # 1. O(1);
    # 2. O(n);
    # 3. O(1);
    
    #  = O(1 + n + 1)
    # => O(n);
    
    # Example usage
data = [10, 20, 30, 40, 50]
search_example = ArrayLinearSearchExample(data)

# Search for an existing value
value_to_find = 30
result = search_example.search(value_to_find)
print(f"Index of {value_to_find}: {result}")  # Output: Index of 30: 2

# Search for a non-existing value
value_to_find = 60
result = search_example.search(value_to_find)
print(f"Index of {value_to_find}: {result}")  # Output: Index of 60: -1