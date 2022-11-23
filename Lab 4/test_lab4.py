from rb_tree import Node, rb_tree
import unittest
 
class T0_tree_left_rotation(unittest.TestCase):

    def test_tree_left_rotation_1(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [3,2,1])
        tree.print_tree()
        print("tree after left rotation about root  in prorder")
        print("\n")
    
    def test_tree_left_rotation_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [9,7,5,3,1,2,6,8,10])
        tree.print_tree()
        print("tree after left rotation about root  in prorder")
        print("\n")
    


class T1_tree_right_rotation(unittest.TestCase):

    def test_tree_right_rotation_1(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)

        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [1,2,3])
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")
    
    def test_tree_right_rotation_2(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [5,3,1,2,7,6,9,8,10])
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")
    

class T2_tree_insert_color(unittest.TestCase):


    def test_tree_insert_color_0(self):
        print("\n")
        print("tree_color_check")
        
        tree = rb_tree()

        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.insert(4)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 3, 4])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black', 'red'])
        print("\n")


    def test_tree_insert_color_1(self):
        print("\n")
        print("tree_color_check")
        
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 4, 3, 6, 5, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black', 'red', 'red'])
        print("\n")

class T3_tree_delete(unittest.TestCase):


    def test_tree_delete_0(self):
        print("\n")
        print("tree_insert")
        #print("checking in order, preorder and post order")
        tree = rb_tree()

        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 6, 9])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black'])
        tree.delete(9)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [6, 5, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black'])
        print("\n")

    def test_tree_delete_1(self):
        print("\n")
        print("tree_insert")
        print("checking in order, preorder and post order")
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.delete(5)
        tree.delete(4)
        # tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 6, 3, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black'])
        print("\n")
    
    def test_tree_delete_color_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(3)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(1)
        tree.insert(2)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 2, 1, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'])
        tree.delete(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 2, 1, 5, 3, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red', 'red'])
        tree.delete(7)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [8, 2, 1, 5, 3, 9, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red'])
        print("\n")

class T4_tree_rotation_intermediate(unittest.TestCase):

    T = rb_tree()
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    T.root = a
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    b.parent = a
    c.parent = a
    d.parent = b
    e.parent = b
    f.parent = c
    g.parent = c

    for node in [d,e,f,g]:
        node.left, node.right = T.sentinel, T.sentinel

    a.parent = T.sentinel

    def test_right_rotation(self):

        self.T.right_rotate(self.T.root.left)

        self.assertEqual(self.T.root.data, 'c')
        self.assertEqual(self.T.root.left.data, 'a')
        self.assertEqual(self.T.root.right.data, 'g')
        self.assertEqual(self.T.root.left.left.data, 'b')
        self.assertEqual(self.T.root.left.right.data, 'f')
        self.assertEqual(self.T.root.right.left.data, None)
        self.assertEqual(self.T.root.right.right.data, None)

        self.assertEqual(self.T.root.parent.data, None)
        self.assertEqual(self.T.root.left.parent.data, 'c')
        self.assertEqual(self.T.root.right.parent.data, 'c')
        self.assertEqual(self.T.root.left.left.parent.data, 'a')
        self.assertEqual(self.T.root.left.right.parent.data, 'a')
        #self.assertEqual(self.T.root.right.left.parent.data, )
        #self.assertEqual(self.T.root.right.right.parent.data, )

    def test_left_rotation(self):

        self.T.right_rotate(self.T.root.right)

        self.assertEqual(self.T.root.data, 'b')
        self.assertEqual(self.T.root.left.data, 'd')
        self.assertEqual(self.T.root.right.data, 'a')
        self.assertEqual(self.T.root.left.left.data, None)
        self.assertEqual(self.T.root.left.right.data, None)
        self.assertEqual(self.T.root.right.left.data, 'e')
        self.assertEqual(self.T.root.right.right.data, 'c')

        self.assertEqual(self.T.root.parent.data, None)
        self.assertEqual(self.T.root.left.parent.data, 'b')
        self.assertEqual(self.T.root.right.parent.data, 'b')
        #self.assertEqual(self.T.root.left.left.parent.data, )
        #self.assertEqual(self.T.root.left.right.parent.data, )
        self.assertEqual(self.T.root.right.left.parent.data, 'a')
        self.assertEqual(self.T.root.right.right.parent.data, 'a')

class T5_tree_insert_color_validation(unittest.TestCase):
        
    def test_small_inserts(self):
        test_vals = [10, 18, 7, 15, 16]
        T = rb_tree()
        for val in test_vals: T.insert(val)
        tree_preorder = [node.data for node in T.preorder()]
        tree_preorder_color = [node.color for node in T.preorder()]

        self.assertEqual(tree_preorder, [10, 7, 16, 15, 18])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black', 'red', 'red'])

    def test_additional_insert(self):
        test_vals = [10, 18, 7, 15, 16, 25, 23]
        T = rb_tree()
        for val in test_vals: T.insert(val)
        tree_preorder = [node.data for node in T.preorder()]
        tree_preorder_color = [node.color for node in T.preorder()]

        self.assertEqual(tree_preorder, [10, 7, 16, 15, 23, 18, 25])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black', 'red', 'red'])

class T6_tree_deletion_color_validation(unittest.TestCase):

    def test_small_deletion(self):
        test_vals = [10, 18, 7, 15, 16]
        T = rb_tree()
        for val in test_vals: T.insert(val)
        T.delete(16)
        tree_preorder = [node.data for node in T.preorder()]
        tree_preorder_color = [node.color for node in T.preorder()]
        
        self.assertEqual(tree_preorder, [10, 7, 15, 18])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black', 'red'])

    def test_med_deletion(self):
        test_vals = [10, 18, 7, 15, 16, 25]
        T = rb_tree()
        for val in test_vals: T.insert(val)
        T.delete(10)
        tree_preorder = [node.data for node in T.preorder()]
        tree_preorder_color = [node.color for node in T.preorder()]
        
        self.assertEqual(tree_preorder, [15, 7, 18, 16, 25])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black'])

class T7_tree_operations_series_color_validation(unittest.TestCase):

    def test_med_delete_insert_delete(self):
        test_vals = [10, 18, 7, 15, 16, 25]
        T = rb_tree()
        for val in test_vals: T.insert(val)
        T.delete(10)
        tree_preorder = [node.data for node in T.preorder()]
        tree_preorder_color = [node.color for node in T.preorder()]
        
        self.assertEqual(tree_preorder, [15, 7, 18, 16, 25])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black'])

        T.insert(19)
        T.insert(20)

        self.assertEqual(tree_preorder, [15, 7, 18, 16, 20, 19, 25])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black', 'red', 'red'])

        T.delete(20)

        self.assertEqual(tree_preorder, [15, 7, 18, 16, 25, 19])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black', 'red'])

if __name__ == "__main__":
    unittest.main()
