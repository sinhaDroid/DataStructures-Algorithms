"""
    Find the element in a singly linked list that's m elements from the end. 
    For example, if a linked list has 5 elements, the 3rd element from the end 
    is the 3rd element. The function definition should look like question5(ll, m), 
    where ll is the first node of a linked list and m is the "mth number from the end". 
    You should copy/paste the Node class below to use as a representation of a node in 
    the linked list. Return the value of the node at that position.

    class Node(object):
        def __init__(self, data):
        self.data = data
        self.next = None 
"""


class Node:

    # Constructor to push a new node in list
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning

    def insert(self, new_element):
        # Allocate the node and put it in data
        node = Node(new_element)
        # Make next of new node as head
        node.next = self.head
        # Move the head to point to new Node
        self.head = node

    # Function to find the m elements from the end

    def question5(self, head, m):
        temp = head
        count = 0

        while temp != None:
            temp = temp.next
            count += 1

        # check if value of n is not more than length of
        # linked list
        if count < m:
            return

        temp = head

        #   get the (count-m+1)th node from the beginning
        for i in range(1, count-m+1):
            temp = temp.next
            i += 1

        return temp.data


# Insert data into list
ll = LinkedList()
ll.insert(50)
ll.insert(40)
ll.insert(30)
ll.insert(20)
ll.insert(10)

# Test LinkedList
print(ll.question5(ll.head, 4))
