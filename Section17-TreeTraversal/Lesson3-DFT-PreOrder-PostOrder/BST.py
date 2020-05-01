import sys
sys.path.append('./stack.py')
sys.path.append('./queue.py')
from queue import Queue
from stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, node):
        if node < self.value:
            if not self.left:
                self.left = BinarySearchTree(node)
            else:
                self.left.insert(node)
        elif node > self.value:
            if not self.right:
                self.right = BinarySearchTree(node)
            else:
                self.right.insert(node) 

    def bfs(self, node):
        data = []
        q = Queue()
        q.enqueue(node)
        while q.size != 0:
            temp = q.dequeue()
            data.append(temp.value)
            if temp.left is not None:
                q.enqueue(temp.left)
            if temp.right is not None:
                q.enqueue(temp.right)
        return data
    
    def dfs(self, node):
        data = []
        s = Stack()
        s.push(node)
        while s.size != 0:
            temp = s.pop()
            data.append(temp.value)
            if temp.left is not None:
                s.push(temp.left)
            if temp.right is not None:
                s.push(temp.right)
        return data

    def dfs_preorder(self, node):
        data = []
        current = node
        def traverse(node):
            data.append(node.value)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
        traverse(current)
        return data

    def dfs_post_order(self, node):
        data = []
        current = node
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            data.append(node.value)
        traverse(current)
        return data

    def dfs_in_order(self, node):
        data = []
        current = node
        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            data.append(node.value)
            if node.right is not None:
                traverse(node.right)
        traverse(current)
        return data

bst = BinarySearchTree(10)
bst.insert(6)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(20)

# Breadth First Search
print('Breadth First Search: ', bst.bfs(bst))

# Depth First Search
print('Depth First Search: ', bst.dfs(bst))

# Depth First Search - Pre Order
print('Depth First Search Pre: ', bst.dfs_preorder(bst))

# Depth First Search - Post Order
print('Depth First Search Post: ', bst.dfs_post_order(bst))

# Depth First Search - In order
print('Depth First Search In Order: ', bst.dfs_in_order(bst))
