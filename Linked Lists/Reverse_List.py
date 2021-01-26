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
