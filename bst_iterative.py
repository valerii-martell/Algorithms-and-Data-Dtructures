class BST:
    nodes = []
    root = None

    class Node():
        def __init__(self, parent, left, right, key, value=None):
            self.parent = parent
            self.left = left
            self.right = right
            self.key = key
            self.value = value

    def insert(self, key, value=None):
        if not self.root:
            self.root = self.Node(None, None, None, key, value)
        else:
            if self.root.key == key:
                raise KeyError
            else:
                prev = None
                temp = self.root
                while temp:
                    prev = temp
                    if temp.key > key:
                        temp = temp.left
                    else:
                        temp = temp.right
                if prev.key > key:
                    prev.left = self.Node(prev, None, None, key, value)
                else:
                    prev.right = self.Node(prev, None, None, key, value)

    def select(self, key):
        temp = self.root
        while temp:
            if temp.key == key:
                return temp
            elif temp.key > key:
                temp = temp.left
            elif temp.key < key:
                temp = temp.right
            else:
                return None


    def get_min(self, root=None):
        if not root:
            root = self.root
        temp = root
        while temp.left:
            temp = temp.left
        return temp

    def get_max(self, root=None):
        if not root:
            root = self.root
        temp = root
        while temp.right:
            temp = temp.right
        return temp

    def delete(self, key):

        def _fix_parent(node, new=None):
            if node.parent.left and node.parent.left.key == key:
                node.parent.left = new
            elif node.parent.right and node.parent.right.key == key:
                node.parent.right = new

        node = self.select(key)
        if node:
            if not node.left and not node.right:
                _fix_parent(node)
            elif node.left and node.right:
                right_min = self.get_min(node.right)

                _fix_parent(right_min)
                _fix_parent(node, right_min)
            elif node.left and not node.right:
                _fix_parent(node, node.left)
            elif node.right and not node.left:
                _fix_parent(node, node.right)

            node.parent = None
            del node
        else:
            raise KeyError

    def inorder(self):
        temp = self.root
        stack, result = [], []
        while temp or len(stack) > 0:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                result.append(temp.key)
                temp = temp.right
        return result
