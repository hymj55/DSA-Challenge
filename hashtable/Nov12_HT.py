class HashTable:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.bucket = [[] for _ in range(capacity)] # 0 to 10 bucket now

    def get_hash_index(self, key): #string(word, ex.cat) key를 주면 convert to ASCII number -> % 공식 -> 인덱스 반환하기 위한 함수
        hash_sum = hash(key) #c:10 a:20 t:30 , hash_sum = 60
        index = hash_sum % self.capacity #60/10 = 6 doing module and get index
        return index

    def insert(self, key, value): #key ='cat', value = 3
        index = self.get_hash_index(key) # index=5
        bucket = self.bucket[index] #버킷[5]을 버킷에 할당해서 그냥 bucket이라고 부를것임 매번 인덱스바뀔때마다 버킷[7] 버킷[6]하지않으려고


        for i, (existing_key, _) in enumerate(bucket): #searching for existing key on bucket
            if existing_key == key:
                bucket[i] = (key, value) #update the value
                print(f"updated key {key} with value {value} at index {i}")
                return


        #If there is none in the bucket(no collision), just append it
        bucket.append((key,value))
        print(f"Inserted {key} with value {value} into bucket index: {index} {bucket}")

        #If there is collision, using linked list

    def get(self, key): #Gets me the value associated with the key
        index = self.get_hash_index(key)
        bucket = self.bucket[index]

        #Search through the bucket/chains of the bucket
        for (existing_key, value) in bucket:
            if existing_key == key:
                return value
        return None

#for (existing_key, value) in bucket:
# → 각 튜플을 꺼내서 튜플 언패킹(tuple unpacking)
# → 왼쪽 existing_key에는 튜플의 첫 번째 값(key)
# → 왼쪽 value에는 튜플의 두 번째 값(value) 저장

    #Remove functions to be done later

    def display(self):
        print("\n This is my current Hashtable \n")
        for i, bucket in enumerate(self.bucket):
            print(f"Bucket{i}:{bucket}")
            print("------")

if __name__ == '__main__':
    my_hashtable = HashTable(capacity=5)

    print("insert data:")
    my_hashtable.insert("apple",10)
    my_hashtable.insert("banana", 20)
    my_hashtable.insert("cherry",30)

    my_hashtable.display()