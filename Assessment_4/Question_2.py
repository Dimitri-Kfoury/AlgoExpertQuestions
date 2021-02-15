def reverseAlternatingKNodes(head, k):

    i = 1
    first = head
    second = head
    previous = None
    alternate = True
    first_head = None

    while second:

        if i == 3 and alternate:
            alternate = False
            next_k = second.next
            second.next = None
            reversed_head = reverseLinkedList(first)
            first.next = next_k
            if previous:
                previous.next = reversed_head
            else:
                first_head = reversed_head
            previous = first
            first  = second = next_k
            i = 1
        if i == 3 and not alternate:
            alternate = True
            previous = second
            i = 1
            second = first = second.next

        if second:
            second = second.next
        i+=1

    if first:
        reversed_head = reverseLinkedList(first)
        previous.next = reversed_head
    return first_head




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


list = LinkedList(1)
list.next = LinkedList(2)
list.next.next = LinkedList(3)
list.next.next.next = LinkedList(4)
list.next.next.next.next = LinkedList(5)
list.next.next.next.next.next = LinkedList(6)
list.next.next.next.next.next.next = LinkedList(7)
list.next.next.next.next.next.next.next = LinkedList(8)
list.next.next.next.next.next.next.next.next = LinkedList(9)
list.next.next.next.next.next.next.next.next.next = LinkedList(10)
list.next.next.next.next.next.next.next.next.next.next = LinkedList(11)
list.next.next.next.next.next.next.next.next.next.next.next = LinkedList(12)
list.next.next.next.next.next.next.next.next.next.next.next.next = LinkedList(13)
list.next.next.next.next.next.next.next.next.next.next.next.next.next = LinkedList(14)
print(reverseAlternatingKNodes(list,3).next.next.next.next.next.next.next.next.next.next.next.next.next.next.value)
