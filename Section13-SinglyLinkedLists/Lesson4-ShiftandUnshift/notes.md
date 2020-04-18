# Singly Linked Lists

# Shift
- Remove a new `node` from the beginning of the Linked List

# Main Idea:
- All we're doing is deleting the head
- Then moving head.next to be the new head
- Good idea to save nodes as variables

# Shifting Pseudocode:

- Store current head in variable
- If there are no nodes, return None
- else: save head.value in variable to return later
- set the new head to be head.next
- set current head variable to None
- return head.value variable

# Unshift:
    - Adding a new node at the `beginning` of the Linked List

# Main Idea:
- All we're doing is moving the pointer from the head to the new head
- Good idea to save nodes in a variable
- Make a new head
- Pointer old head to head.next
- Increment length
