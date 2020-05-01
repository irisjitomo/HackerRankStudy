class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [] * capacity

    def _hash(self, key):
        return hash(key)

    def _hash_mod(self, key):
        return self._hash(key) % self.capacity


ht = HashTable(10)

print('hash:', ht._hash('hello'))
print('index:', ht._hash_mod('hello'))