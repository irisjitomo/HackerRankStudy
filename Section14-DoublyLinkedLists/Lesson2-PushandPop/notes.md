# Doubly Linked Lists

# Pushing
    - adding to the end of the doubly linked lists


Pseudocode:
- if no head and tail, node = head = tail
- Find Tail
- set Tail.next to be that new node
- set new_node.prev to be the old tail
- update self.tail to be new_node
- INcrement Length

# Pop
    - removing from the end of the dll

- make two variables to save old tail and new tail
- self.tail = new tail
- Severing bonds from both .next and .prev
    - self.tail.next = None
    - self.tail.next.prev = None
- decrement by 1