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


llist = SinglyLinkedList()

llist.push('A')
llist.push('B')
llist.print_list()
llist.__len__()
# print(llist)