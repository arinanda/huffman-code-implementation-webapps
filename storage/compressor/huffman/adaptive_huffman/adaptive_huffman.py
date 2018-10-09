from common.util import Node


def insert_node(null, char):
    char_node = Node(char, 1)
    empty_node = Node(parent=null.parent, left=null, right=char_node)
    char_node.parent = empty_node
    if null.parent:
        if null is null.parent.left:
            null.parent.left = empty_node
        else:
            null.parent.right = empty_node
    null.parent = empty_node
    return char_node


def get_code(node):
    code = str()
    while node.parent is not None:
        if node.parent.left is node:
            code = '0' + code
        else:
            code = '1' + code
        node = node.parent
    return '0' + code


def swap(a, b):
    if a and b:
        if a.value > b.value:
            if a.parent.left is a:
                a.parent.left = b
            else:
                a.parent.right = b

            if b.parent.left is b:
                b.parent.left = a
            else:
                b.parent.right = a
            a.parent, b.parent = b.parent, a.parent


def update_tree(root):
    while root:
        if root.parent:
            sibling = root.parent.right if root.parent.left is root else root.parent.left
            swap(root.left, sibling)
            swap(root.right, sibling)
        swap(root.left, root.right)
        if root.left and root.right:
            root.value = root.left.value + root.right.value
        root = root.parent


def print_tree(root, space=0):
    if space == 0:
        print('\n\n')
    if root:
        print('%s%s' % (' ' * space, str(root)))
        print_tree(root.left, space+2)
        print_tree(root.right, space+2)
