def rightSmallerThan(array):

    bst = None

    for i in range(len(array) - 1, -1, -1):
        if bst is None:
            bst = BST(array[i])
            array[i] = 0
        else:
            bst.insert(array[i], i, array, 0)
    return array


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.leftSize = 0

    def insert(self, value, idx, outputArray, numSmaller):
        if value < self.value:
            self.leftSize = self.leftSize + 1
            if self.left is None:
                self.left = BST(value)
                outputArray[idx] = numSmaller
            else:
                self.left.insert(value, idx, outputArray, numSmaller)
        else:

            numSmaller += self.leftSize
            if value > self.value:
                numSmaller += 1
            if self.right is None:
                self.right = BST(value)
                outputArray[idx] = numSmaller
            else:
                self.right.insert(value, idx, outputArray, numSmaller)


