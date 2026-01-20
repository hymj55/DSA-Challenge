
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        # self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def _set(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

    #Let's check if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) #Updates the existing key
                return

    #If key does not exist
        bucket.append((key, value))

    def _get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

    #Search through the chain/list at the index
        for k,v in bucket:  #same code with for (k,v) in bucket: 괄호생략가능//bucket = [("Alice",1), ("Bob",2)]
            if k == key:
                return v
        return None #Key is not found

# my_hash_t = HashTable()
my_hash_t = HashTable(5) #Lower the size with argument 5 to make collision happened
print(my_hash_t.table)
my_hash_t._set("Alice", 1)
my_hash_t._set("Bob", 2)
my_hash_t._set("Charlie", 3)
my_hash_t._set("David", 4)
my_hash_t._set("Eve", 5)

print(my_hash_t.table)