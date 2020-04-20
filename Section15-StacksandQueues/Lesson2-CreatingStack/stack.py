class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0


    def push(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.first = self.last = new_node
        else:
            current_first = self.first
            self.first = new_node
            self.first.next = current_first
        self.size += 1
        return self.size
    
    def pop(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            temp = self.first
            self.first = self.last = None
        else:
            temp = self.first
            self.first = self.first.next
        self.size -= 1
        return temp.value

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())