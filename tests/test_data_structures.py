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

    def test_bst_query_node_5_before_insert(self):
        bst = BinarySearchTree()
        answer = bst.query(5)
        self.assertEquals(answer, False)

    def test_bst_query_node_6_after_insert(self):
        bst = BinarySearchTree()
        bst.insert(6)
        answer = bst.query(6)
        self.assertEquals(answer, bst.root)

    def test_bst_query_node_8_after_insert_7_and_8(self):
        bst = BinarySearchTree()
        bst.insert(7)
        bst.insert(8)
        answer = bst.query(8)
        self.assertEquals(answer.value, 8)
        self.assertEquals(answer, bst.root.right)

    def test_bst_query_node_9_after_insert_10_and_9(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(9)
        answer = bst.query(9)
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
        self.assertEqual(bst.min().value, 1)

    def test_bst_max_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.max(), False)

    def test_bst_max_num_list(self):
        bst = BinarySearchTree()
        num_list = [7, 3, 4, 1, 6, 8, 2, 9, 5]
        for n in num_list:
            bst.insert(n)
        self.assertEqual(bst.max().value, 9)

    def test_bst_remove_inexistent_item(self):
        bst = BinarySearchTree()
        was_removed = bst.remove(15)
        self.assertEquals(was_removed, False)

    def test_bst_remove__single_tree_item(self):
        bst = BinarySearchTree()
        bst.insert(16)
        root = bst.remove(16)
        was_found = bst.query(16)
        self.assertEquals(root, None)
        self.assertEquals(was_found, False)
        self.assertEquals(bst.depth(), 0)
        self.assertEquals(bst.size, 0)

    def test_bst_remove_smaller_leaf_from_tree_with_2(self):
        bst = BinarySearchTree()
        bst.insert(18)
        bst.insert(17)
        root = bst.remove(17)
        self.assertEquals(root.value, 18)
        self.assertEquals(bst.depth(), 1)
        self.assertEquals(bst.size, 1)

    def test_bst_remove_larger_leaf_from_tree_with_2(self):
        bst = BinarySearchTree()
        bst.insert(19)
        bst.insert(20)
        root = bst.remove(20)
        self.assertEquals(root.value, 19)
        self.assertEquals(bst.depth(), 1)
        self.assertEquals(bst.size, 1)

    def test_bst_remove_root_from_tree_with_smaller_leaf(self):
        bst = BinarySearchTree()
        bst.insert(22)
        bst.insert(21)
        root = bst.remove(22)
        self.assertEquals(root.value, 21)
        self.assertEquals(bst.depth(), 1)
        self.assertEquals(bst.size, 1)

    def test_bst_remove_root_from_tree_with_larger_leaf(self):
        bst = BinarySearchTree()
        bst.insert(23)
        bst.insert(24)
        root = bst.remove(23)
        self.assertEquals(root.value, 24)
        self.assertEquals(bst.depth(), 1)
        self.assertEquals(bst.size, 1)

    def test_bst_remove_all_items_of_balanced_tree_with_3_items(self):
        bst = BinarySearchTree()
        bst.insert(26)
        bst.insert(25)
        bst.insert(27)
        bst.remove(27)
        bst.remove(25)
        root = bst.remove(26)
        self.assertEquals(root, None)
        self.assertEquals(bst.depth(), 0)
        self.assertEquals(bst.size, 0)

    def test_bst_remove_root_with_left_and_right_children(self):
        bst = BinarySearchTree()
        bst.insert(29)
        bst.insert(28)
        bst.insert(30)
        root = bst.remove(29)
        self.assertEquals(root.value, 28)
        self.assertEquals(root.right.value, 30)
        self.assertEquals(root.left, None)