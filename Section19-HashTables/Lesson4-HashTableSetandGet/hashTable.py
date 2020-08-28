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
        ht = []
        for i in self.storage:
            if i is not None:
                ht.append((i.key,i.value))
            ht.append('None')
        print(ht)

    def _hash(self, key):
        return hash(key)

    def _hash_djb2(self, s):
        hash = 5381
        for x in s:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def _hash_mod(self, key):
        return self._hash(key) % self.capacity

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

    def remove(self, key):
        index = self._hash_mod(key)
        current = self.storage[index]
        if current.key == key:
            self.storage[index] = current.next
        if current.key != key:
            while current.next is not None:
                next = current.next
                if next.key == key:
                    current.next = next.next
            print('key not found')

    def retrieve(self, key): # with linked list
        index = self._hash_mod(key)
        current = self.storage[index]
        if current is not None:
            while current:
                if key == current.key:
                    return current.value
                elif current.next is not None:
                    current = current.next
        else:
            return None

    def keys(self):
        keys = []
        if len(self.storage) == 0:
            return None
        for i in self.storage:
            if i is not None:
                keys.append(i.key)
        return keys
    
    def values(self):
        values = []
        if len(self.storage) == 0:
            return None
        for i in self.storage:
            if i is not None:
                values.append(i.value)
        return values



ht = HashTable(10)

ht.insert('line_1', 'Tiny hash table')
ht.insert('line_2', 'Filled Beyond Capacity')
ht.insert('line_3', 'Array saves the day')


print(ht.retrieve("line_1"))
print(ht.retrieve("line_2"))
print(ht.retrieve("line_3"))

ht.print()
ht.remove('line_11')
ht.print()

# print(ht.keys())
# print(ht.values())
