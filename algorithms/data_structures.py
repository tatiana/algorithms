# TODO: Integrate with Sphinx

class BinaryNode(object):

    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


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
            n_spaces = 2**(height-level-1) - 1
            current_line = n_spaces * " "
            n_spaces =  2**(height-level) - 1
            middle_spaces = n_spaces * " "

            for item in nodes_in_level:
                if item.value:
                    current_line = "%s%d%s"%(current_line, item.value, middle_spaces)
                else:
                    current_line  = "%s %s"% (current_line, middle_spaces)
                for son in [item.left, item.right]:
                    if son is not None:
                        next_level_items.append(son)
                    else:
                        next_level_items.append(BinaryNode(0))
            output_string = "\n".join([output_string, current_line.rstrip()])
            nodes_in_level = next_level_items
        return output_string

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
        if node == False:
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
