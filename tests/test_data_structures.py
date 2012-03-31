import unittest
from algorithms.data_structures import Node, Tree, BinarySearchTree


class NodeTestCase(unittest.TestCase):

    def test_node_creation(self):
        node = Node('palavra')
        self.assertEquals(node.left, None)
        self.assertEquals(node.right, None)
        self.assertEquals(node.value, 'palavra')


class TreeTestCase(unittest.TestCase):

    def test_tree_creation(self):
        bst = Tree()
        self.assertEquals(bst.root, None)
        self.assertEquals(bst.size, 0)


class BSTTestCase(unittest.TestCase):

    def test_bst_insert_one_node(self):
        bst = BinarySearchTree()
        bst.insert(1)
        self.assertEquals(bst.root.value, 1)
        self.assertEquals(bst.root.right, None)
        self.assertEquals(bst.root.left, None)
        self.assertEquals(bst.size, 1)

    def test_bst_insert_nodes_1_and_2(self):
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)
        self.assertEquals(bst.root.value, 1)
        self.assertEquals(bst.root.right.value, 2)
        self.assertEquals(bst.root.left, None)
        self.assertEquals(bst.size, 2)

    def test_bst_insert_nodes_4_and_3(self):
        bst = BinarySearchTree()
        bst.insert(4)
        bst.insert(3)
        self.assertEquals(bst.root.value, 4)
        self.assertEquals(bst.root.left.value, 3)
        self.assertEquals(bst.root.right, None)
        self.assertEquals(bst.size, 2)

    def test_bst_lookup_node_5_before_insert(self):
        bst = BinarySearchTree()
        answer = bst.lookup(5)
        self.assertEquals(answer, False)

    def test_bst_lookup_node_6_after_insert(self):
        bst = BinarySearchTree()
        bst.insert(6)
        answer = bst.lookup(6)
        self.assertEquals(answer, bst.root)

    def test_bst_lookup_node_8_after_insert_7_and_8(self):
        bst = BinarySearchTree()
        bst.insert(7)
        bst.insert(8)
        answer = bst.lookup(8)
        self.assertEquals(answer.value, 8)
        self.assertEquals(answer, bst.root.right)

    def test_bst_lookup_node_9_after_insert_10_and_9(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(9)
        answer = bst.lookup(9)
        self.assertEquals(answer.value, 9)
        self.assertEquals(answer, bst.root.left)

    def test_bst_depth_0(self):
        bst = BinarySearchTree()
        self.assertEquals(bst.depth(), 0)

    def test_bst_depth_1(self):
        bst = BinarySearchTree()
        bst.insert(11)
        self.assertEquals(bst.depth(), 1)

    def test_bst_depth_2_two_nodes(self):
        bst = BinarySearchTree()
        bst.insert(12)
        bst.insert(13)
        self.assertEquals(bst.depth(), 2)

    def test_bst_depth_2_three_nodes(self):
        bst = BinarySearchTree()
        bst.insert(15)
        bst.insert(14)
        bst.insert(16)
        self.assertEquals(bst.depth(), 2)

    def test_bst_depth_3(self):
        bst = BinarySearchTree()
        bst.insert(12)
        bst.insert(13)
        bst.insert(14)
        self.assertEquals(bst.depth(), 3)

    def test_bst_min_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.min(), False)

    def test_bst_min_num_list(self):
        bst = BinarySearchTree()
        num_list = [9, 3, 4, 1, 6, 8, 2, 7, 5]
        for n in num_list:
            bst.insert(n)
        self.assertEqual(bst.min(), 1)
