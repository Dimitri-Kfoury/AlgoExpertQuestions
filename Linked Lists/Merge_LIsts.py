# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    first = headOne
    second = headTwo
    if first.value < second.value:
        final = first
    else:
        final = second

    while first and second:
        if first.value > second.value:
            temp = second.next
            if second.next:
                if second.next.value >= first.value:
                    second.next = first
            else: second.next = first
            second = temp
        else:
            temp = first.next
            if first.next:
                if first.next.value >= second.value:
                    first.next = second
            else:
                first.next = second
            first = temp

    return final

