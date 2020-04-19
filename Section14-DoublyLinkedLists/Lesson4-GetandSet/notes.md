# Doubly Linked Lists

# Get() method
    - accesssing a node in a dll by its position

- Pseudocode:
    - if index <> 0 or >= self.length: return None
    - we need to check if index is closer to 0 or self.length
    - if index <= half of the list:
        - loop through list, starting from head, loop towards middle
        - return the node once found
    - else index > half length of list:
        - loop through list starting from tail, loop towards middle
        - return once node is found

_________________________________________________________________


# Set() method
    - changing the value of a node in an index. Takes in value and index

- Pseudocode:
    -(use get())
    - make a variable with get()
    - if not variable: return False
    - variable.value = value
    - return True