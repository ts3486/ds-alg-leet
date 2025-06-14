"""
1. Can be divided into two subproblems.
2. Recursive solution.
3. Are there overlapping subproblems?
4. Memoize the subproblems.  
"""

def createMemoizedAddTo80():
    cache = {}  # Cache is now private to the closure
    
    def memoizedAddTo80(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = n + 80
            return cache[n]
    
    return memoizedAddTo80

# Create the memoized function
memoizedAddTo80 = createMemoizedAddTo80()

# Test the function
print(memoizedAddTo80(5))  # First call: calculates and caches
print(memoizedAddTo80(5))  # Second call: returns from cache
print(memoizedAddTo80(6))  # New value: calculates and caches