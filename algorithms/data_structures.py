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

    @property
    def depth(self):
        return self.depth_from_node(self.root)

    def depth_from_node(self, node):
        if node is None:
            return 0
        else:
            ldepth = self.depth_from_node(node.left)
            rdepth = self.depth_from_node(node.right)
            return max(ldepth, rdepth) + 1

    def insert(self, value):
        self.root = self.insert_node(self.root, value)
        self.size += 1

    def insert_node(self, root, value):
        if root is None:
            return Node(value)
        elif root.value > value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)
        return root

    @property
    def max(self):
        return self.max_from_node(self.root)

    def max_from_node(self, node):
        if node is None:
            return False
        while node.right is not None:
            node = node.right
        return node

    @property
    def min(self):
        return self.min_from_node(self.root)

    def min_from_node(self, node):
        if node is None:
            return False
        while node.left is not None:
            node = node.left
        return node

    def predecessor(self, node):
        return self.max_from_node(node.left)

    def to_string(self, node):
        output_string = ""
        depth = self.depth_from_node(node)
        nodes_in_level = [node]

        for level in xrange(depth):
            next_level_items = []
            n_spaces = 2**(depth-level-1) - 1
            current_line = n_spaces * " "
            n_spaces =  2**(depth-level) - 1
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
                        next_level_items.append(Node(0))
            output_string = "\n".join([output_string, current_line.rstrip()])
            nodes_in_level = next_level_items
        return output_string

    def query(self, value):
        return self.query_from_node(value, self.root)

    def query_from_node(self, value, node):
        if node is None:
            return False
        elif node.value == value:
            return node
        elif node.value > value:
            return self.query_from_node(value, node.left)
        else:
            return self.query_from_node(value, node.right)

    def remove(self, value):
        node = self.query(value)
        if node == False:
            return False
        else:
            self.root = self.remove_node(value)
            return self.root

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
