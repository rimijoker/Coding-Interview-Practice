# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None: #corner cases
            return None
        odd_list = head #first node is odd
        even_list = head.next #second node is even
        even_head = even_list #this node is maintain to join odd tail with the even head
        while(even_list != None and even_list.next != None):
            odd_list.next = even_list.next #next odd will be adjacent to the even node 1->2->3
            odd_list = odd_list.next #moving the pointer to the next odd node
            even_list.next = odd_list.next #next even pointer will be adjacent to the odd node 1->2->3
            even_list = even_list.next #moving pointer to the next even node
        odd_list.next = even_head #joining odd tail to the even head
        return head