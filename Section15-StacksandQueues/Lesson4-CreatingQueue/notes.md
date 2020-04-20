# Creating a queue using Array Implementation


# Enqueue Pseudocode
- create new node
- *EDGE CASE*
    - if size is 0: first and last is new node
- else:
    - last.next = new node
    - last = new node
- increment by 1
- return size


# Dequeue Pseudoode
- *EDGE CASE*
    - if size is 0: return None
- *EDGE CASE*
    - if size = 1:
        - create temp var with first
        - last = None
- else:
    - create temp var with first
    - first = first.next
- decrement by 1
- return temp val