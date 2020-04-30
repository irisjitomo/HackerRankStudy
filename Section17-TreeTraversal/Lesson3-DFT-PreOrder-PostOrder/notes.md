# DFS - Depth First Search (Pre Order)

# Steps - Recursively
    - Create var to store visited
    - create `Current` var to store root of BST
    - Write helper function which accepts a node
        - Push the value fo the node to the var that stores the values
        - If the node has left propery, call the helper function with the left property on the node
        - If the node has right property, call the helper function with the right propery on the node
    - invoke the helper function with the current variable
    - return array of values


# DFS - Depth First Search (Post Order):

# Steps - Recursively
    - Create var to store visited ndoes
    - store root at a current var
    - helper function that accepts a node:
        - if node.left, call helper function with left propery on node
        - if node.right, call helper function with right property on node
        - push value of node to the store
    - invoke helper function with current var
    - return store array

# DFS - Depth First Search (In Order):

# Steps - Recursively
    - Create var to store visited ndoes
    - store root at a current var
    - helper function that accepts a node:
        - if node.left, call helper function with left propery on node
        - push value of node to the store
        - if node.right, call helper function with right property on node
    - invoke helper function with current var
    - return store array
