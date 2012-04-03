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

    def depth(self, node='root'):
        if node == 'root':
            node = self.root
        if node is None:
            return 0
        else:
            ldepth = self.depth(node.left)
            rdepth = self.depth(node.right)
            return max(ldepth, rdepth) + 1

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

    def max(self, node='root'):
        # FIXME: recursion
        if node == 'root':
            node = self.root
        if node is None:
            return False
        while node.right is not None:
            node = node.right
        return node

    def min(self, node='root'):
        # FIXME: recursion
        if node == 'root':
            node = self.root
        if node is None:
            return False
        while node.left is not None:
            node = node.left
        return node

    def query(self, value, node='root'):
        if node == 'root':
            node = self.root
        if node is None:
            return False
        elif node.value == value:
            return node
        elif node.value > value:
            return self.query(value, node.left)
        else:
            return self.query(value, node.right)

    def predecessor(self, node):
        return self.max(node.left)

    def remove_node(self, value, node='root'):
        if node == 'root':
            node = self.root

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

    def remove(self, value):
        node = self.query(value)
        if node == False:
            return False
        else:
            self.root = self.remove_node(value)
            return self.root



# TODO:
# - convert depth to property
# - check if there isn't a best way of function default value use object attribute
