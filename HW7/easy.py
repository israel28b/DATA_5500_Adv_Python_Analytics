
class Node: # Create class Node to allow for a tree
    def __init__(self, data): # Constructor allowing data to be stored in a node
        self.data = data
        self.left = None
        self.right = None # Create the right/left child nodes

def insert(root, value): # Function will take a root and value then logically place data according to parent/child heirarchy 
    # If the tree is empty, return a new node
    if root is None:
        return Node(value)

    # Otherwise, recur down the tree
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    # Return the (unchanged) node pointer
    return root