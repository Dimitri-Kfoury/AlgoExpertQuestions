def shiftLinkedList(head, k):

    iterator_node = head
    length = 1
    while iterator_node.next is not None:
        iterator_node = iterator_node.next
        length += 1

    tail = iterator_node

    iterator_node = head

    if k > length:
        k = k % length

    for i in range(1, length - k):
        iterator_node = iterator_node.next
    new_tail = iterator_node

    tail.next = head

    if new_tail.next is not None:
        new_head = new_tail.next
        new_tail.next = None

    return new_head


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
