class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    # A utility function to insert a given key in BST
    def insert_helper(self, root, new_val):
        if root.value < new_val:
            if root.right:
                return self.insert_helper(root.right, new_val)
            else:
                root.right = Node(new_val)
        else:
            if root.left:
                return self.insert_helper(root.left, new_val)
            else:
                root.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    # A utility function to search a given key in BST
    def search_helper(self, root, find_val):
        if root:
            # Base Cases: root is null or key is present at root
            if root.value == find_val:
                return True

            # Key is greater than root's key
            if root.value < find_val:
                self.search_helper(root.left, find_val)
            
            # Key is smaller than root's key
            return self.search_helper(root.right, find_val)

        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
