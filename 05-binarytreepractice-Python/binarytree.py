class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

def search(self, find_val):
    """
    Return True if the find_val is in the tree and False otherwise.
    """
    # Your code goes here
    
    if(find_val == self.find_val):
        return self
    if(find_val < self.find_val):
        return self.left.search(find_val) if self.left else None
    if(find_val > self.find_val):
        return self.right.search(find_val) if self.right else None
        

def print_tree(tree):
    """
    Print out all tree nodes as they are visited in a pre-order traversal."""
    # Your code goes here
    # if(tree.left):
    #     tree.left.print_tree().value
    #     print(tree.left.value)
    # print(tree.value)
    # if(tree.right):
    #     tree.right.print_tree().value
    
    # print_tree(tree.left)
    # print(tree," sdkjgosdhg")
    # print_tree(tree.right)


def preorder_search(self, start, find_val):
    """
    Helper method - use this to create a recursive search solution.
    """
    # Your code goes here
    pass

def preorder_print(self, start, traversal):
    """
    Helper method - use this to create a recursive print solution.
    """
    # Your code goes here
    pass


tree = BinaryTree(1)
print("zvjs")
tree.root.left = Node(2)
print("dfnsdn")
tree.root.right = Node(3)
tree.root.left.left = Node(4)
print("dlgjdog")
tree.root.left.right = Node(5)
print("agljfbsdjg")
print_tree(tree)
