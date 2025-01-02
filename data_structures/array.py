class Array:
    def __init__(self):
        self.data = {}
        self.length = 0

    def insert(self, index, value):
        self.data[index] = value

    def remove(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        raise IndexError("Index out of range")

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