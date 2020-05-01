# Function Set() / Get()


# Set Pseuodocode:
    - Accepts key and a val
    - hash the key
    - Stores the key-val pair in a separate chaining manner
        - if there is nothing in index
            - insert item
        - else:
            - push to existing array

# Get Pseudocode:
    - Accepts a key
    - Hash the key
    - go to index and retrieve the value using separate chaining
        - loop through that index
            - return value once found
        - if not return False/None