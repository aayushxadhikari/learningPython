class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0: # for null items 
            return None
        temp = self.tail
        if self.length == 1: # for 1 item present 
            self.head = None
            self.tail = None
        else:                # for more than 1 items present
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length =-1
        
        return temp




    

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(2)
my_doubly_linked_list.pop()
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()


