# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
# Linked List class
class LinkedList:
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def insert_head(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a new node at the end
    def insert_tail(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while (last.next):
            last = last.next
        
        last.next =  new_node

    # Inserts a new node after the given prev_node
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in LinkedList")
            return
    
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # delete the first occurrence of key in linked list
    def delete_node(self, key):
        temp = self.head
 
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        if(temp == None):
            return
 
        prev.next = temp.next
        temp = None

    # Find x in the linked list
    def search(self, x):
        current = self.head
 
        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False

    # This function counts number of nodes in Linked List
    def get_count(self):
        temp = self.head # Initialise temp
        count = 0 # Initialise count
  
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

    # Print linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print (temp.data),
            temp = temp.next
 
# Initialize LList
llist = LinkedList()

# Insert a few elements at the head
llist.insert_head(7)
llist.insert_head(6)
llist.insert_head(5)
llist.insert_head(4)
llist.insert_head(3)
llist.insert_head(2)
llist.insert_head(1)

# Insert element 99 at the tail
llist.insert_tail(99)

# Insert element 33 after the element 2
llist.insert_after(llist.head.next, 33)

# Delete nodes 1 and 5
llist.delete_node(1)
llist.delete_node(5)


# Print the current list
print("My Linked List:")
llist.print_list()          # [2, 33, 3, 4, 6, 7 99]

# Search for element 3
print("Is 3 in the list?")
if llist.search(3):         # Yes
    print("Yes")
else:
    print("No")

# Search for element 10
print("Is 10 in the list?")
if llist.search(10):        # No
    print("Yes")
else:
    print("No")

# Count
print("The number of nodes in our Linked List is:")  # 7
print(llist.get_count())