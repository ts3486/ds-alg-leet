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
        #On average O(1), but worst case O(n) because there could be a key where there is a linnked list and you would have to perform an linked list insertion operation. 

    def get(self, key):
        hashedKey = self.hash(key)
        if self.data[hashedKey] is not None:
            return self.data[hashedKey][0]
        raise KeyError("Key not found")
       #On average O(1), but worst case O(n) because there could be a linked list and you will have to travserse through it. 

    def remove(self, key):
        hashedKey = self.hash(key)
        if self.data[hashedKey] is not None:
            # self.data.pop(hashedKey)
            self.data[hashedKey] = None
        raise KeyError("Key not found")
        #On average O(1), but worst case O(n) because there could be a linked list and you will have to travserse through it.
    
hash_table = HashTable()

hash_table.insert("key1", "John")
hash_table.insert("key2", "John")

print(hash_table.get("key1"))
print(hash_table.get("key2"))

#Hash tables
# Lookup - average case O(1) but worst O(n). This is due to collisions where data is stored in the same address and has a linked list structure. 
# Insertion - average case O(1) but worst O(n)
# Deletion - average case O(1) but worst O(n)
# - hash tables have very fast lookups because there is a key for each value. 
# - hash tables have hash functions that hash the key. Then the hashed key is used as an address for memory.
# - hash tables sometimes have conflicts of memory address since memory address can be already taken when being assigned (understand better)

#figure out
#the process of memmory assignment having conflicts
#why lookups are more diffcult than arrays?
