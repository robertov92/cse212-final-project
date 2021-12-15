# Node class
class LinkedList:

# Node class
    class Node:

        # Function to initialize the node object
        def __init__(self, data):

            self.data = data
            self.next = None
            self.prev = None

    # Function to initialize the Linked List object
    def __init__(self):

        self.head = None
        self.tail = None

    # Function to insert a new node at the 
    # front or head of the linked list
    def insert_head(self, value):

        new_node = LinkedList.Node(value)  
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node       
    
    # Return a string representation of the linked list.
    def __str__(self):
        
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
    
    # Iterate foward through the Linked List
    def __iter__(self):
        
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    # Solution: Method to check if the Linked List contains a given value
    def contains(self, value):
        
        curr = self.head
        while curr is not None:
            if curr.data == value:
                return True
            curr = curr.next
        
        return False


linked_list = LinkedList()
linked_list.insert_head(1)
linked_list.insert_head(2)
linked_list.insert_head(3)
linked_list.insert_head(4)
linked_list.insert_head(5)
print(linked_list) # linkedlist[4, 3, 2, 1]

print(linked_list.contains(1))  # True
print(linked_list.contains(4))  # True
print(linked_list.contains(2))  # True
print(linked_list.contains(0))  # False
print(linked_list.contains(15)) # False