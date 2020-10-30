# O(N) time | O(1) space


def rearrangeLinkedList(head, k):

    smallerListHead = None
    smallerListTail = None
    equalListHead = None
    equalListTail = None
    greaterListHead = None
    greaterListTail = None

    node = head
    while node is not None:
        if node.value < k:
            smallerListHead, smallerListTail = growLinkedList(
                smallerListHead, smallerListTail, node
            )
        elif node.value > k:
            greaterListHead, greaterListTail = growLinkedList(
                greaterListHead, greaterListTail, node
            )
        else:
            equalListHead, equalListTail = growLinkedList(
                equalListHead, equalListTail, node
            )
        previous = node
        node = node.next
        previous.next = None
    firstHead, firstTail = connectLinkkedLists(
        smallerListHead, smallerListTail, equalListHead, equalListTail
    )
    finalHead, _ = connectLinkkedLists(
        firstHead, firstTail, greaterListHead, greaterListTail
    )


def growLinkedList(head, tail, node):
    newHead = head
    newTail = node
    if newHead is None:
        newHead = node
    if tail is not None:
        tail.next = node
    return (newHead, newTail)


def connectLinkkedLists(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailOne

    if tailOne is not None:
        tailOne.next = headTwo

    return newHead, newTail
