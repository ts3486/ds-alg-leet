class HashTable:
    def __init__(self, size=10):
        self.data = [None] * size 

    def hash(self, key):
        if isinstance(key, str):
        # Convert the string to an integer using a hash function
            hashedKey = hash(key)
        return hashedKey % len(self.data)
        
    def insert(self, key, value):
        hashedKey = self.hash(key)
        self.data[hashedKey] = [key, value]

    def get(self, key):
        hashedKey = self.hash(key)
        if self.data[hashedKey] is not None:
            return self.data[hashedKey][0]
        raise KeyError("Key not found")

    def remove(self, key):
        hashedKey = self.hash(key)
        if self.data[hashedKey] is not None:
            # self.data.pop(hashedKey)
            self.data[hashedKey] = None
        raise KeyError("Key not found")
    
hash_table = HashTable()

hash_table.insert("key1", "John")
hash_table.insert("key2", "John")

print(hash_table.get("key1"))
print(hash_table.get("key2"))
