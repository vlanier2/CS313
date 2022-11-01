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
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        pass

    def min(self):
        """
        Return the minimum value in the tree.
        Return None if the tree is empty.
        """
        pass

    def max(self):
        """
        Return the maximum value held in the tree
        Return None if the tree is empty
        """
        pass

    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        pass

    def contains(self, data):
        """
        Return True if the data is present in the tree. Otherwise, return False.

        Parameters
        -----
        data : int or float
            The value to look for
        """
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        pass

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
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
        # helper method implemented using generators
        # all the traversals can be implemented using a single method

        # Yield data of the correct node/s
        pass

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
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None

        # Return object of successor if found else return None
        pass

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
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None

        pass
