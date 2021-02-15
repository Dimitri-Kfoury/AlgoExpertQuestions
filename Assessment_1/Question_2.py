def invertedBisection(head):
    slow_node = head
    fast_node = head
    even = False

    if not head.next:
        return head

    while fast_node:
        if fast_node.next:
            if fast_node.next.next:
                fast_node = fast_node.next.next
                slow_node = slow_node.next
            else:
                even = True
                break
        else:
            break
    if even:
        second_half_head = slow_node.next
        slow_node.next = None
        first_half_head = reverseLinkedList(head)
        second_half_head = reverseLinkedList(second_half_head)
        head.next = second_half_head
        return first_half_head
    else:
        second_half_head = slow_node.next
        slow_node.next = None
        first_half_head = reverseLinkedList(head)
        second_half_head = reverseLinkedList(second_half_head)
        new_first_half_head = first_half_head.next
        first_half_head.next = second_half_head
        head.next = first_half_head
        return new_first_half_head




# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


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


head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)
head.next.next.next.next.next.next = LinkedList(6)

result = invertedBisection(head)

print(result.value)