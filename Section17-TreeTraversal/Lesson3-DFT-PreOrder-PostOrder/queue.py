class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return self.size

    def dequeue(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            temp = self.first
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
        self.size -= 1
        return temp.value


# q = Queue()

# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
            