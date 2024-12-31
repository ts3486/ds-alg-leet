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

    def size(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)