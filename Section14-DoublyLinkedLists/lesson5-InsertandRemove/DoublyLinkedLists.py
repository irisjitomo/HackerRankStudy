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
        else:
            print('self.tail: ', self.tail.value)
    
    def print_head(self):
        if not self.head:
            print('Empty List')
        print('self.head: ', self.head.value)

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return
        # self.print_list()

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            old_tail = self.tail
            new_tail = self.tail.prev
            self.tail = new_tail
            self.tail.next = None
            old_tail.prev = None #  we need to severe those connections with 
            # old list
            self.length -= 1
        return old_tail.value

    def shift(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            old_head = self.head
            new_head = self.head.next
            self.head = new_head
            self.head.prev = None
            old_head.next = None
        self.length -= 1
        return old_head.value

    def unshift(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return

    def getVal(self, index):
        half = self.length // 2
        if index < 0 or index >= self.length:
            return None
        elif index <= half:
            count = 0
            node = self.head
            while count != index:
                node = node.next
                count += 1
        else:
            count = self.length - 1
            node = self.tail
            while count != index:
                node = node.prev
                count -= 1
        return node.value

    def get(self, index):
        half = self.length // 2
        if index < 0 or index >= self.length:
            return None
        elif index <= half:
            count = 0
            node = self.head
            while count != index:
                node = node.next
                count += 1
        else:
            count = self.length - 1
            node = self.tail
            while count != index:
                node = node.prev
                count -= 1
        return node

    def set(self, value, index):
        foundNode = self.get(index)
        if not foundNode:
            return False
        foundNode.value = value
        return True

    def insert(self, value, index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            not not self.unshift(value)
        elif index == self.length:
            not not self.push(value)
        else:
            prev = self.get(index - 1)
            aft = prev.next
            prev.next = new_node
            new_node.prev = prev
            new_node.next = aft
            aft.prev = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.shift()
        elif index == self.length - 1:
            return self.pop()
        else:
            deletedNode = self.get(index)
            deletedNode.prev.next = deletedNode.next
            deletedNode.next.prev = deletedNode.prev
            deletedNode.next = None
            deletedNode.prev = None
            self.length -= 1
            return deletedNode.value




dll = DoublyLinkedList()

'''
testing push() and pop()
'''
dll.push(3451)
dll.push(123)
dll.push(1456)
dll.push('Hello')
dll.push('How')
dll.push('Are')
dll.push('You')
dll.print_list()
# print('pop(), ', dll.pop())
dll.print_list()
dll.__len__()

# '''
# testing shift() and unshift()
# '''
# print('shift()', dll.shift())
# dll.print_list()
# dll.unshift('Please Work')
# dll.print_list()

# '''
# testing get() and set()
# '''
# print('get()', dll.getVal(1))
# print('set()', dll.set(69, 1))
# dll.print_list()

'''
testing insert() and remove()
'''
dll.insert('last',5)
dll.print_list()
dll.__len__()
print('remove()', dll.remove(6))
dll.print_list()



dll.__len__()