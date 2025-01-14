class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # Create a new node with the given value
        self.head = new_node    # Set the head pointer to this new node
        self.tail = new_node    # Set the tail pointer to this new node
        self.length = 1         # Set the length of the list to 1


    def print_list(self):
         temp = self.head  # Start traversal from the head node
         while temp is not None:  # Continue until you reach the end of the list
            print(temp.value)  # Print the value of the current node
            temp = temp.next   # Move to the next node


    def append(self, value): # adding something 
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:   # If the list is empty
         self.head = new_node  # Set the new node as both head and tail
         self.tail = new_node
        else:                   # If the list is not empty
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node       # Update the tail pointer to the new node
        self.length += 1         # Increment the length of the list
        return True              # Return True to indicate success

    
    def pop(self):
        if self.length == 0:    # If the list is empty, return None
          return None
        temp = self.head        # Start traversal from the head
        pre = self.head         # Use `pre` to track the second-to-last node
        while(temp.next):       # Traverse until the last node
          pre = temp          # Update `pre` to the current node
          temp = temp.next    # Move `temp` to the next node
        self.tail = pre         # Update the tail to point to the second-to-last node
        self.tail.next = None   # Disconnect the last node
        self.length -= 1        # Decrease the length
        if self.length == 0:    # If the list becomes empty
         self.head = None    # Reset head and tail
         self.tail = None
        return temp.value       # Return the value of the removed node
    

    def prepend(self, value): #adding something to the start 
       new_node = Node(value)
       if self.length == 0:
          self.head = new_node
          self.tail = new_node
       else:
          new_node.next = self.head
          self.head = new_node
       self.length += 1
       return True
    

       
          


        
my_linked_list = LinkedList(4)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.prepend(6)
my_linked_list.print_list()
# print(my_linked_list.print_list())
# print(my_linked_list.pop())
# print(my_linked_list.print_list())
# print(my_linked_list.prepend())