"""
CS 313 LAB 4
AUTHOR: VINCENT LANIER
CONTENTS: RED BLACK TREE IMPLEMENTATION
DATE: NOVEMBER 2022
"""

class Node(object):
    def __init__(self, data, left = None, right = None, parent = None, color = 'red'):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class rb_tree(object):
    """
    A Red-Black Tree - A type of self-balancing Binary Search Tree. 

    For a given node N it is guaranteed that each node in the subtree
    rooted by its left child contains data less that in N, and each 
    node in the subtree rooted by its right child contains data 
    greater than that in N.

    A Red-Black Tree guarantees that the longest path from the root to a leaf
    is at most twice as long as the path from the root to the closest leaf.
    As a consequence the height of the tree is at most 2 * lg(n+1) and is 
    reasonably well balanced.

    Attributes
    -----
    root : Node or None
        A pointer to the root of the binary search tree

    Methods
    -----
    print_tree()
        Print the data of all nodes in order

    insert(data)
        Insert a new node containing the given data

    find_min()
        Return the node holding the minimum value in the tree

    find_node(data)
        Return the Node object for the given data

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

    left_rotate(current_node)
        Performs a left rotation about the given node.

    right_rotate(current_node)
        Performs a right rotation about the given node.
    """
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    # initialize root and size
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel
    
    def print_tree(self):
        # Print the data of all nodes in order
        self.__print_tree(self.root)
    
    def __print_tree(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in preorder
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')  # save space
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in PREORDER
        # Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red
        if curr_node is not self.sentinel:

            if curr_node.color == "red":
                node_color = "R"
            else:
                node_color = "B"

            print(str(curr_node.data)+node_color, end=' ')  # save space
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        # Also prints the data of all node but with color indicators
        self.__print_with_colors(self.root)
              
    def __iter__(self):
        return self.inorder()

    def inorder(self):
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    # find_min travels across the leftChild of every node, and returns the
    # node who has no leftChild. This is the min value of a subtree
    def find_min(self):
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node
    
    # find_node expects a data and returns the Node object for the given data
    def find_node(self, data):
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function __get receives a data and a node. Returns the node with
    # the given data
    def __get(self, data, current_node):
        if current_node is self.sentinel: # if current_node does not exist return None
            print("couldnt find data: {}".format(data))
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            # recursively call __get with data and current_node's left
            return self.__get( data, current_node.left )
        else: # data is greater than current_node.data
            # recursively call __get with data and current_node's right
            return self.__get( data, current_node.right )

    def find_successor(self, data):
        # Private Method, can only be used inside of BST.
        current_node = self.find_node(data)

        if current_node is self.sentinel:
            raise KeyError

        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node

        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        if successor:
            return successor
        else:
            return None

    def insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(data, self.root)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)
    
    #Insertion for Binary Search Tree
    def bst_insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            self.__put(data, self.root)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
        
    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, data, current_node):
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else: # current_node has no child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.left = new_node
        else: # data is greater than or equal to current_node's data
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else: # current_node has no right child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.right = new_node
        return new_node

    def delete(self, data):
        # Same as binary tree delete, except we call rb_delete fixup at the end.

        z = self.find_node(data)
        if z.left is self.sentinel or z.right is self.sentinel:
            y = z
        else:
            y = self.find_successor(z.data)
        
        if y.left is not self.sentinel:
            x = y.left
        else:
            x = y.right
        
        if x is not self.sentinel:
            x.parent = y.parent

        if y.parent is self.sentinel:
            self.root = x

        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        
        if y is not z:
            z.data = y.data
    
        if y.color == 'black':
            if x is self.sentinel:
                self.__rb_delete_fixup(y)
            else:
                self.__rb_delete_fixup(x)

    def left_rotate(self, current_node):
        """
        Performs a left rotation about the given node. 

        Rotations are operations that alter the structure of the Tree
        around the given node. A left rotation will decrease the height
        of the right subtree of current_node and increase the height of
        the left subtree. All BST properties are maintained after the
        rotation. WARNING - calling left_rotate alone does not update
        node colors and may cause red-black violations.

        Parameters
        -----
        current_node : Object of type Node
            The node to left rotate
        """
        # If there is nothing to rotate with, then raise a KeyError
        # if x is the root of the tree to rotate with left child subtree T1 and right child y, 
        # where T2 and T3 are the left and right children of y then:
        # x becomes left child of y and T3 as its right child of y
        # T1 becomes left child of x and T2 becomes right child of x

        # refer page 328 of CLRS book for rotations

        pass
    
    def right_rotate(self, current_node):
        """
        Performs a right rotation about the given node. 

        Rotations are operations that alter the structure of the Tree
        around the given node. A right rotation will decrease the height
        of the left subtree of current_node and increase the height of
        the right subtree. All BST properties are maintained after the
        rotation. WARNING - calling right_rotate alone does not update
        node colors and may cause red-black violations.

        Parameters
        -----
        current_node : Object of type Node
            The node to right rotate
        """
        # If there is nothing to rotate with, then raise a KeyError
        # If y is the root of the tree to rotate with right child subtree T3 and left child x, 
        # where T1 and T2 are the left and right children of x then:
        # y becomes right child of x and T1 as its left child of x
        # T2 becomes left child of y and T3 becomes right child of y

        # refer page 328 of CLRS book for rotations

        pass
 
    def __rb_insert_fixup(self, z):
        """
        Resolves red-red conflicts after insertion at the given position in the tree.

        Red-Black trees must maintain equivalent black height in all paths.
        That is, all paths from the root to a leaf must contain the same 
        number of black nodes. Red-Black trees must also not allow red nodes
        to be adjacent in any path. rb_insert_fixup considers all needed cases
        to resolve red-red conflicts and maintain Red-Black properties after 
        inserting a new red node z.

        Paremeters
        -----
        z : Object of type Node
            Node inserted per BST insertion algorithm
        """
        # This function maintains the balancing and coloring property after bst insertion into
        # the tree. Please red the code for insert() method to get a better understanding
        # refer page 330 of CLRS book and lecture slides for rb_insert_fixup

        pass

    def __rb_delete_fixup(self, x):
        """
        Resolves red-red conflicts after deletion at the given position in the tree.

        Red-Black trees must maintain equivalent black height in all paths.
        That is, all paths from the root to a leaf must contain the same 
        number of black nodes. Red-Black trees must also not allow red nodes
        to be adjacent in any path. rb_delete_fixup considers all needed cases
        to resolve red-red conflicts and maintain Red-Black properties after 
        deleting a node and replacing it with it's child x.

        Paremeters
        -----
        x : Object of type Node
            Child node of the node removed per BST deletion algorithm
        """
        # This function maintains the balancing and coloring property after bst deletion 
        # from the tree. Please read the code for delete() method to get a better understanding.
        # refer page 338 of CLRS book and lecture slides for rb_delete_fixup
        
        pass

if __name__ == "__main__":

    case1 = rb_tree()
    case1.bst_insert(10)
    print('case1')
    case1.print_tree()
    print([node.data for node in case1.inorder()])
    print()

    case2 = rb_tree()
    case2.bst_insert(10)
    case2.bst_insert(5)
    case2.bst_insert(15)
    print('case2')
    case2.print_tree()
    print([node.data for node in case2.inorder()])
    print()

    case3 = rb_tree()
    case3.bst_insert(10)
    case3.bst_insert(5)
    case3.bst_insert(15)
    case3.bst_insert(12)
    print('case3')
    case3.print_tree()
    print([node.data for node in case3.inorder()])
    print()

    case4 = rb_tree()
    case4.bst_insert(10)
    case4.bst_insert(5)
    case4.bst_insert(15)
    case4.bst_insert(12)
    case4.bst_insert(20)
    print('case4')
    case4.print_tree()
    print([node.data for node in case4.inorder()])
    print()

    print('------------------------------------------------')

    print("\n")
    print("tree_insert")
    print("checking in order, preorder and post order")
    tree = rb_tree()
    for i in range(1, 8):
        tree.insert(i)
    tree.delete(5)
    tree.delete(4)
    tree_preorder = [node.data for node in tree.preorder()]
    tree_preorder_color = [node.color for node in tree.preorder()]
    print("\n")
    print('finosehd ')
    