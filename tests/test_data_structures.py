import unittest
from algorithms.data_structures import AVLTree, BinaryNode, BinarySearchTree, Tree, List, MoveToFrontList, HashEntry, MyString, HashTable, OptimalBinarySearchTree, OptimalBinaryNode
from fixtures import TREE_WITH_1, TREE_WITH_6, TREE_WITH_7


class BinaryNodeTestCase(unittest.TestCase):

    def test_node_creation(self):
        node = BinaryNode('palavra')
        self.assertEquals(node.left, None)
        self.assertEquals(node.right, None)
        self.assertEquals(node.value, 'palavra')
        self.assertEquals(node.depth, 0)

    def test_equal_nodes(self):
        node1 = BinaryNode("arara")
        node2 = BinaryNode("arara")
        self.assertEquals(node1, node2)

    def test_not_equal_nodes(self):
        node1 = BinaryNode("papagaio")
        node2 = BinaryNode("arara azul")
        assert node1 != node2

    def test_less_node(self):
        node1 = BinaryNode("Rio de Janeiro")
        node2 = BinaryNode("Curitiba")
        self.assertTrue(node1 > node2)

    def test_greater_node(self):
        node1 = BinaryNode("Uberaba")
        node2 = BinaryNode("Uberlandia")
        self.assertTrue(node1 < node2)




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

    def test_bst_height_0(self):
        bst = BinarySearchTree()
        self.assertEquals(bst.height, 0)

    def test_bst_height_1(self):
        bst = BinarySearchTree()
        bst.insert(11)
        self.assertEquals(bst.height, 1)

    def test_bst_height_2_two_nodes(self):
        bst = BinarySearchTree()
        bst.insert(12)
        bst.insert(13)
        self.assertEquals(bst.height, 2)

    def test_bst_height_2_three_nodes(self):
        bst = BinarySearchTree()
        bst.insert(15)
        bst.insert(14)
        bst.insert(16)
        self.assertEquals(bst.height, 2)

    def test_bst_height_3(self):
        bst = BinarySearchTree()
        bst.insert(12)
        bst.insert(13)
        bst.insert(14)
        self.assertEquals(bst.height, 3)

    def test_bst_min_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.min, False)

    def test_bst_min_values_list(self):
        bst = BinarySearchTree()
        values_list = [9, 3, 4, 1, 6, 8, 2, 7, 5]
        bst.insert_list(values_list)
        self.assertEqual(bst.min.value, 1)

    def test_bst_max_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.max, False)

    def test_bst_max_values_list(self):
        bst = BinarySearchTree()
        values_list = [7, 3, 4, 1, 6, 8, 2, 9, 5]
        bst.insert_list(values_list)
        self.assertEqual(bst.max.value, 9)

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
        self.assertEquals(bst.height, 0)
        self.assertEquals(bst.size, 0)

    def test_bst_remove_smaller_leaf_from_tree_with_2(self):
        bst = BinarySearchTree()
        bst.insert(18)
        bst.insert(17)
        root = bst.remove(17)
        self.assertEquals(root.value, 18)
        self.assertEquals(bst.height, 1)
        self.assertEquals(bst.size, 1)

    def test_bst_remove_larger_leaf_from_tree_with_2(self):
        bst = BinarySearchTree()
        bst.insert(19)
        bst.insert(20)
        root = bst.remove(20)
        self.assertEquals(root.value, 19)
        self.assertEquals(bst.height, 1)
        self.assertEquals(bst.size, 1)

    def test_bst_remove_root_from_tree_with_smaller_leaf(self):
        bst = BinarySearchTree()
        bst.insert(22)
        bst.insert(21)
        root = bst.remove(22)
        self.assertEquals(root.value, 21)
        self.assertEquals(bst.height, 1)
        self.assertEquals(bst.size, 1)

    def test_bst_remove_root_from_tree_with_larger_leaf(self):
        bst = BinarySearchTree()
        bst.insert(23)
        bst.insert(24)
        root = bst.remove(23)
        self.assertEquals(root.value, 24)
        self.assertEquals(bst.height, 1)
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
        self.assertEquals(bst.height, 0)
        self.assertEquals(bst.size, 0)

    def test_bst_remove_root_with_left_and_right_children(self):
        bst = BinarySearchTree()
        bst.insert(29)
        bst.insert(28)
        bst.insert(30)
        root = bst.remove(29)
        self.assertEquals(bst.size, 2)
        self.assertEquals(root.value, 28)
        self.assertEquals(root.right.value, 30)
        self.assertEquals(root.left, None)

    def test_bst_with_complex_tree(self):
        bst = BinarySearchTree()
        values_list = [6, 8, 2, 1, 4, 3]
        bst.insert_list(values_list)
        root = bst.remove(6)
        self.assertEquals(bst.size, 5)
        self.assertEquals(root.value, 4)

    def test_bst_to_string_tree_with_1_node(self):
        bst = BinarySearchTree()
        bst.insert(1)
        printlines = bst.to_string(bst.root)
        self.assertEquals(printlines, TREE_WITH_1)

    def test_bst_to_string_tree_with_6_nodes(self):
        bst = BinarySearchTree()
        values_list = [6, 8, 2, 1, 4, 3]
        bst.insert_list(values_list)
        printlines = bst.to_string(bst.root)
        self.assertEquals(printlines, TREE_WITH_6)

    def test_bst_to_string_tree_with_7_nodes(self):
        bst = BinarySearchTree()
        values_list = [4, 2, 1, 3, 6, 5, 7]
        bst.insert_list(values_list)
        printlines = bst.to_string(bst.root)
        self.assertEquals(printlines, TREE_WITH_7)


class AVLTTestCase(unittest.TestCase):

    def test_empty_avl_is_balanced(self):
        avl_tree = AVLTree()
        self.assertEquals(avl_tree.is_balanced(), True)

    def test_avl_with_one_key_is_balanced(self):
        avl_tree = AVLTree()
        avl_tree.insert(1)
        self.assertEquals(avl_tree.is_balanced(), True)

    def test_avl_with_two_keys_is_balanced(self):
        values_list = [1, 2]
        avl_tree = AVLTree()
        avl_tree.insert_list(values_list)
        self.assertEquals(avl_tree.is_balanced(), True)

    def test_avl_unbalanced_with_insertion_becomes_balanced_case_i(self):
        values_list = [5, 4, 3]
        """
            5
          4
        3
        becomes:
            4
          3   5
        """
        avl_tree = AVLTree()
        avl_tree.insert_list(values_list)
        self.assertEquals(avl_tree.is_balanced(), True)

    def test_avl_unbalanced_with_insertion_becomes_balanced_case_ii(self):
        values_list = [1, 2, 3]
        """
            1
              2
                3
        becomes:
            2
          1   3
        """
        avl_tree = AVLTree()
        avl_tree.insert_list(values_list)
        self.assertEquals(avl_tree.is_balanced(), True)

    def test_avl_unbalanced_with_insertion_becomes_balanced_case_i_complex(self):
        values_list = [73, 31, 94, 7, 64, 76, 98, 3, 23, 60, 2]
        """
        given the AVL tree:
                    73
              31         94
           7      64   76   98
         3  23  60

        + node 2 becomes:

                31
           7          73
         3  23      64   94
        2         60    76 98
        """
        avl_tree = AVLTree()
        avl_tree.insert_list(values_list)
        self.assertEquals(avl_tree.is_balanced(), True)

    def test_avl_unbalanced_with_insertion_becomes_balanced_case_iii(self):
        values_list = [6, 4, 5]
        """
           6
        4
         5
        becomes:
          5
        4   6
        """

        avl_tree = AVLTree()
        avl_tree.insert_list(values_list)
        self.assertEquals(avl_tree.is_balanced(), True)

    def test_avl_unbalanced_with_insertion_becomes_balanced_case_iv(self):
        values_list = [7, 9, 8]
        """
           7
             9
            8
        becomes:
          8
        7   9
        """

        avl_tree = AVLTree()
        avl_tree.insert_list(values_list)
        self.assertEquals(avl_tree.is_balanced(), True)

    def test_avl_node_removal_complex(self):
        values_list = [35, 19, 62, 5, 24, 61, 86, 4, 6, 22, 28, 94, 20, 23, 26, 30]
        """
        given the AVL tree:
                      35
                19           62
           5        24     61   86
         4   6   22   28          94
               20 23 26 30

        - node 94 becomes:

                  24
            19           35
         5    22      28    62
        4 6  20 23  26 30  61 86
        """
        avl_tree = AVLTree()
        avl_tree.insert_list(values_list)
        self.assertEquals(avl_tree.is_balanced(), True)


#class OptimalBSTTestCase(unittest.TestCase):
#
#    def test_x(self):
#        OptimalBinarySearchTree


class ListTestCase(unittest.TestCase):

    def test_list_creation(self):
        my_list = List()
        self.assertEquals(my_list.root, None)
        self.assertEquals(my_list.size, 0)

    def test_insert_1_to_list(self):
        my_list = List()
        my_list.insert(1)
        self.assertEquals(my_list.size, 1)
        self.assertEquals(my_list.root.value, 1)
        self.assertEquals(my_list.root.next, None)

    def test_insert_2_and_3_to_list(self):
        my_list = List()
        my_list.insert(2)
        my_list.insert(3)
        self.assertEquals(my_list.size, 2)
        self.assertEquals(my_list.root.value, 2)
        self.assertEquals(my_list.root.next.value, 3)

    def test_query_empty_list(self):
        my_list = List()
        self.assertEquals(my_list.root, None)
        self.assertEquals(my_list.size, 0)
        self.assertEquals(my_list.query(10), False)

    def test_query_5_after_inserting_4_and_5_to_list(self):
        my_list = List()
        my_list.insert(4)
        my_list.insert(5)
        self.assertEquals(my_list.size, 2)
        self.assertEquals(my_list.root.value, 4)
        self.assertEquals(my_list.root.next.value, 5)
        self.assertEquals(my_list.query(5), my_list.root.next)

    def test_to_string(self):
        my_list = List()
        my_list.insert(0)
        my_list.insert(2)
        self.assertEquals(my_list.to_string(), "0 2")


class MoveToFrontListTestCase(unittest.TestCase):

    def test_query_8_after_inserting_8_to_list(self):
        my_list = MoveToFrontList()
        my_list.insert(8)
        self.assertEquals(my_list.root.value, 8)
        self.assertEquals(my_list.root.next, None)
        my_list.query(8)
        self.assertEquals(my_list.root.value, 8)

    def test_query_7_after_inserting_6_and_7_to_list(self):
        my_list = MoveToFrontList()
        my_list.insert(6)
        my_list.insert(7)
        self.assertEquals(my_list.root.value, 6)
        self.assertEquals(my_list.root.next.value, 7)
        my_list.query(7)
        self.assertEquals(my_list.root.value, 7)
        self.assertEquals(my_list.root.next.value, 6)

    def test_query_11_after_inserting_9_10_11_12_to_list(self):
        my_list = MoveToFrontList()
        my_list.insert(9)
        my_list.insert(10)
        my_list.insert(11)
        my_list.insert(12)
        self.assertEquals(my_list.root.value, 9)
        self.assertEquals(my_list.root.next.value, 10)
        self.assertEquals(my_list.root.next.next.value, 11)
        self.assertEquals(my_list.root.next.next.next.value, 12)
        my_list.query(11)
        self.assertEquals(my_list.root.value, 11)
        self.assertEquals(my_list.root.next.value, 9)
        self.assertEquals(my_list.root.next.next.value, 10)
        self.assertEquals(my_list.root.next.next.next.value, 12)


class MyStringTestCase(unittest.TestCase):

    def test_my_string_hash_0(self):
        s = MyString("")
        self.assertEquals(hash(s), 0)

    def test_my_string_hash_3_with_prime_5(self):
        s = MyString("a")
        s.prime_number = 5
        self.assertEquals(s.prime_number, 5)
        self.assertEquals(hash(s), 3)

    def test_my_string_hash_192651(self):
        MyString.prime_number = 280697
        s = MyString("abc")
        self.assertEquals(s.prime_number, 280697)
        self.assertEquals(hash(s), 192651)

    def test_getter_prime_number_not_none(self):
        s = MyString("seven")
        s.prime_number = 7
        self.assertEquals(s.prime_number, 7)


class HashEntryTestCase(unittest.TestCase):

    def test_hash_entry_constructor(self):
        hash_entry = HashEntry(1, "tati")
        self.assertEquals(hash_entry.key, 1)
        self.assertEquals(hash_entry.value_list, ["tati"])

    def test_append_jan_to_hash_entry(self):
        hash_entry = HashEntry(2, "tati")
        hash_entry.append("jan")
        self.assertEquals(hash_entry.key, 2)
        self.assertEquals(hash_entry.value_list, ["tati", "jan"])

    def test_query_exists_in_hash_entry(self):
        hash_entry = HashEntry(3, "lilian")
        hash_entry.append("nina")
        self.assertTrue(hash_entry.query("lilian"))
        self.assertTrue(hash_entry.query("nina"))

    def test_query_doesnt_exist_in_hash_entry(self):
        hash_entry = HashEntry(4, "roberto")
        self.assertFalse(hash_entry.query("onofre"))


class HashTableTestCase(unittest.TestCase):

    def test_construct_hash_table(self):
        table = HashTable(3)
        self.assertEquals(table.maximum, 3)
        self.assertEquals(table.array, [None, None, None])

    def test_append_hash_table(self):
        table = HashTable(3)
        self.assertEquals(table.maximum, 3)
        self.assertEquals(table.array, [None, None, None])

    def test_insert_abc_to_hash_table(self):
        table = HashTable(5)
        table.insert("abc")
        self.assertEquals(len(table.array[0].value_list), 1)

    def test_insert_a_d_to_hash_table(self):
        table = HashTable(5)
        table.insert("a")
        table.insert("d")
        self.assertEquals(len(table.array[3].value_list), 2)

    def test_query_android_in_empty_hash_table(self):
        table = HashTable(11)
        self.assertFalse(table.query("android"))

    def test_query_android_in_hash_table_that_contains_it(self):
        table = HashTable(11)
        table.insert("android")
        self.assertTrue(table.query("android"))

    def test_query_e_g_to_hash_table(self):
        table = HashTable(5)
        table.insert("e")
        table.insert("g")
        self.assertTrue(table.query("e"))
        self.assertTrue(table.query("g"))


class OptimalBinaryNodeTestCase(unittest.TestCase):

    def test_create_node(self):
        node = OptimalBinaryNode("balanoglosos", 0.5)
        self.assertEquals(node.value, "balanoglosos")
        self.assertEquals(node.probability, 0.5)
        self.assertEquals(node.depth, 0)
        self.assertEquals(node.cost, 1)


class OptimalBinarySearchTreeTestCase(unittest.TestCase):

    def test_contructor(self):
       tree = OptimalBinarySearchTree()
       self.assertEquals(tree.num_keys, 0)
       self.assertEquals(tree.keys, [])
       self.assertEquals(tree.probabilities, [])
       self.assertEquals(tree.dummy_probabilities, [1])

    def test_constructor(self):
        tree = OptimalBinarySearchTree()
        tree.num_keys = 5
        tree.keys = [0, 1, 2, 3, 4, 5]
        tree.probabilities = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
        tree.dummy_probabilities = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

        tree.construct_optimal_BST()

        self.assertEquals(tree.root.value, 2)
        self.assertEquals(tree.root.left.value, 1)
        self.assertEquals(tree.root.right.value, 5)
        self.assertEquals(tree.root.right.left.value, 4)
        self.assertEquals(tree.root.right.left.left.value, 3)


