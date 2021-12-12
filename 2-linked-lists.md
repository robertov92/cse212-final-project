# Linked Lists

## Introduction

A linked list is a structure of data elements whose order is not determined by their physical placement in memory. Instead, each element points to the next element, and in the case of a double-linked list each element points to the nexts and the previous element.

Each node contains: 

1) data 
2) one or two pointers (links) to the next and previous nodes

A graphical representation of two Linked Lists is shown below 

![image](./linked-list.jpeg)

## Usage

This structure helps us to insert and remove nodes at any position in an efficient way. However, access time for linked lists is linear, meaning, you need to go through each node from the frist one to find the node you are looking for. In the worst case scenario, finding elements in a Linked List takes O(n).

Both stacks and queues are often implemented using linked lists. You can use linked lists to improve the insertion and removal time of a simple array, but most of the time, the access time will be better on an array or a dynamic array than on a liked list.

In the following tutorial, we will learn to implement a simple Linked List. First, we will create two classes. The first class will initialize a Linked List and the second class will initialize nodes for the first one.

## The LinkedList and Node classes

```python
# Linked List class
class LinkedList:
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
```

Notice that we could have made the Node class an inner class, but we will leave it as two separate classes in this example.

Then, we will write functions to perform the most important operations on the Linked List, which are:

1) Insertion
2) Removal
3) Search

Now we will look at the insertion methods.

## Insertion

### To insert at the head of a lined list...

1) Allocate the Node
2) Put in the data
3) Make next of new Node as head
4) Move the head to point to new Node

```python
# This function is in LinkedList class
# Function to insert a new node at the beginning
def insert_head(self, new_data):
 
    # Allocate the Node
    # Put in the data
    new_node = Node(new_data)
         
    # Make next of new Node as head
    new_node.next = self.head
         
    # Move the head to point to new Node
    self.head = new_node
```

Inserting a node at the head takes O(1)

### To insert at the tail of a linked list...

1) Create a new node
2) Put in the data
3) Set next as None
4) If the Linked List is empty, then make the new node as head
5) Else traverse till the last node
6) Change the next of last node

```python
# This function is in LinkedList class
# Function to insert a new node at the end
def insert_tail(self, new_data):
   # Create a new node
   # Put in the data
   # Set next as None
   new_node = Node(new_data)
 
   # If the Linked List is empty, then make the
   # new node as head
   if self.head is None:
        self.head = new_node
        return
 
   # Else traverse till the last node
   last = self.head
   while (last.next):
       last = last.next
 
   # Change the next of last node
   last.next =  new_node
```

Inserting a node at the tail takes O(n) because of the loop

### To insert after a given node...

1) Check if the given prev_node exists
2) Create new node
3) Put in the data
4) Make next of new Node as next of prev_node
5) Make next of prev_node as new_node

```python
# This function is in LinkedList class
# Inserts a new node after the given prev_node
def insert_after(self, prev_node, new_data):
 
    # Check if the given prev_node exists
    if prev_node is None:
        print("The given previous node must in LinkedList")
        return
 
    # Create new node
    # Put in the data
    new_node = Node(new_data)
 
    # Make next of new Node as next of prev_node
    new_node.next = prev_node.next
 
    # Make next of prev_node as new_node
    prev_node.next = new_node
```

Inserting a node at the head takes O(1)

## Removal

### To remove the head of the linked list...

1) Find the previous node of the node to be deleted
2) Change the next of the previous node

```python
# This function is in LinkedList class
# Given a reference to the head of a list and a key,
# delete the first occurrence of key in linked list
def delete_node(self, key):
        
    # Store head node
    temp = self.head

    # If head node itself holds the key to be deleted
    if (temp is not None):
        if (temp.data == key):
            self.head = temp.next
            temp = None
            return

    # Search for the key to be deleted, keep track of the
    # previous node as we need to change 'prev.next'
    while(temp is not None):
        if temp.data == key:
            break
        prev = temp
        temp = temp.next

    # If key was not present in linked list
    if(temp == None):
        return

    # Unlink the node from linked list
    prev.next = temp.next

    temp = None
```

Deleting a node takes O(n)

## Search

The following method helps us know if x data is in our Linked List

```python
# This function is in LinkedList class
def search(self, x): 
    # Initialize current to head
    current = self.head

    # loop till current not equal to None
    while current != None:
        if current.data == x:
            return True # data found
            
        current = current.next
        
    return False # Data not found
```

## Example

Here is the complete implementation of a simple linked list... 

```python
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

    # Print linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print (temp.data),
            temp = temp.next

'''Driver Code'''
# Initialize LinkedList
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
```

## Problem to Solve

Using the simple linked list above, see if you can write a method to count all the elements in the list.

You can check your code with the solution here: [Solution](simple-linked-list.py)

[Back to Welcome Page](0-welcome.md)
