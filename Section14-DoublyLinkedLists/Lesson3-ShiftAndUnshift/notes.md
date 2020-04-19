# Singly Linked List

# Shift
    - Removing from the head

# Shift pseudocode

- if length = 0, return None
- if length = 1, head and tail = None
- else: 
- save head.next in variable new_head
- save head in var old_head
- severe connections with old_head
- return old_head value

_____________________________________

# Unshift 
    - adding a new head

# unshift pseudocode
- new_node var
- if length = 0: self.head = self.tail = new_node
- else:
*pointer manipulation with next and prev*
- old_head = self.head
- self.head = new_node
- self.head.next = old_head
- old_head.prev = self.head
- Increment length