"""
    Find the least common ancestor between two nodes on a binary search tree. 
    The least common ancestor is the farthest node from the root that is an 
    ancestor of both nodes. For example, the root is a common ancestor of all 
    nodes on the tree, but if both nodes are descendents of the root's left child, 
    then that left child might be the lowest common ancestor. You can assume that 
    both nodes are in the tree, and the tree itself adheres to all BST properties. 
    The function definition should look like question4(T, r, n1, n2), where T is the 
    tree represented as a matrix, where the index of the list is equal to the integer 
    stored in that node and a 1 represents a child node, r is a non-negative integer 
    representing the root, and n1 and n2 are non-negative integers representing the 
    two nodes in no particular order.
"""

# A Binary tree node


class Node(object):

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a new node at the beginning


def push_right(node, new_data):
    new_node = Node(new_data)
    node.right = new_node
    return new_node

# Function to insert a new node at the beginning


def push_left(node, new_data):
    new_node = Node(new_data)
    node.left = new_node
    return new_node

# Function to find LCA of node1 and node2. The function assumes
# that both node1 and node2 are present in BST


def lca(root, node1, node2):

    # Check for value in root
    if root is None:
        return None

    # If both node1 and node2 are smaller than root, then LCA
    # lies in left
    if root.data > node1 and root.data > node2:
        return lca(root.left, node1, node2)

    # If both node1 and node2 are greater than root, then LCA
    # lies in right
    if root.data < node1 and root.data < node2:
        return lca(root.right, node1, node2)

    return root.data


def question4(tree, root, node1, node2):
    
    if root is None:
        return "Error: root value is null!"
    
    # Make BST
    node = Node(root)
    node.left, node.right = None, None
    node_data, node_list = 0, []

    if type(tree) != list:
        return "Error: tree is not matrix list!"

    if root >= len(tree):
        return "Error: root value is greater than size of tree matrix!"

    for value in tree[root]:
        if value:
            if node_data > root:
                node_list.append(push_right(node, node_data))
            else:
                node_list.append(push_left(node, node_data))
        node_data += 1

    if len(node_list) <= 0:
        return "Error: root value is not present in tree!"

    temp_node = node_list.pop(0)

    while temp_node != None:
        node_data = 0
        for val in tree[temp_node.data]:
            if val:
                if node_data > temp_node.data:
                    node_list.append(push_right(temp_node, node_data))
                else:
                    node_list.append(push_left(temp_node, node_data))
            node_data += 1

        if node_list == []:
            break
        else:
            temp_node = node_list.pop(0)

    return lca(node, node1, node2)


# Output


print(question4(7, 4, 1, 4))
# Should print - tree is not matrix list!

# Should print - root value is not present in tree!
print(question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [
      0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 4, 1, 4))

print(question4([[0, 0, 0, 0, 0], [1, 0, 1, 0, 0], [
      0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4))
# Should print - 3
