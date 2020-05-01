class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [] * capacity

    def _hash(self, key):
        return hash(key)

    def _hash_djb2(self, s):
        hash = 5381
        for x in s:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def _hash_mod(self, key):
        return self._hash(key) % self.capacity


ht = HashTable(10)

print('hash:', ht._hash('cyan'))
print('djb2 hash:', ht._hash_djb2('cyan'))
print('index:', ht._hash_mod('cyan'))
