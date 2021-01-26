# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.cache = {}
        self.recents = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):

        if not self.cache.__contains__(key):
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
                self.currentSize -= 1
            self.currentSize += 1
            newNode = Node(key, value)
            self.recents.setHead(newNode)
            self.cache[key] = newNode
        else:
            self.cache[key].value = value
            self.recents.setHead(self.cache[key])

    def evictLeastRecent(self):
        keyToRemove = self.recents.tail.key
        del self.cache[keyToRemove]
        self.recents.remove(self.recents.tail)

    def getValueFromKey(self, key):
        value = self.cache[key].value
        self.recents.setHead(self.cache[key])
        return value

    def getMostRecentKey(self):
        return self.recents.head.key


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):

        if nodeToInsert is None or (
                nodeToInsert == self.head and nodeToInsert == self.tail) or nodeToInsert == node:
            return
        if node is None:
            self.setHead(nodeToInsert)
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        node.prev = nodeToInsert
        nodeToInsert.next = node

        if nodeToInsert.prev is None:
            self.head = nodeToInsert
        else:
            nodeToInsert.prev.next = nodeToInsert
        return

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is None or (
                nodeToInsert == self.head and nodeToInsert == self.tail) or nodeToInsert == node:
            return
        if node is None:
            self.setHead(nodeToInsert)
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node

        nodeToInsert.next = node.next

        if nodeToInsert.next is None:
            self.tail = nodeToInsert
        else:
            nodeToInsert.next.prev = nodeToInsert
        node.next = nodeToInsert
        return

    def insertAtPosition(self, position, nodeToInsert):

        if position < 1 or nodeToInsert is None:
            return

        node = self.head
        if position == 1:
            self.insertBefore(node, nodeToInsert)
            return
        for i in range(2, position):
            node = node.next
            if node is None:
                return
        if node is None:
            return
        self.insertAfter(node, nodeToInsert)

    def removeNodesWithValue(self, value):

        currentNode = self.head

        while currentNode is not None:

            if currentNode.value == value:
                nodeToRemove = currentNode
                currentNode = currentNode.next
                self.remove(nodeToRemove)
                continue
            currentNode = currentNode.next

        return

    def remove(self, node):

        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        removeBindings(node)
        return

    def containsNodeWithValue(self, value):

        currentNode = self.head

        while currentNode is not None:
            if currentNode.value == value:
                return True
            currentNode = currentNode.next
        return False


def removeBindings(node):
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev
    node.next = None
    node.prev = None


class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None
