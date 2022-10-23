class Node:
    def __init__(self, key, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.count = 1


def insert(root, key, parent=None):
    if not root:
        return Node(key, parent)
    else:
        if root.key == key:
            root.count += 1
            return root
        elif root.key > key:
            root.left = insert(root.left, key, root)
        else:
            root.right = insert(root.right, key, root)
    return root


def inorder(root):
    result = []

    def _inorder(root):
        if root:
            if root.left:
                _inorder(root.left)
            for i in range(0, root.count):
                result.append(root.key)
            if root.right:
                _inorder(root.right)

    _inorder(root)
    return result


def get_min(root):
    if not root.left:
        return root
    else:
        return get_min(root.left)


def get_max(root):
    if not root.right:
        return root
    else:
        return get_max(root.right)


def delete(root, key):
    def _fix_parent(node, new=None):
        if node.parent.left and node.parent.left.key == key:
            node.parent.left = new
        elif node.parent.right and node.parent.right.key == key:
            node.parent.right = new

    node = select(root, key)
    if node:
        if node.count > 1:
            node.count -= 1
        else:
            if not node.left and not node.right:
                _fix_parent(node)
            elif node.left and node.right:
                right_min = get_min(node.right)

                _fix_parent(right_min)
                _fix_parent(node, right_min)

                right_min.parent = node.parent
            elif node.left and not node.right:
                _fix_parent(node, node.left)
            elif node.right and not node.left:
                _fix_parent(node, node.right)
            node.parent = None
            del node

    return root


def select(root, key):
    if root:
        if root.key == key:
            return root
        elif root.key > key:
            return select(root.left, key)
        else:
            return select(root.right, key)
    else:
        return None

