'''
    A Python class that represents an individual node 
    in a Binary Tree
'''


class Node:
    '''
        Represents a Node
    '''
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def min_value_node(root):
    '''
        returns the min value from a tree
    '''
    current = root
    while current.left:
        current = current.left

    return current.val


def inorder_traversal(root):
    '''
        stores inorder of root
    '''
    if root:
        inorder_traversal(root.left)
        print root.val
        inorder_traversal(root.right)


def preorder_traversal(root):
    '''
        stores inorder of root
    '''
    if root:
        print root.val
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    '''
        stores inorder of root
    '''
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print root.val


def search(root, key):
    '''
        searches a key in binary search tree
    '''
    if key == root.val or not root:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def insert(root, key):
    '''
        inserts a key in binary search tree
    '''
    if root is None:
        root = Node(key)
    else:
        if root.val < key:
            if root.right is None:
                root.right = Node(key)
            else:
                insert(root.right, key)
        else:
            if root.left is None:
                root.left = Node(key)
            else:
                insert(root.left, key)


def delete(root, key):
    '''
        inserts a key in binary search tree
    '''
    if root is None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.right is None:
            temp = root.left
            root = None
            return temp
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


if __name__ == "__main__":
    r = Node(50)
    insert(r, 30)
    insert(r, 70)
    insert(r, 20)
    insert(r, 40)
    insert(r, 45)
    # insert(r, 80)

    # print "Inorder Traversal"
    # inorder_traversal(r)
    # print "Preorder Traversal"
    # preorder_traversal(r)
    print "Postrder Traversal"
    postorder_traversal(r)

    # delete(r, 40)
    # inorder_traversal(r)
