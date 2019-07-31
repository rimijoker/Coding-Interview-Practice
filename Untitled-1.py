#%%
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    val = l1.val + l2.val + c
    c = int(val / 10)
    ret = ListNode(val % 10 ) 
    
    if (l1.next != None or l2.next != None or c != 0):
      if l1.next == None:
        l1.next = ListNode(0)
      if l2.next == None:
        l2.next = ListNode(0)
      ret.next = self.addTwoNumbers(l1.next,l2.next,c)
    return ret

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)

l2 = ListNode(2)
l2.next = ListNode(2)
l2.next.next = ListNode(2)

result = Solution().addTwoNumbers(l1, l2)
#%%
while result:
  print (result.val)
  result = result.next
# 7 0 8

#%%
