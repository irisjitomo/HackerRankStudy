class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0

    def __len__(self):
        print('length: ', self.length)
    
    def print_list(self):
        if not self.head:
            print('Empty List')
        cur_node = self.head
        list = []
        while cur_node:
            list.append(cur_node.value)
            cur_node = cur_node.next
        print(list)

    def print_tail(self):
        if not self.tail:
            print('Empty List')
        print('self.tail: ', self.tail)
    
    def print_head(self):
        if not self.head:
            print('Empty List')
        print('self.head: ', self.head)

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        removed = self.tail
        new_tail = self.tail.prev
        self.tail = new_tail
        self.tail.next = None
        self.tail.prev = None
        self.length -= 1
        return removed.value



dll = DoublyLinkedList()

'''
testing push() and pop()
'''
dll.push(3451)
dll.push(123)
dll.push(1456)
dll.push('Hello')
dll.print_list()
print('pop(), ', dll.pop())
dll.print_list()


dll.__len__()