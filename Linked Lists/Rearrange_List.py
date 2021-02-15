def rearrangeLinkedList(head, k):
    first_head = first_tail = second_head = second_tail = third_head = third_tail = None
    current_node = head
    while current_node:
        if current_node.value < k:
            if first_head is None:
                first_head = first_tail = current_node
            else:
                first_tail.next = current_node
                first_tail = current_node
        elif current_node.value > k:
            if third_head is None:
                third_head = third_tail = current_node
            else:
                third_tail.next = current_node
                third_tail = current_node
        else:
            if second_head is None:
                second_head = second_tail = current_node
            else:
                second_tail.next = current_node
                second_tail = current_node

        current_node = current_node.next
    return reconstruct_list(first_head, first_tail, second_head, second_tail, third_head, third_tail)



# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reconstruct_list(first_head, first_tail, second_head, second_tail, third_head, third_tail):
    if first_head:
        if second_head:
            first_tail.next = second_head
            if third_head:
                second_tail.next = third_head
                third_tail.next = None
                return first_head
            second_tail.next = None
            return first_head
        elif third_head:
            first_tail.next = third_head
            third_tail.next = None
            return first_head
        return first_head
    elif second_head:
        if third_head:
            second_tail.next = third_head
            third_tail.next = None
        return second_head
    return third_head


