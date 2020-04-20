# Creating a stack

# There is more than one way of implementing a stack


# Easiest way is to use:
    - Aray Implementation


# Push()
- create new node var
- *EDGE CASE*:
    - if no elements, set first and last to be new node
- save first in var
- first = new node
- first.next = var
- increment size
- return size

# Pop()
- *EDGE CASE*
    - if empty, return None
    - if size is 1, first = last = None
- save first in temp var
- first = first.next
- decrement by 1
- return temp.value