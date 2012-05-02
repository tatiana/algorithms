# TODO: Integrate with Sphinx, for API generation
# TODO: Analyse by_node methods
# TODO: ROOT_REFERENCE = 0, 1 # height, etc
# TODO: Add depth attrib to Node, so depth_from_node doesn't need
# to be called
from algorithms.utils import isprime

class BinaryNode(object):

    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
        self.depth = 0

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


class Tree(object):

    def __init__(self):
        self.root = None
        self.size = 0


class BinarySearchTree(Tree):
    """
    Binary search tree (BST), also known as ordered or sorted binary tree. It
    is a node-based binary tree data structure which has the following
    properties:
        - The left subtree of a node contains only nodes with keys less than
        the node's key.
        - The right subtree of a node contains only nodes with keys greater
        than the node's key.
        - Both the left and right subtrees must also be binary search trees.

    Example of a BST containing three nodes:
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)

    Builds the following tree:
          2      # root
        1   3    # leafs
    """

    def __init__(self):
        self.root = None
        self.size = 0

    @property
    def height(self):
        """
        Return the number of links from the root node to the deepest node.
        """
        return self.depth_from_node(self.root)

    def depth_from_node(self, node):
        """
        Return the number of links from the given @node to the deepest node.
        """
        if node is None:
            return 0
        else:
            lheight = self.depth_from_node(node.left)
            rheight = self.depth_from_node(node.right)
            return max(lheight, rheight) + 1

    def insert(self, value):
        """
        Create a node with @value and add it from the root of the tree.
        """
        self.root = self.insert_node(self.root, value)
        self.size += 1

    def insert_list(self, values_list):
        for value in values_list:
            self.insert(value)

    def insert_node(self, root, value):
        """
        Create a node with @value and add it to the subtree of a given @root.
        """
        if root is None:
            return BinaryNode(value)
        elif root.value > value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)
        return root

    @property
    def max(self):
        """
        Retrieve node with maximum value.
        """
        return self.max_from_node(self.root)

    def max_from_node(self, node):
        """
        Retrieve node with maximum value from the subtree where @node is root.
        """
        if node is None:
            return False
        while node.right is not None:
            node = node.right
        return node

    @property
    def min(self):
        """
        Retrieve node with minimum value.
        """
        return self.min_from_node(self.root)

    def min_from_node(self, node):
        """
        Retrieve node with minimum value from the subtree where @node is root.
        """
        if node is None:
            return False
        while node.left is not None:
            node = node.left
        return node

    def predecessor(self, node):
        """
        Find the node which preceeds the given @node, based on the ordering
        (this corresponds to return the rightmost node from the left subtree).
        """
        return self.max_from_node(node.left)

    def query(self, value):
        """
        Retrieve a node with the @value from the root of the tree. If not
        found, return False.

        Note: Implemented using depth first search (DFS).
        """
        return self.query_from_node(value, self.root)

    def query_from_node(self, value, node):
        """
        Retrieve a node with the @value from the @node subtree. If not found,
        return False.

        Note: Implemented using depth first search (DFS).
        """
        if node is None:
            return False
        elif node.value == value:
            return node
        elif node.value > value:
            return self.query_from_node(value, node.left)
        else:
            return self.query_from_node(value, node.right)

    def remove(self, value):
        """
        Remove node with @value, searching from the tree root. If not found,
        return False.
        """
        node = self.query(value)
        if node is False:
            return False
        else:
            self.root = self.remove_node(value, self.root)
            return self.root

    def remove_node(self, value, node):
        """
        Remove node with @value, searching from  @node subtree. If not found,
        return False.
        """
        if node.value == value:
            if (node.left is None) and (node.right is None):
                self.size -= 1
                return None
            elif (node.left is None):
                self.size -= 1
                return node.right
            elif (node.right is None):
                self.size -= 1
                return node.left
            else:
                predecessor = self.predecessor(node)
                node.value = predecessor.value
                predecessor.value = value
                node.left = self.remove_node(value, node.left)
        elif node.value > value:
            node.left = self.remove_node(value, node.left)
        else:
            node.right = self.remove_node(value, node.right)

        return node

    def retrieve_parent(self, node, subtree):
        if node is None or node.value == subtree.value:
            return None
        else:
            if node.value > subtree.value:
                if node.value == subtree.left.value:
                    return subtree
                else:
                    return self.retrieve_parent(node, node.left)
            else:
                if node.value == subtree.right.value:
                    return subtree
                else:
                    return self.retrieve_parent(node, node.right)

    def to_string(self, node):
        """
        Return a string that represents graphically the sub-tree, considering
        @node as root.

        Example of string returned:
        '   4
          2   6
         1 3 5 7'
        """
        output_string = ""
        height = self.depth_from_node(node)
        nodes_in_level = [node]

        for level in xrange(height):
            next_level_items = []
            n_spaces = 2 ** (height - level - 1) - 1
            current_line = n_spaces * " "
            n_spaces = 2 ** (height - level) - 1
            middle_spaces = n_spaces * " "

            for item in nodes_in_level:
                if item.value:
                    current_line = "%s%d%s" % (current_line, item.value, middle_spaces)
                else:
                    current_line = "%s %s" % (current_line, middle_spaces)
                for son in [item.left, item.right]:
                    if son is not None:
                        next_level_items.append(son)
                    else:
                        next_level_items.append(BinaryNode(0))
            output_string = "\n".join([output_string, current_line.rstrip()])
            nodes_in_level = next_level_items
        return output_string


class AVLTree(BinarySearchTree):
    """
    Based on Adelson-Velskii and Landis proposal for Balanced Search Trees.
    If insertion or deletion get the tree out of balance, then we fix it
    immediatelly.
    """

    def is_balanced(self):
        is_balanced, factor = self.is_subtree_balanced(self.root)
        return is_balanced

    def is_subtree_balanced(self, node):
        if node is None:
            return True, 0
        else:
            left_depth = self.depth_from_node(node.left)
            right_depth = self.depth_from_node(node.right)
            delta = left_depth - right_depth
            if abs(delta) > 1:
                return False, delta
            else:
                is_left_balanced, factor = self.is_subtree_balanced(node.left)
                if not is_left_balanced:
                    return False, factor
                else:
                    is_right_balanced, factor = self.is_subtree_balanced(node.right)
                    if not is_right_balanced:
                        return False, factor
                return True, delta

    def _return_unbalanced_node(self, node):
        if node is None:
            return None, 0
        else:
            left_depth = self.depth_from_node(node.left)
            right_depth = self.depth_from_node(node.right)
            delta = left_depth - right_depth
            if abs(delta) > 1:
                return node, delta
            else:
                if not self.is_subtree_balanced(node.left):
                    return node.left
                elif not self.is_subtree_balanced(node.right):
                    return node.right
            return None, delta

    def _rotate_left(self, old_parent):
        new_parent = old_parent.right
        old_parent.right = new_parent.left
        new_parent.left = old_parent
        return new_parent

    def _rotate_right(self, old_parent):
        new_parent = old_parent.left
        old_parent.left = new_parent.right
        new_parent.right = old_parent
        return new_parent

    def _balance_tree(self, root):
        unbalanced_node, factor = self._return_unbalanced_node(root)
        if unbalanced_node is None:
            return root
        else:
            parent_unbalanced = self.retrieve_parent(unbalanced_node, root)
            if (factor == 2):
                left_left_depth = self.depth_from_node(unbalanced_node.left.left)
                left_right_depth = self.depth_from_node(unbalanced_node.left.right)
                delta = left_left_depth - left_right_depth
                if delta == 1:
                    new_root = self._rotate_right(unbalanced_node)
                else:
                    unbalanced_node.left = self._rotate_left(unbalanced_node.left)
                    new_root = self._rotate_right(unbalanced_node)
            elif (factor == -2):
                right_left_depth = self.depth_from_node(unbalanced_node.right.left)
                right_right_depth = self.depth_from_node(unbalanced_node.right.right)
                delta = right_left_depth - right_right_depth
                if delta == -1:
                    new_root = self._rotate_left(unbalanced_node)
                else:
                    unbalanced_node.right = self._rotate_right(unbalanced_node.right)
                    new_root = self._rotate_left(unbalanced_node)

            if parent_unbalanced is None:
                root = new_root
            elif unbalanced_node.value == parent_unbalanced.left.value:
                parent_unbalanced.left = new_root
            else:
                parent_unbalanced.right = new_root

    def insert_node(self, root, value):
        root = super(AVLTree, self).insert_node(root, value)
        root = self._balance_tree(root)
        return root

    def remove_node(self, root, value):
        root = super(AVLTree, self).remove_node(root, value)
        root = self._balance_tree(root)
        return root


class ListItem(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class List(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if not self.query(value):
            self.root = self.insert_item(self.root, value)
            self.size += 1

    def insert_item(self, item, value):
        """
        Create an item with @value and add it to the end of the list.
        """
        if item is None:
            return ListItem(value)
        else:
            item.next = self.insert_item(item.next, value)
        return item

    def query(self, value):
        """
        Retrieve a node with the @value from the root of the tree. If not
        found, return False.

        Note: Implemented using depth first search (DFS).
        """
        return self.query_from_item(value, self.root)

    def query_from_item(self, value, item):
        if item is None:
            return False
        elif item.value == value:
            return item
        else:
            return self.query_from_item(value, item.next)
        #while item is not None:
        #    if item.value == value:
        #        return item
        #    item = item.next
        #return False

    def to_string(self):
        string = ""
        item = self.root
        while item is not None:
            string = " ".join([string, str(item.value)])
            item = item.next
        return string.strip()

#class MoveToFrontList(list):
#
#    def __getitem__(self, index):
#        self.insert(0, self.pop(index))
#        return super(MoveToFrontList, self).__getitem__(0)


class MoveToFrontList(List):

    def query(self, value):
        previous_node = self.query_from_item(value, self.root)
        if isinstance(previous_node, ListItem):
            new_root = previous_node.next
            previous_node.next = new_root.next
            new_root.next = self.root
            self.root = new_root
            return new_root
        elif previous_node:
            return self.root
        else:
            return False

    def query_from_item(self, value, item):
        if item is None:
            return False
        elif item.value == value:
            return True
        else:
            previous_item = self.query_from_item(value, item.next)
            if isinstance(previous_item, ListItem):
                return previous_item
            elif previous_item:
                return item


#PRIME_NUMBER = 766109 # total of 766108 words in the file bible.txt
PRIME_NUMBER = 280697 # total of 280685 words in the file world192.txt

def c_mul(a, b):
    return eval(hex((long(a) * b) & 0xFFFFFFFFL)[:-1])

class MyString(str):

    _prime_number = None

    @property
    def prime_number(self):
        if self._prime_number is None:
            return PRIME_NUMBER
        else:
            return self._prime_number

    @prime_number.setter
    def prime_number(self, value):
        if isprime(value):
            self._prime_number = value

    def __hash__(self):
        if not self:
            return 0
        value = ord(self[0]) << 7
        for char in self:
            value = c_mul(1000003, value) ^ ord(char)
        # value = value ^ len(self)
        value = value % self.prime_number
        return value


class HashEntry(object):

    def __init__(self, key, value):
        self.key = key
        self.value_list = [value]

    def append(self, value):
        if not self.query(value):
            self.value_list.append(value)

    def query(self, value):
        return value in self.value_list


class HashTable(object):

    def __init__(self, maximum = PRIME_NUMBER):
        self.maximum = maximum
        self.array = [None for i in xrange(maximum)]
        MyString.prime_number = maximum

    def insert(self, string):
        string = MyString(string)
        index = hash(string)
        if self.array[index] is None:
            self.array[index] = HashEntry(index, string)
        else:
            hash_entry = self.array[index]
            hash_entry.append(string)

    def query(self, string):
        string = MyString(string)
        index = hash(string)
        entry = self.array[index]
        if entry is not None:
            return self.array[index].query(string)
        return False


class OptimalBinaryNode(BinaryNode):

    def __init__(self, value, probability = 0):
        super(OptimalBinaryNode, self).__init__(value)
        self.probability = probability

    @property
    def cost(self):
        return self.depth + 1


class OptimalBinarySearchTree(BinarySearchTree):
    def __init__(self):
        super(OptimalBinarySearchTree, self).__init__()
        self.num_keys = 0
        self.keys = []
        self.probabilities = []
        self.dummy_probabilities = [1]

    def optimal_BST(self):
        n = len(self.keys) + 1
        root_matrix = [[0 for i in xrange(n)] for j in xrange(n)]
        probabilities_sum_matrix = [[0 for i in xrange(n)] for j in xrange(n)]
        expected_cost_matrix = [[99999 for i in xrange(n)] for j in xrange(n)]
        for i in xrange(1, n):
            probabilities_sum_matrix[i][i-1] = self.dummy_probabilities[i - 1]
            expected_cost_matrix[i][i-1] = self.dummy_probabilities[i - 1]

        for l in xrange(1, n):
            for i in xrange(1, n - l):
                j = i + l - 1
                expected_cost_matrix[i][j] = 99999
                probabilities_sum_matrix[i][j] = probabilities_sum_matrix[i][j - 1] + self.probabilities[j] + self.dummy_probabilities[j]
                for r in xrange(i, j + 1):
                    t = expected_cost_matrix[i][r - 1] + expected_cost_matrix[r+1][j] + probabilities_sum_matrix[i][j]
                    if t < expected_cost_matrix[i][j]:
                        expected_cost_matrix[i][j] = t
                        root_matrix[i][j] = r
        return root_matrix

    def construct_optimal_BST(self):
        root = self.optimal_BST()
        n = self.num_keys
        r = root[1][n]
        value = self.keys[r]
        self.insert(value)
        self.construct_optimal_subtree(1, r-1, r, "left", root)
        self.construct_optimal_subtree(r+1, n, r, "right", root)

    def construct_optimal_subtree(self, i, j, r, direction, root):
        if i <= j:
            t = root[i][j]
            value = self.keys[t]
            self.insert(value)
            self.construct_optimal_subtree(i, t-1, t, "left", root)
            self.construct_optimal_subtree(t+1, j, t, "right", root)

