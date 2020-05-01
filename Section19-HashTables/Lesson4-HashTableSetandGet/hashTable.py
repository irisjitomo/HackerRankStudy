class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def print(self):
        print(self.storage)

    def _hash(self, key):
        return hash(key)

    def _hash_djb2(self, s):
        hash = 5381
        for x in s:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def _hash_mod(self, key):
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value): # with linked list
        index = self._hash_mod(key)
        ht = self.storage
        if ht[index] is not None:
            new_pair = LinkedPair(key, value)
            new_pair.next = ht[index]
            ht[index] = new_pair
        else:
            ht[index] = LinkedPair(key, value)
        return


    
    def retrieve(self, key): # with linked list
        index = self._hash_mod(key)
        while self.storage[index]:
            if key == self.storage[index].key:
                return self.storage[index].value
            return None
        
    # def insert(self, key, value): # without linked list
    #     index = self._hash_mod(key)
    #     ht = self.storage
    #     if ht[index] is None:
    #         ht[index] = []
    #     ht[index].append((key, value))
    #     return
    

    # def retrieve(self, key): # without linked list
    #     index = self._hash_mod(key)
    #     ht = self.storage
    #     if ht[index] is not None:
    #         for i in ht[index]:
    #             if key == i[0]:
    #                 return i[1]
    #     return None


ht = HashTable(10)

ht.insert('line_1', 'Tiny hash table')
ht.insert('line_2', 'Filled Beyond Capacity')
ht.insert('line_3', 'Array saves the day')

# ht.print()

print(ht.retrieve("line_1"))
print(ht.retrieve("line_2"))
print(ht.retrieve("line_3"))

