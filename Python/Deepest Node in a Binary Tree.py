class Node(object) :
    def __init__(self, val) :
        self.val = val
        self.right = None
        self.left = None
    def __repr__(self) :
        return self.val
def deepest(node):
  if node and not node.left and not node.right:
    return (node, 1)  # Leaf and its depth

  if not node.left:  # Then the deepest node is on the right subtree
    return increment_depth(deepest(node.right))
  elif not node.right:  # Then the deepest node is on the left subtree
    return increment_depth(deepest(node.left))

  return increment_depth(
      max(deepest(node.left),
          deepest(node.right),
          key=lambda x: x[1]))  # Pick higher depth tuple and increment depth


def increment_depth(node_depth_tuple):
  node, depth = node_depth_tuple
  return (node, depth + 1)


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.left.right = Node('f')
root.right = Node('c')
print(deepest(root))
# (d, 3)