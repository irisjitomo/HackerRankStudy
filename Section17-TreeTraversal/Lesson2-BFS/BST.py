import sys
sys.path.append('./queue.py')
from queue import Queue


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

    def bft(self, node):
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

bst = BinarySearchTree(10)
bst.insert(6)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(20)
print(bst.bft(bst))

