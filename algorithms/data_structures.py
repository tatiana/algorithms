class Node(object):

    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


class Tree(object):

    def __init__(self):
        self.root = None
        self.size = 0


class BinarySearchTree(Tree):

    def __init__(self):
        self.root = None
        self.size = 0

    def insert_node(self, root, value):
        if root is None:
            return Node(value)
        elif root.value > value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)
        return root

    def insert(self, value):
        self.root = self.insert_node(self.root, value)
        self.size += 1

    def lookup(self, value, node='root'):
        if node == 'root':
            node = self.root
        if node is None:
            return False
        elif node.value == value:
            return node
        elif node.value > value:
            return self.lookup(value, node.left)
        else:
            return self.lookup(value, node.right)

    def depth(self, node='root'):
        if node == 'root':
            node = self.root
        if node is None:
            return 0
        else:
            ldepth = self.depth(node.left)
            rdepth = self.depth(node.right)
            return max(ldepth, rdepth) + 1

# TODO:
# - convert depth to property
# - check if there isn't a best way of function default value use object attribute
