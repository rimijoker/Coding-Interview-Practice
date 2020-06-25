# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None

        lead, follower = head, head
        while n:
            lead = lead.next
            n -= 1
        if not lead:
            return head.next

        while lead.next:
            lead = lead.next
            follower = follower.next
        follower.next = follower.next.next

        return head
