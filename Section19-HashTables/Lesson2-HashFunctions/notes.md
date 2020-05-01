# THE HASH PART
    - To implement a hash table we'll be using an array

    - In order to look up values by key, we need a way to `convert keys into valid array indices`.

    - A function that performs this is called a `hash function`

# What makes a good hash?
    - Fast (i.e constant time)
    - Doesn't cluster outputs at specific indices, but distributes uniformly
    - Deterministic (same input yields same output)

# Example:

    def _hash(self, key):
        return hash(key)

- For this function, we just return the hash() of whatever is passed in as the `key`

    def _hash_mod(self, key):
        return self._hash(key) % self.capacity

- For this function, we use the `_hash()` function in order to get our hash, but we `modulo` it with the `capacity` of the hash table SO that we can get our index place in our hash table storage

# This is a more reliable hash function - djb2 hash

    def _hash_djb2(self, s):
        hash = 5381
        for x in s:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

- This is more `reliable` since we get the same hash AND the same index everytime