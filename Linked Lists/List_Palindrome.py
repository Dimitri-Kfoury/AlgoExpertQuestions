# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    current_node = head
    counter = 0
    while current_node:
        current_node = current_node.next
        counter += 1

    if counter == 1:
        return True
    middle = counter // 2

    i = 0
    first_half_tail = head
    while i < middle - 1:
        first_half_tail = first_half_tail.next
        i += 1

    if counter % 2 == 0:
        second_half_head = first_half_tail.next
        first_half_tail.next = None
    else:
        second_half_head = first_half_tail.next.next
        first_half_tail.next.next = None
        first_half_tail.next = None

    second_half_head = reverseLinkedList(second_half_head)
    first = head
    second = second_half_head
    while first and second:
        if first.value != second.value:
            return False
        first = first.next
        second = second.next
    return True


def reverseLinkedList(head):
    first = head
    second = first.next
    if second:
        third = head.next.next
    first.next = None

    while second:
        third = second.next
        second.next = first
        first = second
        second = third
    return first

