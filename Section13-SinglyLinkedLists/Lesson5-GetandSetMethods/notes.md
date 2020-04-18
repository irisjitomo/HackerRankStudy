# Singly Linked Lists

- Get()
    - Retrieving a `node` by its position in the Linked List

- Get() Pseudocode:
    - *Edge Case*
        - If index is less than zero OR greater than or equal to length of the list, return None
    - Make a `counter` to keep track of where we are
    - Once counter == index:
        return node.value


************************************************

- Set()
    - Changing the `value` of a node baqsed on it's position in the Linked Lis

- Set() Pseudocode:
    - Function should accept a value and an index
    - Use your `get()` function to find the specific node.
    - If the node is not found, return false
    - If the node is found, set the value of that node to be the value passed to the function and return True
    