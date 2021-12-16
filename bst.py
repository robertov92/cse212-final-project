# Binary Serach Tree class (BTS)
class BST:
    # Node class
    class Node:

        # Function to initialize the node object
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    # Function to initialize a BTS object
    def __init__(self):
        self.root = None

    ## Inserting
    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data == node.data:
            return

        elif data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)

        elif data > node.data:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

    # These functions should be in the BST class
    # If the tree is empty, then return 0.  Otherwise, call 
    # _get_height on the root which will recursively determine the 
    # height of the tree.
    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    # Determine the height of the BST.  The height of a sub-tree 
    # (represented by 'node') is 1 plus the height of either the 
    # left sub-tree or the right sub-tree (whichever one is bigger).
    # This function intended to be called the first time by 
    # get_height.
    def _get_height(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)

            # Using the larger one
            if (left_height > right_height):
                return left_height +1
            else:
                return right_height +1

# Declare a BST
tree = BST()

# Insert a few values
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(10)
tree.insert(9)

# Determines the height of the BST
print(tree.get_height()) # 4
tree.insert(6)
print(tree.get_height()) # 4
tree.insert(12)
tree.insert(13)
tree.insert(14)
print(tree.get_height()) # 6


