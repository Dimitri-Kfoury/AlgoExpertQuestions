def subtreesWithinRange(tree, targetRange):
    total_number = [0]

    helper(tree,targetRange,total_number)
    return total_number[0]


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def number_in_range(number, range):

    print(number)
    return range[0] <= number <= range[1]


def helper(node, target_range, total_number):
    if node is None:
        return True

    else:
        is_valid_number  =  number_in_range(node.value, target_range)
        left_is_valid = helper(node.left, target_range,total_number)
        right_is_valid = helper(node.right, target_range,total_number)

        if is_valid_number and left_is_valid and right_is_valid:
            total_number[0] += 1
            return True
        return False





bst = BST(5)
bst.left = BST(2)
bst.left.left = BST(1)
bst.right = BST(8)
bst.right.left = BST(5)
bst.right.right = BST(9)

total_number = [0]
helper(bst,[5,15],total_number)
print(total_number)
