def minHeightBst(array):
    return constructBST(None, 0, len(array), array)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def constructBST(bst, startIdx, endIdx, array):
    if startIdx > endIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    constructBST(bst, startIdx, midIdx - 1, array)
    constructBST(bst, midIdx + 1, endIdx, array)
    return bst
