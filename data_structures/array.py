class Array:
    def __init__(self):
        self.data = {}
        self.size = 0

    def append(self,value):
        self.data[self.size] = value
        self.size += 1

    def insert(self, index, value):
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.size - 1]
        self.size -= 1

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of range")
    
    def index_of(self, value):
        for index in range(self.count):
            if self.data[index] == value:
                return index
        raise ValueError(f"{value} is not in the array")

    def size(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)
    

#Arrays
#Acess O(1)
#lookup O(n)
#insert O(n)
#delete O(n)

# - Arrays have indexes which make them easy to access directly.
# - When inserting or deleting, you also have to shift the index of each element, which causes O(n).
# - When you lookup by a value (not index), you must taverse the array to find the value. 
# - array data is stored next to eachother in memory as a contiguous block
# - however operations that involve lookups will become O(n) because it has to traverse through the array.
# - Arrays will take up memory for each element it stores.
# - (Arrays use to only have a set amount of memory when defined, however in modern languages storage is dynamically added so you do not have to manually resize on the surface. Resize still occurs in the background)

array = Array()
array.append(1)
array.append(2)
array.append(3)
print(array)
array.insert(1,10)
print(array)
array.remove(1)
print(array)


