# Character Frequency using Custom HashTable
# Only counts letters (case-sensitive) and all whitespace characters
# Ignores punctuation

class HashTable:
    def __init__(self, size=50):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size  # built-in hash function

    def _set(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        # check if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update value
                return

        # if key does not exist, append
        bucket.append((key, value))

    def _get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

# Function to count character frequency using the custom HashTable
def char_frequency(sentence):
    ht = HashTable()
    for char in sentence:
        if char.isalpha() or char == " ":  # only letters and whitespace
            current_count = ht._get(char)
            if current_count is None:
                ht._set(char, 1)  # first time seeing this char
            else:
                ht._set(char, current_count + 1)  # increment count
    return ht

# Input from user
text = input("Enter a sentence: ")
char_table = char_frequency(text)

# Display the result
print("\nCharacter frequencies:")
for bucket in char_table.table:
    for k, v in bucket:
        print(f"{k}: {v}")

#using dictionary
# Character Frequency using Custom HashTable (with dictionary buckets)
# Only counts letters (case-sensitive) and space (" "), ignores punctuation

class HashTable_Dic:
    def __init__(self, size=50):
        self.size = size
        self.table = [{} for _ in range(self.size)]  # each bucket is a dictionary

    def _hash(self, key):
        return hash(key) % self.size

    def _set(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        bucket[key] = value  # dictionary handles insert/update in O(1) average time

    def _get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        return bucket.get(key)  # returns value or None


# Function to count character frequency using the custom HashTable
def char_frequency(sentence):
    ht = HashTable_Dic()  # default size = 50

    for char in sentence:  # iterate exactly one time
        if char.isalpha() or char == " ":  # only letters and simple space
            current = ht._get(char)
            if current is None:
                ht._set(char, 1)
            else:
                ht._set(char, current + 1)

    return ht


# User Input
text = input("Enter a sentence: ")
result_ht = char_frequency(text)

# Display results
print("\nCharacter frequencies:")
for bucket in result_ht.table:
    for k, v in bucket.items():  # only non-empty buckets will print
        print(f"{k}: {v}")
