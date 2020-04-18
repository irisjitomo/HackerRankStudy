# Singly Linked Lists

- Get()
    - Retrieving a `node` by its position in the Linked List

- Get() Pseudocode:
    - *Edge Case*
        - If index is less than zero OR greater than or equal to length of the list, return None
    - Make a `counter` to keep track of where we are
    - Once counter == index:
        return node.value