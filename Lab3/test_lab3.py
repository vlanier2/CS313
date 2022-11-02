import lab3
import unittest


class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")

    def test_insert_empty(self):
        t = lab3.Tree()

        t.insert(13)
        self.assertEqual(t.root.data, 13)

    def test_insert_delete_insert(self):
        t = lab3.Tree()

        t.insert(3)
        t.insert(4)
        t.delete(4)
        t.insert(5)
        self.assertEqual(t.root.right.data, 5)


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

    def test_min_and_max_empty(self):
        t = lab3.Tree()

        self.assertEqual(t.min(), None)
        self.assertEqual(t.max(), None)


class T2_Traversal(unittest.TestCase):

    test_data = [10, 11, 8, 3, 2, 12, 4]

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")

    def test_traversal_postorder(self):

        t = lab3.Tree()
        for d in self.test_data:
            t.insert(d)

        self.assertEqual([n for n in t.postorder()], [2, 4, 3, 8, 12, 11, 10])

    def test_traversal_empty(self):

        t = lab3.Tree()
        self.assertEqual([n for n in t.postorder()], [])
        self.assertEqual([n for n in t.preorder()], [])
        self.assertEqual([n for n in t.inorder()], [])

    def test_traversal_after_delete(self):

        t = lab3.Tree()
        for d in self.test_data:
            t.insert(d)
        t.delete(2)
        t.delete(10)
        self.assertEqual([n for n in t.postorder()], [4, 3, 8, 12, 11])
        self.assertEqual([n for n in t.preorder()], [11, 8, 3, 4, 12])
        self.assertEqual([n for n in t.inorder()], [3, 4, 8, 11, 12])


class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")

    def test_successor_empty(self):
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.find_successor(4)

    def test_successor_after_delete(self):
        t = lab3.Tree()
        t.insert(1)
        t.insert(3)
        t.insert(-1)
        self.assertEqual(t.find_successor(1).data, 3)
        t.delete(3)
        self.assertEqual(t.find_successor(1), None)
        self.assertEqual(t.find_successor(-1).data, 1)
        with self.assertRaises(KeyError):
            t.find_successor(3)


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]

        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

    def test_delete_empty(self):
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.delete('2')

    def test_delete_final(self):
        t = lab3.Tree()
        t.insert(12)
        t.delete(12)
        self.assertEqual([n for n in t], [])
        with self.assertRaises(KeyError):
            t.delete(1)


class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

    def test_contains_empty(self):
        t = lab3.Tree()
        self.assertEqual(t.contains(34), False)
        self.assertEqual(t.contains(0), False)

    def test_contains_afterdelete(self):
        t = lab3.Tree()
        t.insert(1)
        self.assertEqual(t.contains(1), True)
        t.insert(2)
        t.delete(1)
        self.assertEqual(t.contains(2), True)
        self.assertEqual(t.contains(1), False)


class T6_find_node(unittest.TestCase):

    t = lab3.Tree()
    test_data = [10, 9, 8, 3, 2, 1, 4]
    for n in test_data:
        t.insert(n)

    def test_find_node_empty(self):
        t = lab3.Tree()
        self.assertEqual(t.find_node(2), None)

    def test_find_node_standard(self):
        self.assertEqual(self.t.find_node(10).data, 10)

    def test_find_node_not_found(self):
        self.assertEqual(self.t.find_node(123), None)


if __name__ == '__main__':
    unittest.main()
