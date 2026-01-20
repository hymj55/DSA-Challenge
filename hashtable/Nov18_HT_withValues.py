#Store a key-value pair

class SimpleHashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * size

    def _get_index(self, key):
        #This is my hash function or magic function
        return hash(key) % self.size

    def put(self, key, value):
        #Get the index
        index = self._get_index(key)
        self.buckets[index] = (key, value) #Tuple로 key-value 저장
        print(f"Inserted {key} with value {value} into bucket index: {index}")

    def get(self, key):
        index = self._get_index(key)
        stored_data = self.buckets[index]

        #Check if the data actually exists
        if stored_data is not None:
            return stored_data
        else:
            return None

my_map = SimpleHashMap()
my_map.put("Alice",1)
my_map.put("Bob",2)

employee_id = my_map.get("Alice")
print(f"Employee ID of Alice is: {employee_id}")
print(f"Employee ID of Alice is: {employee_id[0]}") #To get only key or a value, use index for tuple



