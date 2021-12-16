# Linked Lists

## Introduction

A linked list is a structure of data elements whose order is not determined by their physical placement in memory. Instead, each element points to the next element, and in the case of a double-linked list, each element points to the nexts and the previous element.

Each node contains: 

1) Data 
2) One or two pointers (links) to the next and previous nodes

A graphical representation of two Linked Lists is shown below 

![image](./linked-list.jpeg)

## Usage

Both stacks and queues are often implemented using linked lists. You can use linked lists to improve the insertion and removal time of a simple array, but most of the time, the access time will be better on an array than on a liked list.

Depending on the operations you will be performing more often in your application, you can use a single array or a linked list. Here is a table that can help you decide what data structure you should use.

| Operation   | Dynamic Array  | Linked List |
| ----------- | ---------------| ------------|
| Insert Front  | O(n) | O(1) |
| Insert Middle | O(n) | O(n) |
| Insert End    | O(1) | O(1) |
| Remove Front  | O(n) | O(1) |
| Remove Middle | O(n) | O(n) |
| Remove End    | O(1) | O(1) |

In the following tutorial, we will learn to implement a Double Linked List. First, we will create two classes. The first class will initialize a Linked List and the second class will initialize nodes for the LinkedList class.

## The LinkedList and Node classes

```python
# Linked List class
class LinkedList:

    # Node class
    # Here Node is an inner class, but this isn't necessary
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
```

Then, we will write functions to perform the most important operations on the Linked List, which are:

1) Insertion
2) Removal

## Insertion

### To insert at the head of a linked list...

1) Create a new node (we will call it new_node)
2) Set the "next" of the new node to the current head (new_node.next = self.head)
3) Set the "prev" of the current head to the new node (self.head.prev = new_node)
4) Set the head equal to the new node (self.head = new_node)

```python
# This function is in the LinkedList class
# Function to insert a new node at the 
# front or head of the linked list
def insert_head(self, value)

    # Create the new node
    new_node = LinkedList.Node(value)  
    
    # If the list is empty, then point both head and tail
    # to the new node.
    if self.head is None:
        self.head = new_node
        self.tail = new_node

    # If the list is not empty, then only self.head will be
    # affected.
    else:
        new_node.next = self.head # Connect new node to the previous head
        self.head.prev = new_node # Connect the previous head to the new node
        self.head = new_node      # Update the head to point to the new node
```

Inserting a node at the head takes O(1)

### To insert at the tail of a linked list...

1) Create a new node (we will call it new_node)
2) Set the "prev" of the new node to the current tail (new_node.prev = self.tail)
3) Set the "next" of the current tail to the new node (self.tail.next = new_node)
4) Set the tail equal to the new node (self.tail = new_node)

```python
# This function is in LinkedList class
# Function to insert a new node at the
# end of tail of the Linked List
def insert_tail(self, value):

    # Create the new node
    new_node = LinkedList.Node(value)  
    
    # If the list is empty, then point both head and tail
    # to the new node.
    if self.tail is None:
        self.head = new_node
        self.tail = new_node

    # If the list is not empty, then only self.tail will be
    # affected.
    else:
        new_node.prev = self.tail # Set the "prev" of the new node to the current tail
        self.tail.next = new_node # Set the "next" of the current tail to the new node
        self.tail = new_node      # Set the tail equal to the new node
```

Inserting a node at the tail takes O(1)

### To insert a node after the first occurance of 'value'...

1) Create a new node (we will call it new_node)
2) Set the "prev" of the new node to the current node (new_node.prev = current)"
3) Set the "next" of the new node to the next node after current (new_node.next = current.next)
4) Set the "prev" of the "next" node after current to the new node (current.next.prev = new_node)
5) Set the next of the current node to the new node (current.next = new_node)

```python
# Insert 'new_value' after the first occurance of 'value'
def insert_after(self, value, new_value):

        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head

        while curr is not None:

            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'

                if curr == self.tail:
                    self.insert_tail(new_value)

                # For any other location of 'value', need to create a 
                # new node and reconenct the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node       # Connect the node containing 'value' to the new node

                return # We can exit the function after we insert

            curr = curr.next # Go to the next node to search for 'value'
```

Inserting a node after a given value takes O(n)

## Removal

### To remove the head of the linked list...

1) Set the "prev" of the second node (self.head.next) to nothing (self.head.next.prev = None)
2) Set the head to be the second node (self.head = self.head.next)

```python
# This function is in LinkedList class
# Remove the first node (i.e. the head) of the linked list
def remove_head(self):

    # If the list has only one item in it, then set head and tail 
    # to None resulting in an empty list.  This condition will also
    # cover an empty list.  Its okay to set to None again.
    if self.head == self.tail:
        self.head = None
        self.tail = None
        
    # If the list has more than one item in it, then only self.head
    # will be affected.
    elif self.head is not None:
        self.head.next.prev = None  # Disconnect the second node from the first node
        self.head = self.head.next  # Update the head to point to the second node
```

Removing the head takes O(1)

### To remove the tail of the linked list...

1) Set the "next" of the second to last node (self.tail.prev) to nothing (self.tail.prev.next = None)
2) Set the tail to be the second to last node (self.tail = self.tail.prev)

```python
# This function is in LinkedList class
# Remove the last node (i.e. the tail) of the linked list
def remove_tail(self):

    # If the list has only one item in it, then set head and tail 
    # to None resulting in an empty list.  This condition will also
    # cover an empty list.  Its okay to set to None again.
    if self.head == self.tail:
        self.head = None
        self.tail = None

    # If the list has more than one item in it, then only self.tail
    # will be affected.
    elif self.tail is not None:
        self.tail.prev.next = None  # Set the "next" of the second to last node to nothing
        self.tail = self.tail.prev  # Set the tail to be the second to last node
```

Removing the tail takes O(1)

### To remove the first node that contains 'value'...

1) Set the prev of the node after current to the node before current (current.next.prev = current.prev)
2) Set the next of the node before current to the node after current (current.prev.next = current.next)

```python
# This function is in LinkedList class
# Remove the first node that contains 'value'
def remove(self, value):
    
    # if head.data == value, remove head
    if self.head.data == value:
        self.head.next.prev = None
        self.head = self.head.next
        return
    
    # if tail.data == value, remove tail
    if self.tail.data == value:
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return

    # we already checked head.data, so I'll make a pointer to head.next
    current = self.head.next

    # loop through the middle values
    while current.next is not None:
        if current.data == value:
            # Set the prev of the node after current to the node before current
            current.next.prev = current.prev
            # Set the next of the node before current to the node after current
            current.prev.next = current.next
            break
        current = current.next
```

Removing a given value takes O(n)

## Example

Here is the complete implementation of a Double Linked List... 

```python
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

    # Function to insert a new node at the
    # end of tail of the Linked List
    def insert_tail(self, value):

        new_node = LinkedList.Node(value)  

        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node 
            self.tail = new_node  

    # Insert 'new_value' after the first occurance of 'value'
    def insert_after(self, value, new_value):

        curr = self.head
        while curr is not None:
            if curr.data == value:

                if curr == self.tail:
                    self.insert_tail(new_value)

                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr    
                    new_node.next = curr.next 
                    curr.next.prev = new_node 
                    curr.next = new_node      
                return
            curr = curr.next
    
    # Remove the first node (i.e. the head) of the linked list
    def remove_head(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None

        elif self.head is not None:
            self.head.next.prev = None 
            self.head = self.head.next 

    # Remove the last node (i.e. the tail) of the linked list
    def remove_tail(self):

        if self.head == self.tail:
            self.head = None
            self.tail = None

        elif self.tail is not None:
            self.tail.prev.next = None 
            self.tail = self.tail.prev 

    # Remove the first node that contains 'value'
    def remove(self, value):

        if self.head.data == value:
            self.head.next.prev = None
            self.head = self.head.next
            return

        if self.tail.data == value:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return

        current = self.head.next

        while current.next is not None:
            if current.data == value:

                current.next.prev = current.prev

                current.prev.next = current.next
                break
            current = current.next

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


linked_list = LinkedList()
linked_list.insert_head(1)
linked_list.insert_head(2)
linked_list.insert_head(3)
linked_list.insert_head(4)
linked_list.insert_head(5)
linked_list.insert_tail(99)
linked_list.insert_after(4,3.5)
print(linked_list) # linkedlist[5, 4, 3.5, 3, 2, 1, 99]
linked_list.remove_head()
linked_list.remove_tail()
linked_list.remove(3.5)
print(linked_list) # linkedlist[4, 3, 2, 1]
```
Source: Linked Lists (https://byui-cse.github.io/cse212-course/lesson07/07-prepare.html)

## Problem to Solve

Using the simple linked list above, see if you can write a method to check if the Linked List contains a given value.

You can check your code with the solution here: [Solution](double-linked-list.py)

[Back to Welcome Page](0-welcome.md)
