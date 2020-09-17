# O(N) time | O(1) space

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow, fast = head.next, head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            print(fast.val)
            return True

        except:
            return False
