
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


def search(root, value): # Function will take two paramters, a root, and a value to be searched for
    if root is None:  # Base case: empty tree
        return False
    
    if root.data == value:  # Value found at the current node
        return True
    
    elif value < root.data:  # Value might be in the left subtree
        return search(root.left, value)
    
    else:  # Value might be in the right subtree
        return search(root.right, value)


root = None
root = insert(root,30)
insert(root, 50)
insert(root, 40)
insert(root, 60)
insert(root, 100)


print(search(root, 120))