# Singly Linked Lists

# Pop

- Removing a `node` from the end of the Linked List


# Pop Pseudocode

*Attention* : We have to keep in mind, there are lots of `edge cases` to keep into account

- Edge Case 1: 
    - if there are no nodes, return None
- Edge Case 2:
    - If there is only length of 1, meaning we're trying to pop the self.head

*No Edge Cases Left*

- Loop through the list, (with a while loop)
- if we're at the second to the last node,
    - save that `node` to a `temp variable`
    - save `self.tail` to a `pop variable`
    - set self.tail to be that `node`
    - set `None` to self.tail.next
    - decrement self.length
- else: keep moving through linked list
- return `pop variable`