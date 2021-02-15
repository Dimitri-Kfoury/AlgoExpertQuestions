def largestBstSize(tree):
    return get_largest_trees(tree)[0]



# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_BST(binary_tree, min, max):
    if not binary_tree:
        return True

    if binary_tree.left and (binary_tree.left.value >= binary_tree.value or binary_tree.left.value < min) :
        return False

    if binary_tree.right and (binary_tree.right.value < binary_tree.value or binary_tree.right.value >= max):
        return False

    return is_valid_BST(binary_tree.left, min, binary_tree.value) and is_valid_BST(binary_tree.right, binary_tree.value,max)


def inOrderTraverse(tree, array):
    if tree is None:
        return
    else:
        inOrderTraverse(tree.left, array)
        array[0] += 1
        inOrderTraverse(tree.right, array)
    return array

def get_largest_trees(tree):

    if tree is None:
        return 1

    if is_valid_BST(tree,float('-inf'), float('inf')):
        return inOrderTraverse(tree,array=[0])
    else:
        return [max(get_largest_trees(tree.left)[0],get_largest_trees(tree.right)[0])]



b_tree = BinaryTree(7)
b_tree.left = BinaryTree(0)
b_tree.right = BinaryTree(8)
b_tree.right.right = BinaryTree(9)
b_tree.right.left = BinaryTree(7)

lol_tree = BinaryTree(20)
lol_tree.left = b_tree

lol_tree.right =BinaryTree(10)
lol_tree.right.left =BinaryTree(5)
lol_tree.right.left.left =BinaryTree(6)
lol_tree.right.left.right =BinaryTree(5)
lol_tree.right.left.left.left =BinaryTree(1)
lol_tree.right.right =BinaryTree(15)
lol_tree.right.right.right =BinaryTree(22)
lol_tree.right.right.left =BinaryTree(13)
lol_tree.right.right.left.right =BinaryTree(14)


print(get_largest_trees(lol_tree)[0])