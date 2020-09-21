# O(N) time | O(1) space

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def shiftLinkedList(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        k %= length
        if length == 0:
            return head
        tail.next = head
        for _ in range(length - k):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head
