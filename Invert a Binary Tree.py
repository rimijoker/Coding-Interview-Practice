class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
  def preorder(self):
    print(self.value),
    if self.left: self.left.preorder()
    if self.right: self.right.preorder()

def invert(node):
  if not node:
    return node
  left = invert(node.left)
  right = invert(node.right)
  node.left, node.right = right, left
  return node



root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print("\n")
invert(root)
root.preorder()
# a c f b e d