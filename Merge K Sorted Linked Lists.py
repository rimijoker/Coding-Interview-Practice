class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
    # Combine all nodes into an array
  arr = []
  for head in lists:
    current = head
    while current:
      arr.append(current.val)
      current = current.next
  new_head = current = Node(0)  # dummy head
  for val in sorted(arr):
    current.next = Node(val)
    current = current.next
  return new_head.next

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
c = merge([a, b])
print(c)
# 123456S