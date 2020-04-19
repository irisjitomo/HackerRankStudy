# Doubly Linked List

# Insert Method
    - Adding a node to the Linked List at a `specific` position

*ALL ABOUT CONNECTING POINTERS*
    - new node has to point at next node
    - previous node has to point at new node

# Insert Pseudocode
- *EDGE CASE*:
    - If the index is less than zero or greater than the length, return False
- *EDGE CASE*:
    - If te index is the same as the length, push a new code to the end of the list
    - Maybe use push()

***********************************************

# Remove Method
    - Removing a node at a `specific` position

*ALL ABOUT CONNECTING POINTERS*
    - new node has to point at next node
    - previous node has to point at new node

# Remove Pseudocode
- *Edge Case*:
    - If the index is less than zero or greater than the length, return False
- Use shift() and pop() if index is 0 or self.length
- Use get(index - 1) and save that in a prev variable
- save the next node to a temp variable 
- save the next next node to a `next` varaible
- point prev.next to be te `next` variable
- decrement length
- return temp.value