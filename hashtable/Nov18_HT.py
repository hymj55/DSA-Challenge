#only think about key and no value, not considering collision

class SimpleHashSet:
    def __init__(self, size=10):
        #Create an array of 10
        self.size = size
        self.buckets = [None] * size  #[None, None, None,...,None] 이 형태로 생성됨. key-val이 아닌 only key만 저장하기때문에 가능

    def _get_index (self, key):
        #Implement your magic function(= hash function)
        return hash(key) % self.size

    def add(self, key):
        index = self._get_index(key)
        self.buckets[index] = key
        print(f"I added {key} to bucket index: {index}")
        # 이코드의 핵심 문제: 이미값이 있는 인덱스값이 또 나오게된 경우 기존 값 덮어쓰게(Alice와 Charlie가 같은 해시 인덱스로 충돌가능)

    def contains(self, key):    #key = Alice
        index = self._get_index(key)    #index=1

        #Now check if the item at this index matches our key
        if self.buckets[index] == key: #buckets[1] 에 Alice가 있는지 확인
            return True
        return False

my_set = SimpleHashSet()
my_set.add("Alice")
my_set.add("Bob")


print(f"Is Alice in the set? {my_set.contains("Alice")}")
print(f"Is Alice in the set? {my_set.contains("Bob")}")
print(f"Is Alice in the set? {my_set.contains("Charlie")}")