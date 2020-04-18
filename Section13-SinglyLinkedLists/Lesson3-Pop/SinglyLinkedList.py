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
        print(self.length)

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    def print_last(self):
        node = self.head
        while node:
            if node == self.tail:
                print('self.tail value: ', node.value)
            node = node.next

    def push(self, value):
        new_node = Node(value)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = self.head
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
            else:
                node = node.next
        return pop


llist = SinglyLinkedList()

llist.push('A')
llist.push('B')
llist.push('C')
llist.push('D')
llist.print_list()

print(llist.pop())
print(llist.pop())
print(llist.pop())
print(llist.pop())
llist.print_list()

llist.__len__()
# llist.print_last()
# print('POPPING')
# print(llist.pop())
# llist.print_last()
# print('----------')
# llist.push(44)
# llist.print_list()
# llist.__len__()