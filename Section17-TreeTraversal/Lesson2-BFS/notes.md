# BFS - Breadth First Search

# Steps - Iteratively
    - Create a Queue and a variable to store the values of nodes visited
    - Place the root in the queue
    - loop as long as there is anything in the Queue:
        - Dequeue a node from the queue and push the value of the node into the variable that stores the nodes
        - If there is a left prop on the dequeued node, add it to the queue
        - If there is a right prop on the dequeued node, add it to the queue
    - Return the var that stores the value