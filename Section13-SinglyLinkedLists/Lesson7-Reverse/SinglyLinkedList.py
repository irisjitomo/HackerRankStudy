class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
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
        node = self.head
        while node:
            if node == self.tail:
                print('self.tail value: ', node.value)
            node = node.next

    def print_head(self):
        if not self.head:
            print('Empty List')
        else:  
            print('self.head:', self.head.value)

    def push(self, value):
        new_node = Node(value)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = new_node
        return

    def pop(self):
        node = self.head
        if not node:
            return None
        elif self.length == 1:
            popped = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return popped
        while node:
            if node.next == self.tail:
                pop = self.tail.value
                new_tail = node
                self.tail = new_tail
                self.tail.next = None
                self.length -= 1
            node = node.next
        return pop
    
    def shift(self):
        node = self.head
        if not node:
            return None
        node_value = node.value
        self.head = self.head.next
        self.length -= 1
        return node_value
    
    def unshift(self, value):
        new_head = Node(value)
        if not self.head:
            self.head = new_head
            self.tail = self.head
        else:
            new_head.next = self.head
            self.head = new_head
        self.length += 1
        return

    def get(self, index): # This returns the actual node which will be used 
        # with set()
        if index < 0 or index >= self.length:
            return None
        counter = 0
        node = self.head
        if not node:
            return None
        else:
            while node:
                if counter == index:
                    return node
                node = node.next
                counter += 1

    def getValue(self, index): # Returns node value, cannot be used with set()
        if index < 0 or index >= self.length:
            return None
        counter = 0
        node = self.head
        if not node:
            return None
        else:
            while node:
                if counter == index:
                    return node.value
                node = node.next
                counter += 1

    def set(self, value, index):
        foundNode = self.get(index)
        if not foundNode:
            return False
        foundNode.value = value
        return True

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == self.length:
            not not self.push(value)
        elif index == 0:
            not not self.unshift(value)
        else:
            node = self.get(index - 1)
            prev = node
            aft = node.next
            new_node.next = aft
            prev.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.shift()
        elif index == self.length:
            return self.pop()
        else:
            prev = self.get(index - 1)
            deleted = prev.next
            next = prev.next.next
            prev.next = next
            self.length -= 1
            return deleted.value

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



llist = SinglyLinkedList()
'''
Testing push()
'''
llist.push('A')
llist.push(44)
llist.push([1,2,3])
llist.push(110)
llist.push('D')
llist.print_list() 
llist.__len__()
print('------')

'''
Testing insert() and remove()
'''
# llist.insert(2, 'hello')
# llist.remove(3)
# llist.print_list()

'''
Testing shift(), unshift()
'''
# print('shift()', llist.shift())
# llist.unshift(66)
# llist.print_list()

'''
Testing getValue() and set()
'''
# print('getValue()', llist.getValue(2))
# print('set()', llist.set(567, 2))
# print('getValue()', llist.getValue(2))
# llist.print_list()

'''
Testing pop()
'''
# llist.print_head()
# print('pop()', llist.pop())
# print('pop()', llist.pop())
# print('pop()', llist.pop())
# print('pop()',llist.pop())
# print('pop()',llist.pop())
# print('pop()',llist.pop())

'''
Testing reverse()
'''
llist.reverse()
llist.print_list()

llist.__len__()
