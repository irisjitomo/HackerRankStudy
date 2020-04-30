class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = root

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value == current.value:
                    return None
                if value < current.value:
                    if current.left == None:
                        current.left = new_node
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right == None:
                        current.right = new_node
                    else:
                        current = current.right

    def find(self, value):
        if this.root == None:
            return False
        current = self.root
        found = False
        while current and not found:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True
        if found == False:
            return False
        return True