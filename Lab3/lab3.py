"""
CLASS: CS 313
AUTHOR: Vincent Lanier
TITLE: LAB 3
CONTENTS: Binary Search Tree Implementation
"""


class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """
    A standard binary search tree. 

    For a given node N it is guaranteed that each node in the subtree
    rooted by its left child contains data less that in N, and each 
    node in the subtree rooted by its right child contains data 
    greater than that in N.

    Attributes
    -----
    root : Node or None
        A pointer to the root of the binary search tree

    Methods
    -----
    print()
        Print the data of all nodes in order

    insert(data)
        Insert a new node containing the given data

    min()
        Return the minimum value in the tree

    max()
        Return the maximum value in the treee

    contains(data)
        Return True if the data is found in the tree
        Otherwise return false

    inorder()
        Return a generator over the tree data. Data is 
        ordered as a 'inorder' traversal.

    preorder()
        Return a generator over the tree data. Data is 
        ordered as a 'preorder' traversal.

    postorder()
        Return a generator over the tree data. Data is 
        ordered as a 'postorder' traversal.

    find_successor(data)
        Return the node holding the successor of data.
        Return False if data is not found.

    delete(data) 
        Remove the data from the tree.
        Raises KeyError if data not found.
    """
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        """Initialze a new Binary Search Tree"""
        self.root = None

    def print(self):
        """Print the data of all nodes in order"""
        self.__print(self.root)

    def __print(self, curr_node):
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')
            self.__print(curr_node.right)

    def insert(self, data):
        """
        Insert a new node containing data

        Parameters
        -----
        data : int or float
            The value to be inserted
        """
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            return

        prev_node = None
        curr_node = self.root
        while curr_node:
            data_is_less = data < curr_node.data
            prev_node = curr_node
            curr_node = curr_node.left if data_is_less else curr_node.right

        if data_is_less:
            prev_node.left = new_node
        else:
            prev_node.right = new_node

        new_node.parent = prev_node

    def min(self):
        """
        Return the minimum value in the tree.
        Return None if the tree is empty.
        """
        if not self.root:
            return

        curr_node = self.root
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node.data

    def max(self):
        """
        Return the maximum value held in the tree
        Return None if the tree is empty
        """
        if not self.root:
            return

        curr_node = self.root
        while curr_node.right:
            curr_node = curr_node.right
        return curr_node.data

    def __find_node(self, data):
        if not self.root:
            return

        curr_node = self.root
        while curr_node and curr_node.data != data:
            curr_node = curr_node.left if data < curr_node.data else curr_node.right
        return curr_node

    def find_node(self, data):
        ### PUBLIC WRAPPER FOR FIND NODE ###
        # Inserting this so I can unittest find_node as asked in the instructions
        # It will also be tested in the successor tests as well as the contains tests
        return self.__find_node(data)

    def contains(self, data):
        """
        Return True if the data is present in the tree. Otherwise, return False.

        Parameters
        -----
        data : int or float
            The value to look for
        """
        return self.__find_node(data) is not None

    def __iter__(self):
        return self.inorder()

    def inorder(self):
        """Return an inorder traversal generator"""
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        """Return a preorder traversal generator"""
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        """Return a postorder traversal generator"""
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        if curr_node is None:  # PEP225?
            return
        if traversal_type is Tree.PREORDER:
            yield curr_node.data
        if curr_node.left:
            yield from self.__traverse(curr_node.left, traversal_type)
        if traversal_type is Tree.INORDER:
            yield curr_node.data
        if curr_node.right:
            yield from self.__traverse(curr_node.right, traversal_type)
        if traversal_type is Tree.POSTORDER:
            yield curr_node.data

    def find_successor(self, data):
        """
        Return the node containing the successor of data. Return None if no successor found.

        The successor is the 'next larger' element found in the tree.

        Parameters
        -----
        data : int or float
            The data to find the sucessor of

        Raises
        -----
        KeyError
            If the given data is not found in the tree
        """

        curr_node = self.__find_node(data)

        if curr_node is None:
            raise KeyError(f'{data} does not exist in the tree')

        if curr_node.right:
            curr_node = curr_node.right
            while curr_node.left:
                curr_node = curr_node.left
            return curr_node

        while curr_node:
            if curr_node.parent and curr_node.parent.left == curr_node:
                return curr_node.parent
            curr_node = curr_node.parent

    def __transplant(self, node_a, node_b):
        if node_a.parent is None:
            self.root = node_b
        elif node_a == node_a.parent.left:
            node_a.parent.left = node_b
        else:
            node_a.parent.right = node_b
        if node_b:
            node_b.parent = node_a.parent

    def delete(self, data):
        """
        Delete the given data from the tree

        Parameters
        -----
        data : int or float
            The data to delete from the tree

        Raises
        -----
        KeyError
            If the given data is not found in the tree
        """

        curr_node = self.find_node(data)

        if curr_node is None:
            raise KeyError(f'{data} does not exist in the tree')

        if curr_node.left is None:
            self.__transplant(curr_node, curr_node.right)
            return

        if curr_node.right is None:
            self.__transplant(curr_node, curr_node.left)
            return

        successor = curr_node.right
        while(successor.left):
            successor = successor.left

        if successor.parent != curr_node:
            self.__transplant(successor, successor.right)
            successor.right = curr_node.right
            successor.right.parent = successor

        self.__transplant(curr_node, successor)
        successor.left = curr_node.left
        successor.left.parent = successor
